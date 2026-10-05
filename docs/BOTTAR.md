# Scopes för bottar

Välj policy efter vilka botten ska betjäna. Ett lokalt kanalutskick och en DM-tjänst har olika
behov. Ändra först i fas 2, efter test med den botklient och companion-firmware som ska användas.

## Välj profil

| Botens uppgift | Kanalutskick | Companionens default scope |
| --- | --- | --- |
| Publicerar bara lokala meddelanden | Explicit kommun- eller länsscope som når målgruppen | Lokalt scope kan användas om även botens adverts ska begränsas. Ingen DM-tjänst utanför området utlovas. |
| Svarar på DM inom ett lokalt område | Explicit scope för kanalens målgrupp | Lokalt scope, om första DM, ACK/vägretur och svar fungerar för hela den avsedda målgruppen. |
| Svarar på DM över flera områden | Explicit lokalt scope för lokala utskick | Scope som stöds på vägarna åt båda håll, till exempel `se` om tjänsten ska fungera över länsgränser. |

Välj det minsta scope som faktiskt betjänar målgruppen. Antalet repeatrar i kommunen räcker
inte som grund för valet: var de står och vilka radiovägar som fungerar är också avgörande.
Ett nationellt default betyder att botens egna flood-adverts också får nationellt scope.

## Varför default påverkar DM

I companion-firmware 1.16 skickar ett första floodat DM en automatisk vägretur med ACK.
Den returtrafiken använder mottagarens aktuella scopeval: ett aktivt override, annars dess
default scope. Den kopierar inte automatiskt frågans scope.

En fråga med `se` kan därför nå en bot i Mullsjö, medan botens vägretur med `se-jkp-mul` stannar
vid en repeater som inte tillåter kommunscope. Botloggen kan visa en mottagen fråga trots att
användaren saknar ACK eller svar. En redan känd direktväg kan dölja felet.

Kodunderlag: [vägretur med ACK](https://github.com/meshcore-dev/MeshCore/blob/companion-v1.16.0/src/helpers/BaseChatMesh.cpp#L230)
och [companionens scopeval](https://github.com/meshcore-dev/MeshCore/blob/companion-v1.16.0/examples/companion_radio/MyMesh.cpp#L497).
Detta beskriver firmwarebeteende; botklientens faktiska scopehantering behöver också testas.

## Kontrollera botklienten

Inställningar gjorda i telefonappen räcker inte som bevis för vad ett separat botprogram skickar.
Kontrollera följande innan migration:

- Klienten skickar varje kanalutskick med avsett scope. En kanal utan explicit scope kan använda
  ett bredare default och ge större spridning än avsett.
- Tillfälliga scopeval återställs korrekt. I firmware 1.16 är override gemensamt för utgående
  floods och kvarstår tills det ändras; ett kvarlämnat lokalt override kan påverka DM-returer.
- Ett inkommande DM under eller direkt efter ett lokalt kanalutskick får fungerande ACK/vägretur
  och svar. Kontrollera detta även om klienten normalt återställer override efter utsändning.
- Efter återanslutning och omstart skickar klienten fortfarande rätt scopes.

Om klienten inte kan kombinera lokala utskick med fungerande DM-returer, behåll den tidigare
konfigurationen tills stödet är verifierat. Att sätta hela companionens default till kommunen
är ingen generell lösning för en bot som ska svara utanför kommunen.

Scope begränsar vidarebefordran, inte vilka förfrågningar botten får ta emot eller vilka användare
som får använda tjänsten. Sådana begränsningar behöver botprogrammet hantera separat.

## Prov före migration

Använd testkontakter med utbytta kontaktuppgifter men rensade DM-vägar i **båda** companionerna.
Radera inte administratörens enda fungerande väg till en repeater. Anteckna version av botklient,
companion-firmware, båda sidors default scope och klientens eventuella override.

| Prov | Kontrollera |
| --- | --- |
| Lokalt kanalutskick | Avsett scope, mottagning hos målgruppen och vidarebefordran på berörda repeatrar. |
| Nytt DM från insidan av området | Mottagen fråga, ACK/vägretur och botens svar som tre separata resultat. |
| Nytt DM från utsidan av området | Samma tre resultat för en tjänst som ska betjäna dessa användare. För en lokal tjänst dokumenteras begränsningen; scope är inte åtkomstkontroll. |
| Nytt DM under och efter kanalutskick | Lokalt scopeval för utskicket stör inte tjänstens DM-returer. |
| DM med etablerad väg | Svar fungerar även efter att vägen hittats; detta ersätter inte proven med rensade vägar. |
| Omstart och återanslutning | Utskick och nytt DM upprepas med rätt scopeval. |

Godkänn profilen först när alla trafikslag tjänsten lovar har verifierats. Återställ både
companionens inställningar och botklientens scopeval om leveransen försämras.
