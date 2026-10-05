import contextlib
import copy
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import build


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.rows = copy.deepcopy(build.load())

    def test_current_data(self):
        self.assertEqual(build.validate(self.rows), [])
        self.assertEqual(build.validate_grannlan(self.rows, build.load_grannlan()), [])
        self.assertEqual(build.render(self.rows, build.load_grannlan()), build.OUT.read_text())

    def test_duplicate_identity_with_distinct_scope(self):
        staffanstorp = next(r for r in self.rows if r['kommun'] == 'Staffanstorp')
        burlov = next(r for r in self.rows if r['kommun'] == 'Burlöv')
        staffanstorp.update(scb_kommun=burlov['scb_kommun'], kommun=burlov['kommun'])
        errors = build.validate(self.rows)
        self.assertTrue(any('1231 står 2 gånger' in e for e in errors), errors)
        self.assertTrue(any('saknar SCB-kommun 1230' in e for e in errors), errors)

    def test_exact_scb_code_formats(self):
        for field, value, message in (
            ('scb_kommun', '0114000', 'exakt fyra siffror'),
            ('scb_kommun', '114', 'exakt fyra siffror'),
            ('scb_kommun', '０１１４', 'exakt fyra siffror'),
            ('scb_lan', '0', 'exakt två siffror'),
            ('scb_lan', '001', 'exakt två siffror'),
        ):
            with self.subTest(field=field, value=value):
                rows = copy.deepcopy(self.rows)
                rows[0][field] = value
                errors = build.validate(rows)
                self.assertTrue(any(message in e for e in errors), errors)

    def test_unknown_municipality(self):
        self.rows[0]['scb_kommun'] = '0199'
        errors = build.validate(self.rows)
        self.assertTrue(any('finns inte i SCB-referensen' in e for e in errors), errors)

    def test_reference_names_and_county(self):
        for field, value in (('kommun', 'Fel namn'), ('lan', 'Fel län'), ('scb_lan', '03')):
            with self.subTest(field=field):
                rows = copy.deepcopy(self.rows)
                rows[0][field] = value
                errors = build.validate(rows)
                self.assertTrue(any(f'{field} ska vara' in e for e in errors), errors)

    def test_missing_municipality(self):
        removed = self.rows.pop()
        errors = build.validate(self.rows)
        self.assertTrue(any(f"saknar SCB-kommun {removed['scb_kommun']}" in e for e in errors), errors)

    def test_scope_changes_remain_allowed(self):
        self.rows[0]['kommun_kod'] = 'zzz'
        self.assertEqual(build.validate(self.rows), [])

    def test_duplicate_scope_still_rejected(self):
        self.rows[1]['kommun_kod'] = self.rows[0]['kommun_kod']
        errors = build.validate(self.rows)
        self.assertTrue(any('används av 2 kommuner' in e for e in errors), errors)

    def test_missing_row_fields(self):
        for filename, columns, validator, rows in (
            ('regioner.csv', build.REGIONER_KOLUMNER, build.validate, self.rows),
            ('grannlan.csv', build.GRANNLAN_KOLUMNER,
             lambda r: build.validate_grannlan(self.rows, r), build.load_grannlan()),
        ):
            with self.subTest(filename=filename):
                rows = copy.deepcopy(rows)
                rows[0][columns[-1]] = None
                errors = validator(rows)
                self.assertTrue(any(f'{filename} rad 2: saknar' in e for e in errors), errors)

    def test_csv_header_validation_even_without_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'regioner.csv'
            path.write_text('scb_kommun,kommun\n')
            with self.assertRaisesRegex(ValueError, 'saknar kolumner'):
                build.load_csv(path, build.REGIONER_KOLUMNER)

    def test_extra_csv_fields(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'regioner.csv'
            path.write_text('scb_kommun,kommun\n0114,Upplands Väsby,extra\n')
            with self.assertRaisesRegex(ValueError, 'rad 2: för många fält'):
                build.load_csv(path, ['scb_kommun', 'kommun'])

    def test_invalid_data_fails_check_and_does_not_overwrite_output(self):
        self.rows[0]['scb_kommun'] += '000'
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'REGIONER.md'
            output.write_text('Behåll befintlig dokumentation')
            for args in (['build.py'], ['build.py', '--check']):
                with self.subTest(args=args), patch.object(build, 'load', return_value=self.rows), \
                        patch.object(build, 'OUT', output), patch.object(build.sys, 'argv', args), \
                        contextlib.redirect_stdout(io.StringIO()) as stdout:
                    self.assertEqual(build.main(), 1)
                    self.assertIn('FEL:', stdout.getvalue())
                    self.assertEqual(output.read_text(), 'Behåll befintlig dokumentation')

    def test_csv_error_is_reported_without_traceback(self):
        with patch.object(build, 'load', side_effect=ValueError('regioner.csv: saknar kolumner')), \
                contextlib.redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(build.main(), 1)
            self.assertIn('FEL: regioner.csv: saknar kolumner', stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
