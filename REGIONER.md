# Alla regioner

Den här filen genereras från [data/regioner.csv](data/regioner.csv) med `python3 scripts/build.py`.
Ändra inte här – ändra i CSV-filen och kör skriptet.

**Grund:** *vedertagen* = känd förkortning med belägg · *kandidat* = förkortning med svagt belägg ·
*krock* = ändrad eftersom tre första bokstäverna krockar inom länet · *reserv* = tre första bokstäverna.

**Grannlän:** län som ligger inom räckhåll från kommunen, från [data/grannlan.csv](data/grannlan.csv).
En kantrepeater i kommunen kan bära ett av dem. Se *Grannlän* i [README.md](README.md#grannlän).

## Stockholms län – `se-sth`

Ersätter `se01`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Botkyrka | `se-sth-bot` | `se0127` | reserv |  | `se-upp`, `se-sor`, `se-ost`, `se-vml` |
| Danderyd | `se-sth-dan` | `se0162` | reserv |  | `se-upp`, `se-sor` |
| Ekerö | `se-sth-eke` | `se0125` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Haninge | `se-sth-han` | `se0136` | reserv |  | `se-upp`, `se-sor`, `se-ost`, `se-gtl` |
| Huddinge | `se-sth-hud` | `se0126` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Järfälla | `se-sth-jar` | `se0123` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Lidingö | `se-sth-lid` | `se0186` | reserv | `lio` | `se-upp`, `se-sor` |
| Nacka | `se-sth-nac` | `se0182` | reserv |  | `se-upp`, `se-sor` |
| Norrtälje | `se-sth-nor` | `se0188` | reserv | `ntl`, `tal` | `se-upp`, `se-sor`, `se-gav` |
| Nykvarn | `se-sth-nyk` | `se0140` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Nynäshamn | `se-sth-nyn` | `se0192` | reserv |  | `se-upp`, `se-sor`, `se-ost` |
| Salem | `se-sth-sal` | `se0128` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Sigtuna | `se-sth-sig` | `se0191` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Sollentuna | `se-sth-slt` | `se0163` | krock | `sol` | `se-upp`, `se-sor` |
| Solna | `se-sth-sol` | `se0184` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Stockholm | `se-sth-sth` | `se0180` | vedertagen | `sto` | `se-upp`, `se-sor`, `se-vml` |
| Sundbyberg | `se-sth-sbb` | `se0183` | kandidat | `sun` | `se-upp`, `se-sor` |
| Södertälje | `se-sth-tlj` | `se0181` | kandidat | `sod`, `stl` | `se-upp`, `se-sor`, `se-ost`, `se-vml` |
| Tyresö | `se-sth-tyr` | `se0138` | reserv |  | `se-upp`, `se-sor` |
| Täby | `se-sth-tab` | `se0160` | reserv |  | `se-upp`, `se-sor` |
| Upplands Väsby | `se-sth-vas` | `se0114` | kandidat | `upp`, `uvb` | `se-upp`, `se-sor`, `se-vml` |
| Upplands-Bro | `se-sth-upp` | `se0139` | reserv |  | `se-upp`, `se-sor`, `se-vml` |
| Vallentuna | `se-sth-val` | `se0115` | reserv |  | `se-upp` |
| Vaxholm | `se-sth-vax` | `se0187` | reserv |  | `se-upp`, `se-sor` |
| Värmdö | `se-sth-var` | `se0120` | reserv |  | `se-upp`, `se-sor` |
| Österåker | `se-sth-ost` | `se0117` | reserv |  | `se-upp`, `se-sor` |

## Uppsala län – `se-upp`

Ersätter `se03`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Enköping | `se-upp-enk` | `se0381` | reserv |  | `se-sth`, `se-sor`, `se-vml`, `se-dal`, `se-gav` |
| Heby | `se-upp-heb` | `se0331` | reserv |  | `se-sth`, `se-sor`, `se-vml`, `se-dal`, `se-gav` |
| Håbo | `se-upp-hab` | `se0305` | reserv |  | `se-sth`, `se-sor`, `se-vml` |
| Knivsta | `se-upp-kni` | `se0330` | reserv |  | `se-sth`, `se-sor`, `se-vml` |
| Tierp | `se-upp-tie` | `se0360` | reserv |  | `se-sth`, `se-vml`, `se-dal`, `se-gav` |
| Uppsala | `se-upp-upp` | `se0380` | reserv | `ups` | `se-sth`, `se-sor`, `se-vml`, `se-dal`, `se-gav` |
| Älvkarleby | `se-upp-alv` | `se0319` | reserv |  | `se-sth`, `se-vml`, `se-dal`, `se-gav` |
| Östhammar | `se-upp-ost` | `se0382` | reserv |  | `se-sth`, `se-gav` |

## Södermanlands län – `se-sor`

Ersätter `se04`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Eskilstuna | `se-sor-esk` | `se0484` | reserv | `etu`, `tun` | `se-sth`, `se-upp`, `se-ost`, `se-ore`, `se-vml` |
| Flen | `se-sor-fle` | `se0482` | reserv |  | `se-sth`, `se-upp`, `se-ost`, `se-ore`, `se-vml` |
| Gnesta | `se-sor-gne` | `se0461` | reserv |  | `se-sth`, `se-upp`, `se-vml` |
| Katrineholm | `se-sor-kat` | `se0483` | reserv | `khm` | `se-ost`, `se-ore`, `se-vml` |
| Nyköping | `se-sor-nyk` | `se0480` | reserv |  | `se-sth`, `se-upp`, `se-ost`, `se-kal`, `se-ore` |
| Oxelösund | `se-sor-oxe` | `se0481` | reserv |  | `se-sth`, `se-ost`, `se-kal` |
| Strängnäs | `se-sor-str` | `se0486` | reserv |  | `se-sth`, `se-upp`, `se-vml` |
| Trosa | `se-sor-tro` | `se0488` | reserv |  | `se-sth`, `se-upp`, `se-ost` |
| Vingåker | `se-sor-vin` | `se0428` | reserv |  | `se-ost`, `se-ore`, `se-vml` |

## Östergötlands län – `se-ost`

Ersätter `se05`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Boxholm | `se-ost-box` | `se0560` | reserv |  | `se-jkp`, `se-kal`, `se-vgr` |
| Finspång | `se-ost-fin` | `se0562` | reserv |  | `se-sor`, `se-ore`, `se-vml` |
| Kinda | `se-ost-kin` | `se0513` | reserv |  | `se-jkp`, `se-kal` |
| Linköping | `se-ost-lkp` | `se0580` | vedertagen | `lpi` | `se-sor`, `se-jkp`, `se-kal`, `se-ore` |
| Mjölby | `se-ost-mjo` | `se0586` | reserv |  | `se-jkp`, `se-kal`, `se-vgr`, `se-ore` |
| Motala | `se-ost-mot` | `se0583` | reserv |  | `se-sor`, `se-jkp`, `se-vgr`, `se-ore` |
| Norrköping | `se-ost-nkp` | `se0581` | vedertagen | `nrk` | `se-sth`, `se-sor`, `se-kal`, `se-ore` |
| Söderköping | `se-ost-sod` | `se0582` | reserv | `skp`, `sor` | `se-sth`, `se-sor`, `se-kal` |
| Vadstena | `se-ost-vad` | `se0584` | reserv |  | `se-jkp`, `se-vgr`, `se-ore` |
| Valdemarsvik | `se-ost-val` | `se0563` | reserv |  | `se-sth`, `se-sor`, `se-kal` |
| Ydre | `se-ost-ydr` | `se0512` | reserv |  | `se-jkp`, `se-kal` |
| Åtvidaberg | `se-ost-atv` | `se0561` | reserv |  | `se-kal` |
| Ödeshög | `se-ost-ode` | `se0509` | reserv |  | `se-jkp`, `se-vgr`, `se-ore` |

## Jönköpings län – `se-jkp`

Ersätter `se06`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Aneby | `se-jkp-ane` | `se0604` | reserv |  | `se-ost`, `se-kal`, `se-vgr` |
| Eksjö | `se-jkp-eks` | `se0686` | reserv |  | `se-ost`, `se-kro`, `se-kal` |
| Gislaved | `se-jkp-gis` | `se0662` | reserv |  | `se-kro`, `se-hal`, `se-vgr` |
| Gnosjö | `se-jkp-gno` | `se0617` | reserv |  | `se-kro`, `se-hal`, `se-vgr` |
| Habo | `se-jkp-hab` | `se0643` | reserv |  | `se-ost`, `se-vgr`, `se-ore` |
| Jönköping | `se-jkp-jkp` | `se0680` | vedertagen | `jkg`, `jon` | `se-ost`, `se-vgr`, `se-ore` |
| Mullsjö | `se-jkp-mul` | `se0642` | reserv |  | `se-ost`, `se-vgr` |
| Nässjö | `se-jkp-nas` | `se0682` | reserv | `nsj` | `se-ost`, `se-kro`, `se-kal`, `se-vgr` |
| Sävsjö | `se-jkp-sav` | `se0684` | reserv |  | `se-ost`, `se-kro`, `se-kal` |
| Tranås | `se-jkp-tra` | `se0687` | reserv |  | `se-ost`, `se-kal`, `se-vgr` |
| Vaggeryd | `se-jkp-vag` | `se0665` | reserv |  | `se-kro`, `se-hal`, `se-vgr` |
| Vetlanda | `se-jkp-vet` | `se0685` | reserv |  | `se-ost`, `se-kro`, `se-kal` |
| Värnamo | `se-jkp-var` | `se0683` | reserv | `vmo` | `se-kro`, `se-hal`, `se-vgr` |

## Kronobergs län – `se-kro`

Ersätter `se07`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Alvesta | `se-kro-alv` | `se0764` | reserv |  | `se-jkp`, `se-blk`, `se-ska` |
| Lessebo | `se-kro-les` | `se0761` | reserv |  | `se-jkp`, `se-kal`, `se-blk` |
| Ljungby | `se-kro-lju` | `se0781` | reserv | `lby` | `se-jkp`, `se-blk`, `se-ska`, `se-hal`, `se-vgr` |
| Markaryd | `se-kro-mar` | `se0767` | reserv |  | `se-jkp`, `se-blk`, `se-ska`, `se-hal` |
| Tingsryd | `se-kro-tin` | `se0763` | reserv |  | `se-jkp`, `se-kal`, `se-blk`, `se-ska` |
| Uppvidinge | `se-kro-upp` | `se0760` | reserv |  | `se-jkp`, `se-kal`, `se-blk` |
| Växjö | `se-kro-vxo` | `se0780` | vedertagen | `vax` | `se-jkp`, `se-kal`, `se-blk`, `se-ska` |
| Älmhult | `se-kro-alm` | `se0765` | reserv |  | `se-jkp`, `se-blk`, `se-ska`, `se-hal` |

## Kalmar län – `se-kal`

Ersätter `se08`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Borgholm | `se-kal-bor` | `se0885` | reserv |  | `se-ost`, `se-gtl`, `se-blk` |
| Emmaboda | `se-kal-emm` | `se0862` | reserv |  | `se-kro`, `se-blk` |
| Hultsfred | `se-kal-hul` | `se0860` | reserv |  | `se-ost`, `se-jkp`, `se-kro` |
| Högsby | `se-kal-hog` | `se0821` | reserv |  | `se-jkp`, `se-kro` |
| Kalmar | `se-kal-kal` | `se0880` | reserv | `klr` | `se-kro`, `se-blk` |
| Mönsterås | `se-kal-mon` | `se0861` | reserv |  | `se-jkp`, `se-kro`, `se-blk` |
| Mörbylånga | `se-kal-mor` | `se0840` | reserv |  | `se-blk` |
| Nybro | `se-kal-nyb` | `se0881` | reserv |  | `se-jkp`, `se-kro`, `se-blk` |
| Oskarshamn | `se-kal-osk` | `se0882` | reserv |  | `se-ost`, `se-jkp`, `se-kro`, `se-gtl` |
| Torsås | `se-kal-tor` | `se0834` | reserv |  | `se-kro`, `se-blk` |
| Vimmerby | `se-kal-vim` | `se0884` | reserv |  | `se-ost`, `se-jkp` |
| Västervik | `se-kal-vas` | `se0883` | reserv | `vvk`, `vik` | `se-sor`, `se-ost`, `se-jkp` |

## Gotlands län – `se-gtl`

Ersätter `se09`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Gotland | `se-gtl-got` | `se0980` | reserv | `gtl`, `vby` | `se-sth`, `se-kal` |

## Blekinge län – `se-blk`

Ersätter `se10`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Karlshamn | `se-blk-khn` | `se1082` | krock | `kha` | `se-kro`, `se-kal`, `se-ska` |
| Karlskrona | `se-blk-kar` | `se1080` | reserv | `kna`, `pin` | `se-kro`, `se-kal`, `se-ska` |
| Olofström | `se-blk-olo` | `se1060` | reserv |  | `se-kro`, `se-ska` |
| Ronneby | `se-blk-ron` | `se1081` | reserv | `rby` | `se-kro`, `se-kal`, `se-ska` |
| Sölvesborg | `se-blk-sol` | `se1083` | reserv | `sbg` | `se-kro`, `se-ska` |

## Skåne län – `se-ska`

Ersätter `se12`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Bjuv | `se-ska-bju` | `se1260` | reserv |  | `se-hal` |
| Bromölla | `se-ska-bro` | `se1272` | reserv | `bma` | `se-kro`, `se-blk` |
| Burlöv | `se-ska-bur` | `se1231` | reserv |  |  |
| Båstad | `se-ska-bas` | `se1278` | reserv |  | `se-kro`, `se-hal` |
| Eslöv | `se-ska-esl` | `se1285` | reserv |  | `se-hal` |
| Helsingborg | `se-ska-hbg` | `se1283` | vedertagen |  | `se-hal` |
| Hässleholm | `se-ska-has` | `se1293` | reserv | `hlm` | `se-kro`, `se-blk`, `se-hal` |
| Höganäs | `se-ska-hog` | `se1284` | reserv | `hns` | `se-hal` |
| Hörby | `se-ska-hor` | `se1266` | reserv |  |  |
| Höör | `se-ska-hoo` | `se1267` | reserv |  | `se-kro`, `se-hal` |
| Klippan | `se-ska-kli` | `se1276` | reserv |  | `se-kro`, `se-hal` |
| Kristianstad | `se-ska-kst` | `se1290` | kandidat | `krs` | `se-kro`, `se-blk` |
| Kävlinge | `se-ska-kav` | `se1261` | reserv |  | `se-hal` |
| Landskrona | `se-ska-lan` | `se1282` | reserv | `lkr` | `se-hal` |
| Lomma | `se-ska-lom` | `se1262` | reserv |  |  |
| Lund | `se-ska-lun` | `se1281` | reserv |  |  |
| Malmö | `se-ska-mal` | `se1280` | reserv | `mmo` |  |
| Osby | `se-ska-osb` | `se1273` | reserv |  | `se-kro`, `se-blk`, `se-hal` |
| Perstorp | `se-ska-per` | `se1275` | reserv |  | `se-kro`, `se-hal` |
| Simrishamn | `se-ska-sim` | `se1291` | reserv |  | `se-blk` |
| Sjöbo | `se-ska-sjo` | `se1265` | reserv |  |  |
| Skurup | `se-ska-sku` | `se1264` | reserv |  |  |
| Staffanstorp | `se-ska-sta` | `se1230` | reserv | `stp` |  |
| Svalöv | `se-ska-sva` | `se1214` | reserv |  | `se-hal` |
| Svedala | `se-ska-sve` | `se1263` | reserv |  |  |
| Tomelilla | `se-ska-tom` | `se1270` | reserv |  |  |
| Trelleborg | `se-ska-tre` | `se1287` | reserv | `tbg` |  |
| Vellinge | `se-ska-vel` | `se1233` | reserv |  |  |
| Ystad | `se-ska-yst` | `se1286` | reserv | `ysd` | `se-blk` |
| Ängelholm | `se-ska-ang` | `se1292` | reserv | `agh` | `se-kro`, `se-hal` |
| Åstorp | `se-ska-ast` | `se1277` | reserv |  | `se-kro`, `se-hal` |
| Örkelljunga | `se-ska-ork` | `se1257` | reserv |  | `se-kro`, `se-hal` |
| Östra Göinge | `se-ska-ost` | `se1256` | reserv |  | `se-kro`, `se-blk`, `se-hal` |

## Hallands län – `se-hal`

Ersätter `se13`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Falkenberg | `se-hal-fbg` | `se1382` | vedertagen |  | `se-jkp`, `se-kro`, `se-ska`, `se-vgr` |
| Halmstad | `se-hal-hst` | `se1380` | kandidat | `hal` | `se-jkp`, `se-kro`, `se-ska`, `se-vgr` |
| Hylte | `se-hal-hyl` | `se1315` | reserv |  | `se-jkp`, `se-kro`, `se-vgr` |
| Kungsbacka | `se-hal-kba` | `se1384` | vedertagen |  | `se-vgr` |
| Laholm | `se-hal-lah` | `se1381` | reserv |  | `se-jkp`, `se-kro`, `se-ska` |
| Varberg | `se-hal-vbg` | `se1383` | vedertagen |  | `se-jkp`, `se-ska`, `se-vgr` |

## Västra Götalands län – `se-vgr`

Ersätter `se14`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Ale | `se-vgr-ale` | `se1440` | reserv |  | `se-hal` |
| Alingsås | `se-vgr-ali` | `se1489` | reserv |  | `se-hal` |
| Bengtsfors | `se-vgr-ben` | `se1460` | reserv |  | `se-var` |
| Bollebygd | `se-vgr-bol` | `se1443` | reserv |  | `se-hal` |
| Borås | `se-vgr-bor` | `se1490` | reserv | `bas` | `se-jkp`, `se-hal` |
| Dals-Ed | `se-vgr-dal` | `se1438` | reserv |  | `se-var` |
| Essunga | `se-vgr-ess` | `se1445` | reserv |  | `se-jkp` |
| Falköping | `se-vgr-fkp` | `se1499` | kandidat | `fal` | `se-jkp` |
| Färgelanda | `se-vgr-far` | `se1439` | reserv |  |  |
| Grästorp | `se-vgr-gra` | `se1444` | reserv |  | `se-var` |
| Gullspång | `se-vgr-gul` | `se1447` | reserv |  | `se-ost`, `se-var`, `se-ore` |
| Göteborg | `se-vgr-gbg` | `se1480` | vedertagen | `got` | `se-hal` |
| Götene | `se-vgr-got` | `se1471` | reserv |  | `se-var` |
| Herrljunga | `se-vgr-her` | `se1466` | reserv |  | `se-jkp` |
| Hjo | `se-vgr-hjo` | `se1497` | reserv |  | `se-ost`, `se-jkp`, `se-ore` |
| Härryda | `se-vgr-har` | `se1401` | reserv |  | `se-hal` |
| Karlsborg | `se-vgr-kar` | `se1446` | reserv |  | `se-ost`, `se-jkp`, `se-var`, `se-ore` |
| Kungälv | `se-vgr-kun` | `se1482` | reserv |  | `se-hal` |
| Lerum | `se-vgr-ler` | `se1441` | reserv |  | `se-hal` |
| Lidköping | `se-vgr-lid` | `se1494` | reserv | `lkp` | `se-var` |
| Lilla Edet | `se-vgr-lil` | `se1462` | reserv |  |  |
| Lysekil | `se-vgr-lys` | `se1484` | reserv |  |  |
| Mariestad | `se-vgr-mar` | `se1493` | reserv |  | `se-var`, `se-ore` |
| Mark | `se-vgr-mrk` | `se1463` | krock | `mar` | `se-jkp`, `se-hal` |
| Mellerud | `se-vgr-mel` | `se1461` | reserv |  | `se-var` |
| Munkedal | `se-vgr-mun` | `se1430` | reserv |  |  |
| Mölndal | `se-vgr-mdl` | `se1481` | kandidat | `mol` | `se-hal` |
| Orust | `se-vgr-oru` | `se1421` | reserv |  | `se-hal` |
| Partille | `se-vgr-par` | `se1402` | reserv |  | `se-hal` |
| Skara | `se-vgr-ska` | `se1495` | reserv |  | `se-jkp` |
| Skövde | `se-vgr-sko` | `se1496` | reserv | `sde`, `kvb` | `se-ost`, `se-jkp`, `se-ore` |
| Sotenäs | `se-vgr-sot` | `se1427` | reserv |  |  |
| Stenungsund | `se-vgr-ste` | `se1415` | reserv |  | `se-hal` |
| Strömstad | `se-vgr-str` | `se1486` | reserv | `std` | `se-var` |
| Svenljunga | `se-vgr-sve` | `se1465` | reserv |  | `se-jkp`, `se-kro`, `se-hal` |
| Tanum | `se-vgr-tan` | `se1435` | reserv |  | `se-var` |
| Tibro | `se-vgr-tib` | `se1472` | reserv |  | `se-ost`, `se-jkp`, `se-ore` |
| Tidaholm | `se-vgr-tid` | `se1498` | reserv |  | `se-ost`, `se-jkp` |
| Tjörn | `se-vgr-tjo` | `se1419` | reserv |  | `se-hal` |
| Tranemo | `se-vgr-tra` | `se1452` | reserv |  | `se-jkp`, `se-hal` |
| Trollhättan | `se-vgr-thn` | `se1488` | kandidat | `tro` |  |
| Töreboda | `se-vgr-tor` | `se1473` | reserv |  | `se-ost`, `se-var`, `se-ore` |
| Uddevalla | `se-vgr-udd` | `se1485` | reserv |  | `se-hal` |
| Ulricehamn | `se-vgr-ulr` | `se1491` | reserv |  | `se-jkp` |
| Vara | `se-vgr-var` | `se1470` | reserv |  | `se-jkp` |
| Vänersborg | `se-vgr-vbg` | `se1487` | kandidat | `van` | `se-var` |
| Vårgårda | `se-vgr-vgd` | `se1442` | krock | `var` | `se-hal` |
| Åmål | `se-vgr-ama` | `se1492` | reserv |  | `se-var` |
| Öckerö | `se-vgr-ock` | `se1407` | reserv |  | `se-hal` |

## Värmlands län – `se-var`

Ersätter `se17`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Arvika | `se-var-arv` | `se1784` | reserv |  | `se-vgr` |
| Eda | `se-var-eda` | `se1730` | reserv |  | `se-vgr` |
| Filipstad | `se-var-fil` | `se1782` | reserv |  | `se-ore`, `se-dal` |
| Forshaga | `se-var-for` | `se1763` | reserv |  |  |
| Grums | `se-var-gru` | `se1764` | reserv |  | `se-vgr` |
| Hagfors | `se-var-hag` | `se1783` | reserv |  | `se-ore`, `se-dal` |
| Hammarö | `se-var-ham` | `se1761` | reserv |  | `se-vgr` |
| Karlstad | `se-var-kar` | `se1780` | reserv | `ksd` | `se-vgr`, `se-ore` |
| Kil | `se-var-kil` | `se1715` | reserv |  |  |
| Kristinehamn | `se-var-kri` | `se1781` | reserv | `khn` | `se-vgr`, `se-ore` |
| Munkfors | `se-var-mun` | `se1762` | reserv |  | `se-ore`, `se-dal` |
| Storfors | `se-var-sto` | `se1760` | reserv |  | `se-vgr`, `se-ore` |
| Sunne | `se-var-sun` | `se1766` | reserv |  | `se-dal` |
| Säffle | `se-var-saf` | `se1785` | reserv |  | `se-vgr` |
| Torsby | `se-var-tor` | `se1737` | reserv |  | `se-dal` |
| Årjäng | `se-var-arj` | `se1765` | reserv |  | `se-vgr` |

## Örebro län – `se-ore`

Ersätter `se18`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Askersund | `se-ore-ask` | `se1882` | reserv |  | `se-sor`, `se-ost`, `se-jkp`, `se-vgr`, `se-var` |
| Degerfors | `se-ore-deg` | `se1862` | reserv |  | `se-vgr`, `se-var` |
| Hallsberg | `se-ore-hal` | `se1861` | reserv |  | `se-sor`, `se-ost`, `se-vgr`, `se-var`, `se-vml` |
| Hällefors | `se-ore-hlf` | `se1863` | krock | `hae` | `se-var`, `se-vml`, `se-dal` |
| Karlskoga | `se-ore-kga` | `se1883` | kandidat | `kar` | `se-vgr`, `se-var` |
| Kumla | `se-ore-kum` | `se1881` | reserv |  | `se-sor`, `se-ost`, `se-vgr`, `se-var`, `se-vml` |
| Laxå | `se-ore-lax` | `se1860` | reserv |  | `se-ost`, `se-vgr`, `se-var` |
| Lekeberg | `se-ore-lek` | `se1814` | reserv |  | `se-sor`, `se-ost`, `se-vgr`, `se-var`, `se-vml` |
| Lindesberg | `se-ore-lbg` | `se1885` | kandidat | `lin` | `se-sor`, `se-var`, `se-vml`, `se-dal` |
| Ljusnarsberg | `se-ore-lju` | `se1864` | reserv |  | `se-var`, `se-vml`, `se-dal` |
| Nora | `se-ore-nor` | `se1884` | reserv |  | `se-var`, `se-vml`, `se-dal` |
| Örebro | `se-ore-ore` | `se1880` | reserv | `orb` | `se-sor`, `se-ost`, `se-var`, `se-vml`, `se-dal` |

## Västmanlands län – `se-vml`

Ersätter `se19`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Arboga | `se-vml-arb` | `se1984` | reserv |  | `se-sor`, `se-ost`, `se-ore`, `se-dal` |
| Fagersta | `se-vml-fag` | `se1982` | reserv |  | `se-upp`, `se-ore`, `se-dal` |
| Hallstahammar | `se-vml-hal` | `se1961` | reserv |  | `se-sth`, `se-upp`, `se-sor`, `se-ore`, `se-dal` |
| Kungsör | `se-vml-kun` | `se1960` | reserv | `ksr` | `se-sth`, `se-upp`, `se-sor`, `se-ost`, `se-ore` |
| Köping | `se-vml-kop` | `se1983` | reserv |  | `se-sth`, `se-upp`, `se-sor`, `se-ore`, `se-dal` |
| Norberg | `se-vml-nor` | `se1962` | reserv |  | `se-upp`, `se-ore`, `se-dal`, `se-gav` |
| Sala | `se-vml-sal` | `se1981` | reserv |  | `se-upp`, `se-sor`, `se-ore`, `se-dal`, `se-gav` |
| Skinnskatteberg | `se-vml-ski` | `se1904` | reserv |  | `se-sor`, `se-ore`, `se-dal` |
| Surahammar | `se-vml-sur` | `se1907` | reserv |  | `se-upp`, `se-sor`, `se-ore`, `se-dal` |
| Västerås | `se-vml-vas` | `se1980` | reserv | `vst` | `se-sth`, `se-upp`, `se-sor`, `se-ore`, `se-dal` |

## Dalarnas län – `se-dal`

Ersätter `se20`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Avesta | `se-dal-ave` | `se2084` | reserv |  | `se-upp`, `se-vml`, `se-gav` |
| Borlänge | `se-dal-blg` | `se2081` | kandidat | `bor` | `se-ore`, `se-vml`, `se-gav` |
| Falun | `se-dal-fal` | `se2080` | reserv |  | `se-vml`, `se-gav` |
| Gagnef | `se-dal-gag` | `se2026` | reserv |  | `se-var`, `se-ore` |
| Hedemora | `se-dal-hed` | `se2083` | reserv |  | `se-upp`, `se-ore`, `se-vml`, `se-gav` |
| Leksand | `se-dal-lek` | `se2029` | reserv | `lsd` | `se-gav` |
| Ludvika | `se-dal-lud` | `se2085` | reserv |  | `se-var`, `se-ore`, `se-vml` |
| Malung-Sälen | `se-dal-mal` | `se2023` | reserv | `sal` | `se-var`, `se-ore`, `se-jam` |
| Mora | `se-dal-mor` | `se2062` | reserv |  | `se-var`, `se-gav`, `se-jam` |
| Orsa | `se-dal-ors` | `se2034` | reserv |  | `se-gav`, `se-jam` |
| Rättvik | `se-dal-rat` | `se2031` | reserv |  | `se-gav`, `se-jam` |
| Smedjebacken | `se-dal-sme` | `se2061` | reserv |  | `se-var`, `se-ore`, `se-vml`, `se-gav` |
| Säter | `se-dal-sat` | `se2082` | reserv |  | `se-ore`, `se-vml`, `se-gav` |
| Vansbro | `se-dal-van` | `se2021` | reserv |  | `se-var`, `se-ore` |
| Älvdalen | `se-dal-alv` | `se2039` | reserv |  | `se-var`, `se-gav`, `se-jam` |

## Gävleborgs län – `se-gav`

Ersätter `se21`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Bollnäs | `se-gav-bol` | `se2183` | reserv |  | `se-dal` |
| Gävle | `se-gav-gav` | `se2180` | reserv | `gvx` | `se-sth`, `se-upp`, `se-vml`, `se-dal` |
| Hofors | `se-gav-hof` | `se2104` | reserv |  | `se-upp`, `se-vml`, `se-dal` |
| Hudiksvall | `se-gav-hud` | `se2184` | vedertagen | `huv` | `se-vnl`, `se-jam` |
| Ljusdal | `se-gav-lju` | `se2161` | reserv |  | `se-dal`, `se-vnl`, `se-jam` |
| Nordanstig | `se-gav-nor` | `se2132` | reserv |  | `se-vnl`, `se-jam` |
| Ockelbo | `se-gav-ock` | `se2101` | reserv |  | `se-upp`, `se-dal` |
| Ovanåker | `se-gav-ova` | `se2121` | reserv |  | `se-dal`, `se-jam` |
| Sandviken | `se-gav-san` | `se2181` | reserv |  | `se-upp`, `se-vml`, `se-dal` |
| Söderhamn | `se-gav-sod` | `se2182` | reserv | `soo` | `se-upp`, `se-dal` |

## Västernorrlands län – `se-vnl`

Ersätter `se22`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Härnösand | `se-vnl-har` | `se2280` | reserv | `hos` | `se-gav`, `se-jam` |
| Kramfors | `se-vnl-kra` | `se2282` | reserv |  | `se-gav`, `se-jam`, `se-vbt` |
| Sollefteå | `se-vnl-sol` | `se2283` | reserv | `sla` | `se-jam`, `se-vbt` |
| Sundsvall | `se-vnl-sun` | `se2281` | reserv | `svl` | `se-gav`, `se-jam` |
| Timrå | `se-vnl-tim` | `se2262` | reserv |  | `se-gav`, `se-jam` |
| Ånge | `se-vnl-ang` | `se2260` | reserv |  | `se-gav`, `se-jam` |
| Örnsköldsvik | `se-vnl-ovk` | `se2284` | vedertagen | `ovi` | `se-jam`, `se-vbt` |

## Jämtlands län – `se-jam`

Ersätter `se23`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Berg | `se-jam-ber` | `se2326` | reserv |  | `se-gav`, `se-vnl` |
| Bräcke | `se-jam-bra` | `se2305` | reserv |  | `se-gav`, `se-vnl` |
| Härjedalen | `se-jam-har` | `se2361` | reserv |  | `se-dal`, `se-gav`, `se-vnl` |
| Krokom | `se-jam-kro` | `se2309` | reserv |  |  |
| Ragunda | `se-jam-rag` | `se2303` | reserv |  | `se-vnl` |
| Strömsund | `se-jam-str` | `se2313` | reserv |  | `se-vnl`, `se-vbt` |
| Åre | `se-jam-are` | `se2321` | reserv |  |  |
| Östersund | `se-jam-osd` | `se2380` | kandidat | `ost` | `se-vnl` |

## Västerbottens län – `se-vbt`

Ersätter `se24`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Bjurholm | `se-vbt-bju` | `se2403` | reserv |  | `se-vnl` |
| Dorotea | `se-vbt-dor` | `se2425` | reserv |  | `se-vnl`, `se-jam` |
| Lycksele | `se-vbt-lyc` | `se2481` | reserv |  | `se-vnl`, `se-nbt` |
| Malå | `se-vbt-mal` | `se2418` | reserv |  | `se-nbt` |
| Nordmaling | `se-vbt-nor` | `se2401` | reserv |  | `se-vnl` |
| Norsjö | `se-vbt-nsj` | `se2417` | krock |  | `se-nbt` |
| Robertsfors | `se-vbt-rob` | `se2409` | reserv |  |  |
| Skellefteå | `se-vbt-ske` | `se2482` | kandidat | `ska` | `se-nbt` |
| Sorsele | `se-vbt-sor` | `se2422` | reserv |  | `se-nbt` |
| Storuman | `se-vbt-sto` | `se2421` | reserv |  | `se-jam`, `se-nbt` |
| Umeå | `se-vbt-ume` | `se2480` | reserv |  | `se-vnl` |
| Vilhelmina | `se-vbt-vil` | `se2462` | reserv |  | `se-vnl`, `se-jam` |
| Vindeln | `se-vbt-vin` | `se2404` | reserv |  | `se-vnl` |
| Vännäs | `se-vbt-van` | `se2460` | reserv |  | `se-vnl` |
| Åsele | `se-vbt-ase` | `se2463` | reserv |  | `se-vnl`, `se-jam` |

## Norrbottens län – `se-nbt`

Ersätter `se25`.

| Kommun | Region | Ersätter | Grund | Alternativ | Grannlän |
| --- | --- | --- | --- | --- | --- |
| Arjeplog | `se-nbt-arj` | `se2506` | reserv |  | `se-vbt` |
| Arvidsjaur | `se-nbt-arv` | `se2505` | reserv |  | `se-vbt` |
| Boden | `se-nbt-bod` | `se2582` | reserv |  | `se-vbt` |
| Gällivare | `se-nbt-gal` | `se2523` | reserv |  |  |
| Haparanda | `se-nbt-hap` | `se2583` | reserv |  |  |
| Jokkmokk | `se-nbt-jok` | `se2510` | reserv |  |  |
| Kalix | `se-nbt-kal` | `se2514` | reserv | `klx` |  |
| Kiruna | `se-nbt-kir` | `se2584` | reserv | `krn` |  |
| Luleå | `se-nbt-lul` | `se2580` | reserv | `lla` | `se-vbt` |
| Pajala | `se-nbt-paj` | `se2521` | reserv |  |  |
| Piteå | `se-nbt-pit` | `se2581` | reserv |  | `se-vbt` |
| Älvsbyn | `se-nbt-alv` | `se2560` | reserv |  | `se-vbt` |
| Överkalix | `se-nbt-okx` | `se2513` | krock | `okl` |  |
| Övertorneå | `se-nbt-ove` | `se2518` | reserv |  |  |
