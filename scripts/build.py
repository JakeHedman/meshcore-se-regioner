#!/usr/bin/env python3
"""Validerar data/regioner.csv och data/grannlan.csv och genererar REGIONER.md.

Kör:  python3 scripts/build.py          (validera + skriv REGIONER.md)
      python3 scripts/build.py --check  (validera + kontrollera att REGIONER.md är aktuell)
"""
import csv
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "regioner.csv"
GRANNLAN = ROOT / "data" / "grannlan.csv"
OUT = ROOT / "REGIONER.md"
GRUNDER = {"vedertagen", "kandidat", "krock", "reserv"}
VIA = {"land", "vatten", "omvand", "lokal"}
GRANNLAN_KOLUMNER = ["scb_kommun", "kommun", "scb_grannlan", "grannlan", "via"]
KOD = re.compile(r"^[a-z]{3}$")
SWEDISH_ORDER = str.maketrans({"å": "{", "ä": "|", "ö": "}"})


def swedish_sort_key(name):
    """Sortera å, ä och ö efter z utan beroende på systemets locale."""
    return name.casefold().translate(SWEDISH_ORDER)


def load():
    with CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_grannlan():
    with GRANNLAN.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate_grannlan(rows, grannlan):
    errors = []
    for nr, g in enumerate(grannlan, start=2):
        saknas = [k for k in GRANNLAN_KOLUMNER if g.get(k) is None]
        if saknas:
            return [f"grannlan.csv rad {nr}: saknar {', '.join(saknas)}"]
    kommuner = {r["scb_kommun"]: r for r in rows}
    lan = {r["scb_lan"]: r["lan"] for r in rows}
    for g in grannlan:
        where = f"grannlan.csv: {g['kommun']} ({g['scb_kommun']}) → {g['grannlan']}"
        kommun = kommuner.get(g["scb_kommun"])
        if not kommun:
            errors.append(f"{where}: kommunkoden finns inte i regioner.csv")
            continue
        if kommun["kommun"] != g["kommun"]:
            errors.append(f"{where}: kommunen heter '{kommun['kommun']}' i regioner.csv")
        if g["scb_grannlan"] not in lan:
            errors.append(f"{where}: länskoden {g['scb_grannlan']} finns inte i regioner.csv")
        elif lan[g["scb_grannlan"]] != g["grannlan"]:
            errors.append(f"{where}: länet heter '{lan[g['scb_grannlan']]}' i regioner.csv")
        if g["scb_grannlan"] == kommun["scb_lan"]:
            errors.append(f"{where}: det egna länet kan inte vara grannlän")
        if g["via"] not in VIA:
            errors.append(f"{where}: okänt värde i via '{g['via']}'")
    for (kommun, grann), n in Counter((g["scb_kommun"], g["scb_grannlan"]) for g in grannlan).items():
        if n > 1:
            errors.append(f"grannlan.csv: {kommun} → {grann} står {n} gånger")
    par = {(g["scb_kommun"][:2], g["scb_grannlan"]) for g in grannlan}
    for a, b in sorted(par):
        if (b, a) not in par:
            errors.append(f"grannlan.csv: {lan.get(a, a)} når {lan.get(b, b)} men inte tvärtom")
    return errors


def validate(rows):
    errors = []
    if len(rows) != 290:
        errors.append(f"förväntade 290 kommuner, hittade {len(rows)}")
    lan_kod = {}
    for r in rows:
        where = f"{r['kommun']} ({r['scb_kommun']})"
        if not KOD.match(r["lan_kod"]):
            errors.append(f"{where}: länskoden '{r['lan_kod']}' är inte tre tecken a-z")
        if not KOD.match(r["kommun_kod"]):
            errors.append(
                f"{where}: kommunkoden '{r['kommun_kod']}' är inte tre tecken a-z"
            )
        if r["grund"] not in GRUNDER:
            errors.append(f"{where}: okänd grund '{r['grund']}'")
        if not r["scb_kommun"].startswith(r["scb_lan"]):
            errors.append(f"{where}: SCB-kommunkoden hör inte till län {r['scb_lan']}")
        if lan_kod.setdefault(r["scb_lan"], r["lan_kod"]) != r["lan_kod"]:
            errors.append(f"{where}: länet {r['scb_lan']} har flera olika länskoder")
    for kod, n in Counter(lan_kod.values()).items():
        if n > 1:
            errors.append(f"länskoden '{kod}' används av {n} län")
    for (lan, kod), n in Counter((r["lan_kod"], r["kommun_kod"]) for r in rows).items():
        if n > 1:
            errors.append(f"se-{lan}-{kod} används av {n} kommuner i samma län")
    return errors


def render(rows, grannlan):
    lan_kod = {r["scb_lan"]: r["lan_kod"] for r in rows}
    grannar = {}
    for g in grannlan:
        grannar.setdefault(g["scb_kommun"], []).append(g["scb_grannlan"])
    by_lan = OrderedDict()
    for r in rows:
        by_lan.setdefault(r["scb_lan"], []).append(r)
    out = [
        "# Alla regioner",
        "",
        "Den här filen genereras från [data/regioner.csv](data/regioner.csv) med `python3 scripts/build.py`.",
        "Ändra inte här – ändra i CSV-filen och kör skriptet.",
        "",
        "**Grund:** *vedertagen* = känd förkortning med belägg · *kandidat* = förkortning med svagt belägg ·",
        "*krock* = ändrad eftersom tre första bokstäverna krockar inom länet · *reserv* = tre första bokstäverna.",
        "",
        "**Grannlän:** möjliga grannlän enligt avståndsmodellen, från [data/grannlan.csv](data/grannlan.csv).",
        "En kantrepeater i kommunen kan bära ett av dem. Se *Grannlän* i [README.md](README.md#grannlän).",
        "",
        "## Hitta ditt län",
        "",
    ]
    for ks in by_lan.values():
        out.append(f"- [{ks[0]['lan']}](#se-{ks[0]['lan_kod']})")
    out.append("")
    for lan, ks in by_lan.items():
        lk = ks[0]["lan_kod"]
        out += [
            f'<a id="se-{lk}"></a>',
            "",
            f"## {ks[0]['lan']} – `se-{lk}`",
            "",
            f"Ersätter `se{lan}`.",
            "",
            "| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for r in sorted(ks, key=lambda r: swedish_sort_key(r["kommun"])):
            alt = ", ".join(f"`{a}`" for a in r["alternativ"].split())
            grann = ", ".join(
                f"`se-{lan_kod[g]}`" for g in sorted(grannar.get(r["scb_kommun"], []))
            )
            out.append(
                f"| {r['kommun']} | `se-{lk}-{r['kommun_kod']}` | `se{r['scb_kommun']}` | {r['grund']} | {alt} | {grann} |"
            )
        out.append("")
    return "\n".join(out)


def main():
    rows = load()
    grannlan = load_grannlan()
    errors = validate(rows)
    if not errors:
        errors = validate_grannlan(rows, grannlan)
    if errors:
        print("\n".join(f"FEL: {e}" for e in errors))
        return 1
    text = render(rows, grannlan)
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("FEL: REGIONER.md är inte aktuell – kör python3 scripts/build.py")
            return 1
        print(f"OK: {len(rows)} kommuner, inga krockar, REGIONER.md aktuell")
        return 0
    OUT.write_text(text, encoding="utf-8")
    print(f"OK: {len(rows)} kommuner, inga krockar, skrev {OUT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
