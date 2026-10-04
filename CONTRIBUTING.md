# Bidra

Förslaget blir bara bra om folk som bor på orten säger vad orten faktiskt kallas. Alla koder i
[data/regioner.csv](data/regioner.csv) går att ändra med en pull request.

## Ändra en kod

1. Ändra raden för din kommun i `data/regioner.csv`.
2. Kör `python3 scripts/build.py`. Skriptet kontrollerar reglerna och skriver om `REGIONER.md`.
3. Skicka en pull request med båda filerna. Skriv i beskrivningen **varför** koden är bättre.

Har du inte Python går det bra att bara ändra CSV-filen och beskriva ändringen – någon annan kör skriptet.
Du kan också öppna ett issue i stället för en pull request.

## Regler för koderna

- Exakt tre tecken, bara `a`–`z`. Å och ä skrivs `a`, ö skrivs `o`.
- Koden måste vara unik **inom länet**. Samma kommunkod får finnas i olika län.
- Prioritetsordning:
  1. En förkortning som folk på orten redan använder (`gbg`, `jkp`, `vxo`).
  2. Annars de tre första bokstäverna i kommunnamnet.
- Krockar två kommuner i samma län behåller den större sin naturliga kod.
- Reglerna är till för att fylla luckor. Vet du vad orten kallas går det före dem.

## Kolumnen `grund`

| Värde | Betyder |
| --- | --- |
| `vedertagen` | Känd förkortning. Kräver belägg i pull requesten: lokalpress, föreningar, företag, skyltar. |
| `kandidat` | Förkortning med svagt belägg. Behöver bekräftas av folk på orten. |
| `krock` | Tre första bokstäverna krockade inom länet, så koden är ändrad. |
| `reserv` | Tre första bokstäverna. |

Vill du flytta en kod från `kandidat` till `vedertagen`, eller tillbaka till `reserv`: skriv att du bor
eller är aktiv på orten och vad ni faktiskt säger. Det väger tyngre än en webbsökning.

## Ändra ett grannlän

[data/grannlan.csv](data/grannlan.csv) har en rad per kommun och grannlän. Listan är framräknad
från avstånd på kartan, se *Grannlän* i [README.md](README.md#grannlän). Vet du att din kommun
har kontakt med ett län som saknas, eller saknar kontakt med ett som står där: ändra filen.

1. Lägg till eller ta bort raden i `data/grannlan.csv`. Sätt `via` till `lokal` på rader du lägger till.
2. Ett par ska gälla åt båda håll. Lägger du till Värmland för en kommun i Dalarna måste minst en
   kommun i Värmland ha Dalarna.
3. Kör `python3 scripts/build.py` och skicka en pull request med `data/grannlan.csv` och `REGIONER.md`.

| `via` | Betyder |
| --- | --- |
| `land` | Länets landyta ligger inom 40 km, fågelvägen. |
| `vatten` | Längre bort än 40 km, men inom 80 km över öppet vatten. |
| `omvand` | Tillagd för att paret ska gälla åt båda håll. |
| `lokal` | Tillagd av någon som känner till trakten. Skriv i pull requesten vad du vet. |

## Ändra själva förslaget

Texten i `README.md` går också att ändra med en pull request. Större ändringar (nivåer, utrullning,
namnformat) är bäst att ta som ett issue först, så att fler hinner tycka till.
