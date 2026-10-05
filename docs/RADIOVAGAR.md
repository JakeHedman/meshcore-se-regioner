# Sammanhängande radiovägar för scopes

Kommun- och länskoderna anger målgruppen. De säger inte vilka repeatrar som behövs för att
nå den. Grundkonfigurationen med egen kommun och eget län måste därför kompletteras där
nödvändiga radiovägar passerar andra områden.

## Ett scope kan behöva transit

Ett förenklat exempel, inte en uppmätt svensk radioväg:

```text
Kommun A                    Kommun B                    Kommun A
Repeater 1 ─────────────── Repeater 2 ──────────────── Repeater 3
se-lan-aaa                 se-lan-bbb                  se-lan-aaa
```

Om detta är den enda radiovägen mellan ändpunkterna kan ett kanalmeddelande med `se-lan-aaa`
inte nå från 1 till 3 när repeater 2 saknar scopet. Alla tre kan vara uppdaterade och korrekt
inställda enligt sina egna kommuner. Att de också tillåter länsscope eller `se` hjälper inte
paketet med kommunscope: ingen repeater byter automatiskt dess scope.

Om ägarna kommer överens kan repeater 2 även tillåta `se-lan-aaa` för transit mellan delarna
av A. Trafiken kan då också höras av användare nära repeater 2. Ett scope blir ingen exakt
geografisk gräns. Samma problem och lösning kan förekomma för ett län vars radioväg passerar
ett annat län.

Om transit inte går att ordna, pröva ett större gemensamt scope som faktiskt fungerar för
kanalens målgrupp. Samordna kanalens scopeval med användarna och mät den större spridningen.
Att välja ett större scope hjälper bara om radiovägen tillåter det och ryms inom hoppgränsen.

## Kom överens om minsta nödvändiga utökning

Gör detta före migration av berörda kanaler:

1. Ange vilka orter eller användargrupper som ska kunna nå varandra med scopet. Skilj på
   avsedd täckning och vad som redan har testats.
2. Identifiera radiovägarna och de repeatrar utanför området som behövs. En hörbar granne
   eller ett lyckat prov med `se` bevisar inte att det lokala scopet fungerar.
3. Be berörda repeaterägare komma överens om extra scopes på just dessa noder. Tillåt inte
   automatiskt alla grannkommuners eller grannläns scopes utifrån avståndslistan.
4. Dokumentera nod, extra scope, syfte, ansvarig ägare och datum för senaste prov. Behåll
   befintliga namn, föräldrar och flaggor; ett tillägg är inget skäl att ändra `*` eller default.
5. Testa det avsedda scopet i båda riktningarna och kontrollera spridning och belastning kring
   transitnoderna. Upprepa efter omstart och när viktiga noder eller länkar ändras.

En enkel lokal förteckning räcker; det krävs ingen nationell databas över repeatrar.
Konfigurera bara namn som saknas. `region put <namn> *` tillåter flood i firmware 1.16 men kan
också flytta ett befintligt namn. Granska därför först med `region`, spara med `region save`
och kontrollera efter omstart. Utgå från den befintliga konfigurationen vid återställning.

## Vad proven behöver skilja på

| Prov | Vad det visar |
| --- | --- |
| Kanalmeddelande med exakt kommun- eller länsscope, åt båda håll | Den valda trafikens vägar fungerar mellan testpunkterna. |
| Samma prov med nationellt scope | En jämförelse; det godkänner inte de lokala scopena. |
| Nytt DM med rensade vägar åt båda håll | Fråga, ACK/vägretur och svar fungerar med respektive companions scopeval. Ett tidigare fungerande DM räcker inte. |
| Trafik nära transitnod och områdets kant | Extra scopes ger den avsedda förbindelsen och deras större spridning är acceptabel. |
| Bortfall av en viktig transitnod, om det kan provas utan att störa nätet | Om reservvägen också stöder scopet. Saknas reservväg ska beroendet vara känt. |

Nåbarhet är riktad: A till B bevisar inte B till A. Radioförhållanden ändras också över tid.
Redovisa vilka vägar som provats och kända beroenden, inte en garanti för hela kommunen eller länet.

## Grannlänslistans roll

`data/grannlan.csv` föreslår möjliga grannlän enligt en avståndsmodell. Den visar varken
fungerande länkar, vilka noder som behövs för transit eller dubbelriktad radiokontakt.
Använd den som underlag för undersökning, inte som automatisk repeaterkonfiguration.

Beteendet är kontrollerat mot [scopekontrollen](https://github.com/meshcore-dev/MeshCore/blob/repeater-v1.16.0/src/helpers/RegionMap.cpp#L188)
och [vidarebefordring och hoppgränser](https://github.com/meshcore-dev/MeshCore/blob/repeater-v1.16.0/examples/simple_repeater/MyMesh.cpp#L429)
i repeater-firmware 1.16. Radioproven ovan återstår att genomföra för varje berört område.
