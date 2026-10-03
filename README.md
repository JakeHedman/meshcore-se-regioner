# Förslag: svenska MeshCore-regioner med namn folk kan

> **Förslag för diskussion – inte antaget.**
> Gäller Sverige · repeater-firmware 1.16+ rekommenderas · MeshCore-appen 1.43+

Regioner (scopes) hindrar lokalt prat från att flooda hela nätet. I dag heter de svenska regionerna
efter SCB:s sifferkoder, till exempel `se06` och `se0680`, som nästan ingen kan utantill. Det här
förslaget behåller samma nivåer men byter siffrorna mot korta namn som går att komma ihåg:
`se-jkp` för Jönköpings län och `se-jkp-mul` för Mullsjö.

Upplägget och utrullningen är en svensk anpassning av
[MeshCore Canadas förslag för Ontario och Québec](https://meshcore.ca/proposals/onqc-scopes/).
Nivåerna är de som [meshat.se](https://meshat.se/meshcore/regioner/) redan beskriver.

**Tycker du att din ort har fel kod?** Bra – det är därför det här ligger på GitHub.
Se [CONTRIBUTING.md](CONTRIBUTING.md) och skicka en pull request.

## Vad behöver jag göra?

| Du… | Vad du gör | När |
| --- | --- | --- |
| Använder MeshCore-appen med en companion | **Inget än.** Låt inställningarna vara. [Fas 2](#fas-2-companions) består av två inställningar. | Tidigast när fas 1 är klar |
| Äger en repeater | Inget förrän förslaget är antaget. Sedan [fas 1](#fas-1-repeatrar). | När förslaget är antaget |
| Kör en bot | Sätt den till din kommun, se [Bottar](#bottar). | I slutet av fas 1 |
| Vet vad din ort kallas | Kontrollera koden i [REGIONER.md](REGIONER.md) och föreslå en bättre. | Nu |

Resten av sidan förklarar hur allt hänger ihop. Du behöver inte förstå det för att följa stegen.

## Kortversionen

Det finns fyra nivåer. Varje repeater bär en kod från varje nivå: sin kommun, sitt län, `se` och `eu`.
När du skickar ett meddelande avgör scopet hur långt det färdas.

| Nivå | Exempel | Betyder |
| --- | --- | --- |
| Kommun | `se-jkp-mul` `se-vgr-gbg` `se-kro-vxo` | Ditt närområde. |
| Län | `se-jkp` `se-vgr` `se-kro` | Alla repeatrar i länet. |
| Sverige | `se` | Alla repeatrar i Sverige. |
| Europa | `eu` | Reserverad för senare. Bärs nu, används inte än. |

När alla faser är klara:

- **Repeatrar** bär sin kommun, sitt län, `se` och `eu`.
- **Bottar** använder sin kommun, så att de håller sig lokala.
- **Companions** har `se` som standard, så att direktmeddelanden når vem som helst.
- **Public** använder `se`, så att alla i Sverige kan prata.
- **Testkanaler** använder kommunen, så att tester håller sig lokala.
- **Meddelanden utan scope** fungerar fortfarande inom länet. Kantrepeatrar, de som länkar ihop två
  län, släpper inte igenom dem, så de floodar inte nästa län.

Companions kommer sist, i fas 2. Sätter du ett scope på din companion innan repeatrarna runt dig är
omställda når dina meddelanden **färre**, inte fler.

## Så är namnen uppbyggda

```
se - jkp - mul
│    │     └── kommun, tre bokstäver
│    └──────── län, tre bokstäver
└───────────── Sverige
```

- **Vedertagen förkortning först.** Göteborg är `gbg`, Jönköping `jkp`, Växjö `vxo`, Stockholm `sth`.
- **Annars de tre första bokstäverna.** Mullsjö är `mul`, Habo `hab`, Tibro `tib`.
- **Bara `a`–`z`.** Å och ä skrivs `a`, ö skrivs `o`. Inga stora bokstäver.
- **Länet är nyckeln.** En kommunkod behöver bara vara unik inom sitt län. Habo (`se-jkp-hab`) och
  Håbo (`se-upp-hab`) krockar därför inte.
- **Krockar inom ett län** löses genom att den större kommunen behåller sin naturliga kod.
  Sju kommuner i landet har fått en avvikande kod av det skälet.

Hela listan över alla 290 kommuner finns i [REGIONER.md](REGIONER.md). Källan är
[data/regioner.csv](data/regioner.csv).

### Vem koden kommer från

Koden bestäms där den används. En kommunkod angår kommunen, en länskod angår länet, och ingen av dem
behöver ett ja ovanifrån.

- **Vedertaget är lokalt.** Vad en ort kallas vet folk på orten. Listan här är ett utgångsläge, och
  den som bor där har sista ordet om sin egen kod.
- **Unik där den används, inte överallt.** En kommunkod behöver bara vara unik inom sitt län. Två
  län kan använda `hab` utan att något går sönder, och vad ett län i ett annat land kallar sina
  kommuner spelar ingen roll alls.
- **Lokal logik går före en nationell regel.** Reglerna ovan är till för att ge varje kommun en kod
  utan att någon behöver fråga. Säger orten något annat är det orten som stämmer, och regeln som
  fick fylla luckan.
- **Länskoden följer samma ordning.** Den angår de som delar länet. Ett län som vill ha en annan kod
  än den här listan föreslår ändrar den.

Det här är redan ungefär hur listan har vuxit fram: 12 koder är vedertagna och 257 är de tre första
bokstäverna, alltså en gissning i väntan på någon som vet bättre. Skillnaden är att gissningen inte
blir riktig förrän orten har sagt sitt.

### Länen

| Län | Region | Ersätter |
| --- | --- | --- |
| Stockholm | `se-sth` | `se01` |
| Uppsala | `se-upp` | `se03` |
| Södermanland | `se-sor` | `se04` |
| Östergötland | `se-ost` | `se05` |
| Jönköping | `se-jkp` | `se06` |
| Kronoberg | `se-kro` | `se07` |
| Kalmar | `se-kal` | `se08` |
| Gotland | `se-gtl` | `se09` |
| Blekinge | `se-blk` | `se10` |
| Skåne | `se-ska` | `se12` |
| Halland | `se-hal` | `se13` |
| Västra Götaland | `se-vgr` | `se14` |
| Värmland | `se-var` | `se17` |
| Örebro | `se-ore` | `se18` |
| Västmanland | `se-vml` | `se19` |
| Dalarna | `se-dal` | `se20` |
| Gävleborg | `se-gav` | `se21` |
| Västernorrland | `se-vnl` | `se22` |
| Jämtland | `se-jam` | `se23` |
| Västerbotten | `se-vbt` | `se24` |
| Norrbotten | `se-nbt` | `se25` |

## Ord som används här

- **Companion:** MeshCore-radion du parar med appen i telefonen eller datorn.
- **Repeater:** en fast radio, ofta på ett tak eller i en mast, som för meddelanden vidare.
- **Flood:** hur ett meddelande sprids när det inte finns någon känd väg: varje repeater som hör det
  skickar det vidare. Kanalmeddelanden floodar alltid, och det gör även det första direktmeddelandet
  till någon.
- **Hopp:** en repeater som skickar ett meddelande vidare.
- **DM:** ett direktmeddelande till en kontakt.
- **Advert:** en radio som annonserar sig själv så att andra hittar den.
- **Kantrepeater:** en repeater som regelbundet pratar med repeatrar i två olika län.

## Vad ett scope är

Ett scope är ett kort namn som sätts på ett meddelande, till exempel `se-jkp`. Repeatrar använder
det för att avgöra om meddelandet ska skickas vidare.

Ett scope är **inte kryptering och inget GPS-staket**. Vem som helst som kan namnet kan använda det,
och det har inget att göra med var du befinner dig. Det är bara en etikett som säger "repeatrar som
bär det här namnet, skicka vidare".

Appen gör om namnet till en liten kod och lägger den i meddelandets huvud. Varje repeater har en
lista över namn den skickar vidare, och jämför koden mot listan.

## Så bestämmer en repeater

En repeater i Mullsjö bär enligt förslaget den här listan: `*`, `se-jkp-mul`, `se-jkp`, `se`, `eu`.

| Meddelande | Scope | Vad repeatern gör |
| --- | --- | --- |
| Kanal för Mullsjö | `se-jkp-mul` | Skickar vidare |
| Kanal för Jönköpings län | `se-jkp` | Skickar vidare |
| DM till Luleå, skickat med companionens standard | `se` | Skickar vidare |
| Äldre app, inget scope | inget | Skickar vidare |
| Kanal för Habo | `se-jkp-hab` | Släpper |
| Kanal för Västra Götaland | `se-vgr` | Släpper |

- Namnet finns på listan: skicka vidare.
- Namnet finns inte på listan: släpp.
- Inget scope alls: räknas som `*`. Skickas vidare bara om `*` är tillåtet.
- För många hopp: släpps när det passerar `flood.max`, oavsett scope.

Repeatern hör fortfarande alla meddelanden. Scopet avgör bara om den skickar dem vidare.

Fyra saker som folk brukar gå bet på:

- **Stavningen måste vara exakt.** `se-jkp`, `SE-JKP` och `se06` är tre olika namn.
- **Bara floods kontrolleras.** När ett direktmeddelande har en känd väg går det raka vägen, och
  scopet spelar ingen roll.
- **Det finns inget arv.** Att bära `se-jkp` betyder inte att bära `se-jkp-mul`. Varje namn måste
  stå på listan för sig. Bindestrecken i namnet är till för människor, inte för repeatern.
- **En repeater utan regioner släpper alla meddelanden med scope.** Från start bär en repeater bara
  `*`. Scope fungerar först när repeatrarna längs vägen är inställda.

## Nivåerna

```
eu                      Europa. Reserverad. Bärs nu, används inte än.
└─ se                   Alla repeatrar i Sverige.
   ├─ se-jkp            Jönköpings län
   │  ├─ se-jkp-jkp     Jönköping
   │  ├─ se-jkp-mul     Mullsjö
   │  ├─ se-jkp-hab     Habo
   │  └─ …
   └─ se-vgr            Västra Götalands län
      ├─ se-vgr-gbg     Göteborg
      ├─ se-vgr-fkp     Falköping
      └─ …
```

Det en repeater i Mullsjö faktiskt lagrar är en platt lista:

```
*   se-jkp-mul   se-jkp   se   eu
```

Trädet ovan är till för människor, inte för repeatern.

### Varför `eu`?

Alla repeatrar bär `eu` redan nu, så att ett scope över landsgränser fungerar senare utan att någon
behöver ställa om sin repeater igen. Använd inte `eu` på din companion eller dina kanaler än.

### Varför inte flygplatskoder, som i Kanada?

Kanada valde flygplatskoder eftersom deras verktyg redan använde dem. I Sverige fungerar det sämre:

- De flesta av landets 290 kommuner har ingen flygplats.
- Flygplatskoderna är ofta inte det folk säger. Göteborg är `GOT` i flyget men Gbg för alla andra,
  och Jönköping är `JKG` fast alla skriver Jkpg.
- Svenska repeatrar behöver redan i dag kunna två kodsystem: SCB-siffror för regionen och en
  flygplatskod för MQTT-rapportering. Ett enda system som folk kan utantill är enklare än två som
  ingen kan.

### Varför inte SCB-koderna?

De är kompletta och entydiga, men i praktiken är det bara SCB som använder dem. `se0642` säger
ingenting, `se-jkp-mul` går att gissa. Ett namn som går att gissa blir oftare rätt stavat, och rätt
stavat är det enda som räknas.

## Utrullning

Gör det här i ordning. Varje fas börjar först när den förra är klar.

| Fas | Vem | Vad |
| --- | --- | --- |
| 1 | Repeatrar | Ägare lägger till de nya namnen **bredvid** de gamla. Vanliga repeatrar behåller `*`, kantrepeatrar släpper `*`. I slutet sätts bottar till sin kommun. Inget går sönder. |
| 2 | Companions | När repeatrarna runt dem är klara: standard och Public sätts till `se`, testkanaler till kommunen. |
| 3 | Städning | De gamla `seXX`- och `seXXXX`-namnen tas bort från repeatrarna. |
| 4 | Vid behov | Om meddelanden utan scope fortfarande stör inom ett län kan repeatrar köra `set flood.max.unscoped 3`. |

**Skillnad mot Kanada:** där rensas gamla regioner bort först. Här finns kanaler som redan använder
`se01`-namnen, så de gamla namnen ligger kvar på repeatrarna tills companions har bytt.

### Fas 1: Repeatrar

Fas 1 har tre mål:

1. **Få in de nya namnen på varje repeater**, så att var och en bär sin kommun, sitt län, `se` och `eu`.
2. **Begränsa trafik utan scope mellan län.** Kantrepeatrar släpper meddelanden utan scope.
3. **I slutet: sätt bottar till sin kommun**, när repeatrarna runt dem bär kommunkoden.

Companions ändrar ingenting i den här fasen.

Skriv kommandona ett i taget i repeaterns kommandorad: i MeshCore-appen öppnar du repeatern, loggar
in som admin och använder kommandorutan, eller så använder du USB-konsolen. Vänta på `OK` innan du
skickar nästa.

#### Steg 1: Kontrollera firmware och hitta dina koder

```
ver
```

Slå sedan upp din kommun i [REGIONER.md](REGIONER.md). Exemplen nedan gäller en repeater i Mullsjö:
kommun `se-jkp-mul`, län `se-jkp`.

Avgör också om din repeater är en vanlig repeater eller en **kantrepeater**. En kantrepeater pratar
regelbundet med repeatrar i ett annat län. Alla andra är vanliga repeatrar, även de som står nära en
länsgräns: om inget på andra sidan kopplar mot den är den en vanlig repeater. En enstaka länk som
setts några gånger, eller inte på flera veckor, räknas inte.

#### Steg 2: Se vad som redan finns

```
region
```

Finns `se`, `se06`, `se0642` eller liknande redan: låt dem vara. De tas bort i fas 3.

#### Steg 3: Lägg till de nya namnen

Vanlig repeater, firmware 1.16 eller nyare:

```
region def se-jkp-mul|* se-jkp|* se|* eu
region allowf *
region default se-jkp-mul
region save
```

Kantrepeater, firmware 1.16 eller nyare:

```
region def se-jkp-mul|* se-jkp|* se|* eu
region denyf *
region default se-jkp-mul
region save
```

Vad kommandona gör:

| Kommando | Vad det gör |
| --- | --- |
| `region def …` | Lägger till kommun, län, `se` och `eu`. Tecknen `\|*` hoppar tillbaka till toppen mellan varje namn, så att alla hamnar sida vid sida. Tar inte bort något som redan finns. |
| `region allowf *` | Vanliga repeatrar skickar vidare meddelanden utan scope. |
| `region denyf *` | Kantrepeatrar släpper meddelanden utan scope, så att de inte floodar nästa län. |
| `region default <kommun>` | Repeaterns egna adverts får kommunens scope, så att de håller sig lokala. Finns från firmware 1.15. |
| `region save` | Behåller inställningarna efter omstart. |

På äldre firmware finns inte `region def`. Då läggs varje namn till för sig med `region put <namn>`
följt av `region allowf <namn>`.

**Grannlän (valfritt):** en kantrepeater kan också bära grannlänets kod, till exempel `se-vgr`, så
att folk nära den kan delta i grannlänets kanaler. Alla andra når grannlänet genom `se`.

**Kantrepeater som enda repeater:** en kantrepeater skickar inte vidare närboende som saknar scope.
Undvik därför att göra den enda repeatern på en ort till kantrepeater.

#### Steg 4: Kontrollera resultatet

```
region
```

För Mullsjö ska listan innehålla:

```
*^ F
se-jkp-mul F
se-jkp F
se F
eu F
```

`F` betyder att repeatern skickar vidare det namnet. Gamla namn som `se06` ligger kvar tills fas 3.

#### Tillåt eller släpp, snabbreferens

| Kommando | Vad det gör |
| --- | --- |
| `region allowf <namn>` | Skicka vidare meddelanden med det namnet |
| `region denyf <namn>` | Släpp meddelanden med det namnet. Repeatern tar fortfarande emot dem själv. |
| `<namn>` | Kan vara `*` för meddelanden utan scope, eller en kod som `se-jkp` |
| `set flood.max.unscoped <hopp>` | En egen hoppgräns för meddelanden utan scope. `0` har samma effekt som `region denyf *`. |
| `region save` | Kör alltid efter `allowf` eller `denyf` |

#### Bottar

Det här görs i slutet av fas 1, när repeatrarna runt dig bär din kommunkod. På companionen som
botten använder: sätt **Default Region Scope** till kommunkoden, till exempel `se-jkp-mul`. Sätt
också alla kanaler som botten skriver i till kommunen.

Har kommunen bara någon enstaka repeater är länet (`se-jkp`) ett bättre val för botten.

### Fas 2: Companions

**Inte än.** Fas 1 måste vara klar först. En repeater utan de nya namnen släpper alla meddelanden
som har dem. Sätter du din standard till `se` innan repeatrarna på dina vägar bär det når dina
kanalmeddelanden och första DM bara närområdet.

När fas 2 öppnar är det här allt som behövs. Det tar ungefär fem minuter i appen.

#### Steg 1: Sätt ditt standard-scope

Öppna **Settings** i MeshCore-appen. Under **Network Settings**, tryck på **Default Region Scope**,
lägg till `se` och välj det.

#### Steg 2: Sätt scope på varje kanal

Öppna kanalen, tryck på **⋮** uppe till höger, välj **Set Region Scope** och välj enligt tabellen:

| Kanal | Scope | Varför |
| --- | --- | --- |
| Public | `se` | Alla i Sverige kan prata |
| Testkanaler, som `#test` | Din kommun, till exempel `se-jkp-mul` | Tester håller sig lokala |
| Bottkanaler | Din kommun | Bottsvar håller sig lokala |
| Egna kanaler | Kommun, län eller `se` | Välj hur långt den ska nå |

Meddelanden med scope är lite kortare. MeshCore Canada såg i sina tester att gränsen på Public sjönk
från 137 till 127 tecken när kanalen fick ett scope.

#### Varför är companionens standard `se`?

Du kan inte välja scope för ett enskilt direktmeddelande. När ett DM saknar känd väg floodar det med
ditt **standard-scope**. Svaret som talar om vägen för din companion kommer tillbaka med din kontakts
standard-scope.

| Din standard | Vad som händer med ett DM från Mullsjö till Göteborg |
| --- | --- |
| `se-jkp-mul` | Kommer aldrig fram. Repeatrarna utanför Mullsjö bär inte `se-jkp-mul`, så meddelandet stannar vid kommungränsen. Även om det kom fram skulle svaret använda `se-vgr-gbg` och stanna på vägen tillbaka. |
| `se` | Kommer fram. Alla repeatrar bär `se`, åt båda håll. När vägen är känd går senare DM raka vägen och scopet spelar ingen roll. |

Haken: en kanal utan eget scope använder också din standard, `se`, och når då hela Sverige. Det är
vad vi vill för Public, men inte för testkanaler och bottar. Därför sätts de till kommunen i steg 2.

### Fas 3: Städning

När companions har bytt tas de gamla namnen bort från repeatrarna med `region remove <namn>`, ett i
taget med det mest indragna först, och sedan `region save`:

```
region remove se0642
region remove se06
region save
region
```

Svarar ett kommando `Err - not empty` ligger ett annat namn fortfarande under det. Ta bort det
först. `Err - not found` betyder att namnet redan är borta.

### Fas 4: Bara vid behov

Om meddelanden utan scope fortfarande stör inom ett län efter fas 2 kan repeatrar köra
`set flood.max.unscoped 3` och sedan `region save`. Meddelanden utan scope stannar då efter tre
hopp. Meddelanden med scope når fortfarande `flood.max`.

## Vem hör vad

Exemplet är länken mellan Jönköpings län och Västra Götaland, genom en kantrepeater i Mullsjö som
också bär grannlänets kod `se-vgr`.

| Meddelande | Repeatrar i Jönköpings län | Kantrepeatern i Mullsjö | Repeatrar i Västra Götaland | Vem får det |
| --- | --- | --- | --- | --- |
| Ny användare i Jönköping, inget scope | Skickar vidare | Släpper | Nås aldrig | Hela Jönköpings län |
| Ny användare i Falköping, inget scope | Nås aldrig | Släpper | Skickar vidare | Hela Västra Götaland |
| Länskanal, `se-jkp` | Skickar vidare | Skickar vidare | Släpper | Jönköpings län |
| Länskanal, `se-vgr` | Släpper | Skickar vidare | Skickar vidare | Västra Götaland, plus folk nära Mullsjö |
| Bot i Jönköping, `se-jkp-jkp` | Bara de i Jönköpings kommun | Släpper | Släpper | Jönköpings kommun |
| DM med companionens standard, `se` | Skickar vidare | Skickar vidare | Skickar vidare | Hela Sverige |

En ny användare som inte har satt något scope når alltså fortfarande hela sitt län. Meddelandena
tar sig bara inte över till nästa län.

## Bra att veta

- **Meddelanden med scope är ungefär tio tecken kortare.**
- **Repeaterns adverts stannar i kommunen.** Användare i Göteborg ser inte repeatrar i Mullsjö genom
  flood-adverts.
- **Hoppgränsen gäller `se` också.** Är den verkliga vägen genom landet längre än `flood.max`
  stannar meddelandet på vägen.
- **Versioner:** `region def` kräver repeater-firmware 1.16 eller nyare. Standard-scope i appen
  kräver MeshCore 1.43 eller nyare. Uppgifterna kommer från MeshCore Canadas förslag.
- **`offgrid`** från meshat.se påverkas inte. Den regionen handlar om strömförsörjning, inte om
  geografi, och kan bäras bredvid de andra.

## Öppna frågor

Det här är inte avgjort, och synpunkter är välkomna som issues eller pull requests.

1. **Koderna.** 12 kommunkoder är vedertagna förkortningar, 14 är kandidater med svagt belägg och
   257 är de tre första bokstäverna. Kandidaterna och länskoderna behöver bekräftas av folk på
   respektive ort. Se [CONTRIBUTING.md](CONTRIBUTING.md).
2. **Kommandona är inte provkörda.** De följer MeshCore Canadas och meshat.se:s dokumentation men
   har inte testats på en repeater med de nya namnen, och inte ihop med befintliga `seXX`-namn.
3. **Var går kanten?** Förslaget lägger kantrepeatrarna vid länsgränserna. I stora län som Västra
   Götaland kan det vara för grovt, och i tätbebyggda områden som korsar en länsgräns för fint.
4. **Är kommun rätt lägsta nivå överallt?** I Stockholm är det troligen länet som är det verkliga
   närområdet. Kommunkoden finns för alla, men behöver inte användas överallt.
5. **MQTT-koderna.** meshat.se använder flygplatskoder per län för MQTT. Kan länskoderna här ersätta
   dem, så att det bara finns ett kodsystem?
6. **`europe`.** meshat.se har både `eu` och `europe`. Förslaget använder bara `eu`.
7. **Tidplan.** Inga datum är satta.

## Nästa steg

- Enas om listan över läns- och kommunkoder.
- Provköra kommandona på riktiga repeatrar.
- Ett verktyg där man väljer kommun och får färdiga kommandon.
- Bestämma var faserna annonseras.

## Tack

Texten bygger på [MeshCore Canadas ON/QC-förslag](https://meshcore.ca/proposals/onqc-scopes/)
([källa](https://github.com/MeshCore-ca/MeshCore-Canada), MIT-licens) och på
[meshat.se:s regionguide](https://meshat.se/meshcore/regioner/). Kommunlistan kommer från SCB.
