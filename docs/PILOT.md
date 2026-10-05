# Pilotprotokoll

Kopiera protokollet och fyll i före försöket. Det ska visa om en bestämd ändring hjälper den
avsedda målgruppen och ge underlag för nästa beslut. Tomma resultat betyder **inte provat**.

## Bestäm försöket

| Uppgift | Fyll i |
| --- | --- |
| Område och målgrupp | Minst två kommuner och två län för första piloten; vilka orter, användare och tjänster ska fungera? |
| Ansvariga | Vem ändrar varje nod, samlar resultaten och beslutar om fortsättning eller återställning? |
| Testpunkter och vägar | Identifiera repeatrar, nödvändiga transitnoder och kända beroenden. Skilj på observerade länkar och antagna vägar. |
| Versioner | App, companion- och repeater-firmware, botklient samt tillämplig version av regionlistan. |
| Radio och konfiguration | Radioparametrar, tillåtna scopes, default, eventuella override och hoppgränser per nod. Spara före och efter. |
| Ändring | Precis vilka inställningar som ändras och varför. |
| Mätning | Testperioder, antal prov per fall, mottagare, observationsnoder och hur scope, paketmängd och airtime kontrolleras. |
| Krav före start | Minsta godtagbara leveransgrad per trafikfall, längsta godtagbara svarstid och högsta godtagbara belastning på berörda repeatrar. |
| Återställning | Tidigare värden, återställningskommandon, vem som kan utföra dem och hur återställd trafik kontrolleras. |

Sätt kraven lokalt **före** försöket. Ett högt genomsnitt får inte dölja att en ort eller tjänst
har slutat fungera. Kan ett viktigt krav inte mätas är den delen fortfarande oprövad.

## Jämför en ändring i taget

1. Kör baslinjen med befintlig konfiguration.
2. Genomför en ändring och upprepa samma trafikfall med jämförbar mängd trafik, meddelandelängd
   och testpunkter. Behåll radioparametrar och andra inställningar under jämförelsen.
3. Vid försämring eller oklara resultat, återställ och upprepa baslinjen. Anteckna ändrade
   radioförhållanden och annan trafik som kan förklara skillnaden.

Pröva namnbyte, botarnas scopeval, companionens default, nationell Public, repeaterns adverts
och begränsning av `*` som separata förändringar. Ett namnbyte minskar inte floodtrafiken i sig;
för att jämföra namnen ska gamla och nya namn tillåtas på samma avsedda noder. Bedöm namnens
nytta genom exempelvis felval och behov av hjälp när användare konfigurerar samma uppgift.

## Trafikfall

Använd unika meddelande-ID:n och anteckna scope samt riktning för varje prov. Vid prov av första
DM ska kontaktuppgifterna redan vara utbytta, men testkontaktens vägar rensade i båda ändar.
Rensa på nytt inför varje sådant prov, även när riktningen byts, och kontrollera att frågan
faktiskt skickas som flood. Behåll administratörens fungerande väg till repeatrarna.

| Fall | Kontrollera separat |
| --- | --- |
| Kanaltrafik utan scope och med gamla scopes | Befintliga användare och kanaler fungerar under förberedelse och migration. |
| Kanaltrafik med nya kommun-, läns- och nationella scopes | Leverans i båda riktningarna mellan avsedda testpunkter, även över nödvändig transit. Ett lyckat `se`-prov godkänner inte kommunscope. |
| Nytt DM inom och mellan områden | Mottagen fråga, ACK/vägretur och mottaget svar. Starta också ett nytt DM från andra änden. |
| DM med etablerad väg | Fortsatt leverans; redovisas separat från prov med rensade vägar. |
| Botens utskick och DM | Avsett scope på utskicket samt fråga, ACK/vägretur och svar för målgruppen. Testa DM under och efter lokalt utskick. |
| Adverts | Avsedda användare hittar noderna, inklusive från testpunkt där kontakten inte redan ligger sparad. |
| Omstart och återanslutning | Inställningar, utskick, upptäckt och nya DM fungerar fortfarande. |
| Återställning | Den tidigare konfigurationen och dess trafik fungerar igen. |

Kontrollera även vilka repeatrar som vidarebefordrar lokalt scoped trafik nära områdets kant.
Mottagning direkt över radio utanför området bevisar inte felaktig vidarebefordran: scope är
inte ett GPS-staket eller ett mottagningsfilter.

## Redovisa utfallet

| Trafikfall, riktning och mottagare | Sända unika meddelanden | Mottagna inom vald tidsgräns | Leveransgrad | Svarstid för DM | Krav uppfyllt? |
| --- | --- | --- | --- | --- | --- |
| Fyll i en rad per fall, riktning och mottagare | | | | | |

Leveransgrad är mottagna unika meddelanden inom tidsgränsen delat med sända unika meddelanden.
Räkna inte omsändningar eller dubbletter som nya leveranser. För DM redovisas dessutom andelen
frågor som får ACK och svar; en mottagen fråga ensam är inte ett lyckat tjänsteanrop.

Redovisa paketmängd och airtime för samma mätperioder på de repeatrar som bär provtrafiken,
särskilt gemensamma transitnoder. Ange om airtime är mätt eller beräknad och vilken metod som
använts. Ta med omsändningar och adverts där de ingår i mätningen; märk om annan trafik inte
kan särskiljas. En minskning på en nod kan bero på tappad trafik, så bedöm belastning och
leverans tillsammans.

## Beslut efter försöket

Ange vad som kan gå vidare, vad som återställs och vad som återstår att prova, med hänvisning
till resultaten. Beslut om namn, nationell Public och begränsning av `*` fattas var för sig.
Ett litet områdesprov visar lokal funktion och belastning; det bevisar inte kapacitet för
nationell Public. Innan det beslutet behövs även mätning på de gemensamma radiovägar som ska
bära den större trafikmängden. Om underlaget saknas är beslutet fortsatt öppet.

Ändra inte en inställning vars tidigare värde inte kan återställas med den planerade metoden.
I repeater-firmware 1.16 kan `get flood.max.unscoped` visa `255` (följer `flood.max`), medan
[`set flood.max.unscoped`](https://github.com/meshcore-dev/MeshCore/blob/repeater-v1.16.0/src/helpers/CommonCLI.cpp#L615)
bara accepterar 0–64. Ett försök att sätta tillbaka `255` återställer därför inte inställningen.
Verifiera en annan återställningsmetod före ett sådant prov, eller lämna inställningen oförändrad.
