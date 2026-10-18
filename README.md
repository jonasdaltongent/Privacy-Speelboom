# Handleiding voor de leraar — Les 5: Wat mag je delen?

**Vak:** Toegepaste Informatica
**Doelgroep:** klas 3MWb — 2de graad Maatschappij en welzijn, dubbele finaliteit
**Lesduur:** 1 × 50 minuten: **10 minuten instructie + 40 minuten keuzewerktijd**
**Context:** De Speelboom, een fictieve buitenschoolse opvang (groep De Eekhoorns, 6 tot 9 jaar)
**Waar:** lokaal 18 (Windows 11)
**Lesdag:** maandag 26 oktober 2026, 9de lesuur (15.25–16.15)
**Kernleerplandoelen:** `BV2_04.04` (ethische, sociale en legale regels: privacy, AVG, portretrecht) en `BK2_02.07.04` (correct omgaan met privacy van anderen als voorloper op deontologisch handelen)
**Opdracht in Classroom:** *Les 5 — Wat mag je delen?*, deadline vrijdag 30 oktober 2026, 20.00 uur

<!-- Beginvragen (stap 1 van CONTEXT.md), beantwoord door Jonas op 18-10-2026:
     klas 3MWb · les 5 van het lessenplan (Wat mag je delen?) · gewoon in de klas in lokaal 18 op Windows 11
     op maandag 26 oktober 2026, 9de uur (10–15 min instructie met demo + 35–40 min keuzewerktijd) ·
     lesstart: ophalen uit les 4 (bv. waarom je in een groepsbericht geen andere kinderen bij naam noemt), maar zo
     geformuleerd dat ook wie les 4 (de afstandsles van ma 19-10) nog niet maakte meteen kan antwoorden ·
     werkdocument en werkvorm: alles in één werkdocument Privacyprotocol.docx (zonder zip of losse Drive-map):
     casussen beoordelen (foto's/sociale media/Speelboom-app, klas-groepschat), een ruw stageverslag anonimiseren
     en een eigen privacyprotocol met 5 concrete afspraken voor De Speelboom opstellen. -->

## 1. Inhoud van het pakket

```text
W09 - Les 05 - MW - Wat mag je delen/
├── index.html              de lespagina: startpagina in beelden · route · één stap · checklist (6 stappen, 18 taken)
├── presentatie.html        10 dia's voor het bord; dia 1 is de vaste startdia, dia 9 heeft kloktijden uit de planning
├── css/style.css           opmaak van de lespagina
├── css/slides.css          opmaak van de dia's
├── js/script.js, js/slides.js   interactie (Kijk na in stap 4, zelftest + codewoord KLUIS in stap 6, kloktijden)
├── assets/                 logo's De Speelboom en GO! Dalton Gent, lettertypes (OFL), mascotte, video/inleveren.mp4, stapjes/
├── werkdocument/
│   ├── Privacyprotocol.docx        het werkdocument dat de leerling INLEVERT
│   ├── maak_werkdocumenten.py      genereert Privacyprotocol.docx (python-docx)
│   ├── huisstijl.py, go-dalton-gent.png   de huisstijl van het werkdocument
│   └── maak_stapjes.py             maakt de beelden in assets/stapjes/ uit de pdf van Google Documenten
├── lesvoorbereiding.md     de lesvoorbereiding (28 punten + bronnenonderzoek)
├── dalton-lesfiche.html    de Dalton-lesfiche (instructie 10 + KWT 40): openen, Kopieer de fiche, plakken
├── lesdoelen.json          de doelen voor je jaaroverzicht
├── classroom.json          de opdracht voor de Classroom-koppeling
├── ai-bron.txt             de volledige tekst van de lespagina (zonder het codewoord)
└── README.md               deze handleiding
```

### 1b. Hoe de lespagina werkt

- **Startpagina**: *Wat heb je nodig?* in drie beelden in twee kolommen (de opdracht in Classroom, deze lespagina, je
  werkdocument *Privacyprotocol*), *Dit maak je vandaag* (het skelet van deel 4: de vijf onderdelen van het
  privacyprotocol), *Na deze les kan je*, en *Vast?* als genummerde rij (*1. Klik in de stap op Toon stapjes · 2. Je
  buur · 3. Je leraar*).
- **Handelingen met stapjes, start in *Kort*** (`data-modus-start="kort"`, zonder knop *Stap voor stap / Kort*, volgens
  de afspraak van 18-10-2026): de leerling ziet eerst de vette hoofdhandelingen en klikt op *Toon stapjes* waar hij een
  uitsnede uit het werkdocument met een rood kader wil zien.
- **Stap 4 (*Kijk na*)**: na het herschrijven van het ruwe stageverslag van Kobe kan de leerling met de knop **Kijk na**
  een geanonimiseerd voorbeeld openen en zijn eigen tekst op drie punten controleren.
- **Stap 5 (*Een beeld van het resultaat*)**: onder de handelingen staat het skelet van deel 4 (*Ziet het bij jou er zo
  uit?*), zodat de leerling ziet dat alle vijf de vakken met een wél- en níét-afspraak ingevuld moeten zijn zonder dat
  de tekst het antwoord verklapt.
- **Stap 6 (*Eerst de zelftest, dan inleveren*)**: *Wat moet je doen?* is vergrendeld achter drie meerkeuzevragen. Zijn
  ze alle drie juist, dan toont de groene balk het codewoord **KLUIS** (dat de leerling bovenaan deel 5 typt) en klapt
  *Wat moet je doen?* open, met onderaan het filmpje `assets/video/inleveren.mp4` (10 seconden).
- **Geen AI-hulp** (`data-ai-hulp="uit"` op `<body>`, sinds 18-10-2026).

## 2. Klaarzetten

### Stap 1 — Publiceren via GitHub Pages

Repository [`jonasdaltongent/Privacy-Speelboom`](https://github.com/jonasdaltongent/Privacy-Speelboom), Pages op branch `main`,
map `/ (root)`:
- **Lespagina:** <https://jonasdaltongent.github.io/Privacy-Speelboom/>
- **Presentatie:** <https://jonasdaltongent.github.io/Privacy-Speelboom/presentatie.html>

### Stap 2 — De opdracht in Classroom, met de koppeling

De opdracht staat als **concept** klaar in [3MWb - Informatica](https://classroom.google.com/c/MjUzNTk0NjYzMTJa) en is
**ingepland** voor publicatie op **maandag 26 oktober 2026 om 14.55 uur** (een half uur vóór het 9de lesuur van 15.25 uur).

| | Opdracht: **Les 5 — Wat mag je delen?** |
|---|---|
| **Onderwerp** | Module 1 — Organiseren en professioneel communiceren |
| **Bijlage 1** | de link naar de lespagina (`Lespagina · Les 5 · Wat mag je delen? · De Speelboom`) |
| **Bijlage 2** | `Privacyprotocol` (Google-document) — **Een kopie maken voor elke leerling** |
| **Punten** | 20 |
| **Deadline** | vrijdag 30 oktober 2026, 20.00 uur |

```bash
python3 "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/_tools/zet_opdracht_klaar.py" "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W09 - Les 05 - MW - Wat mag je delen" --proef
```

### Afvinklijst vóór de les

- [ ] De lespagina en presentatie staan online (HTTP 200).
- [ ] De opdracht staat als **concept** klaar in `3MWb - Informatica` en is ingepland voor ma 26-10 om 14.55 uur.
- [ ] Zet het wachtwoord van de klascomputers op het bord (staat nooit op de dia).
- [ ] Open `presentatie.html` op het bord op **dia 1 (*Zo start je*)** terwijl de leerlingen binnenkomen.
- [ ] Kopieer de Dalton-lesfiche uit `dalton-lesfiche.html` naar je planner.

### 2b. Nagelezen klikpaden

| Handeling | Klikpad / naam | Bron |
|---|---|---|
| De opdracht (leerling) | in het midden de bijlagen; rechts **Jouw werk** met de eigen kopie van `Privacyprotocol` en **Inleveren** | demoleerling3 (09-10 en 15-10-2026), `_afspraken/klikpaden.md` |
| Inleveren | rechts bij **Jouw werk** op **Inleveren** › in het venster **Je werk inleveren?** op **Inleveren** › status **Ingeleverd** (daarna **Ongedaan maken**) | demoleerling3 (15-10-2026), `_afspraken/klikpaden.md` |
| Computer vergrendelen | **Windows-toets + L** | [Microsoft](https://support.microsoft.com/nl-nl/windows/sneltoetsen-in-windows-dcc61a57-8ff0-cffe-9796-cb9706c75eec) (13-10-2026), `_afspraken/klikpaden.md` |

## 3. Verloop van de les en de eerste rondgang

### Instructie en demo (10 minuten, dia 1–7)

- **Dia 1 (0–1'):** *Zo start je.* Wacht tot de meesten de lespagina open hebben.
- **Dia 2 (1–4'):** *Weet je het nog?* Vingervraag (1, 2 of 3 vingers): waarom hoort *"Lina en Daan waren vandaag weer
  superdruk trouwens"* niet in een bericht aan **alle** ouders? → **B** (andere ouders hoeven niet te lezen hoe het met
  Lina en Daan ging). Ook wie de thuisles van 19-10 miste, kan dit meteen beredeneren.
- **Dia 3–4 (4–6'):** *Wat kan je straks?* en *Dit maak je vandaag* (het privacyprotocol met vijf onderdelen).
- **Dia 5 (6–8'):** *Demo 1 — Portretrecht: twee keer toestemming.* Lees de tabel met Nora, Ilyas en Finn samen en doe
  **rij a van deel 1** hardop voor (groepsfoto met Finn erop in de Speelboom-app → **Nee**, want de ouders van Finn
  gaven geen toestemming voor de Speelboom-app).
- **Dia 6 (8–9'):** *Demo 2 — Discretieplicht: wie moet het weten?* Intern in het team (mentor Lien, collega's) = **wel**;
  buitenstaanders (klas-groepschat, op de bus, thuis, andere ouders) = **niet**.
- **Dia 7 (9–10'):** *Controle · iedereen antwoordt.* Vingervraag: *De ouders van Nora gaven toestemming voor foto's in
  de Speelboom-app. Mag jij een leuke foto van Nora op je eigen Instagram of TikTok zetten?* → **B** (Nee, toestemming
  geldt per plek, en op eigen sociale media zet je nooit foto's uit de opvang). Onthoud wie A of C toont.

### Keuzewerktijd (40 minuten, dia 8–10)

- **Dia 8 (Samen · 3 minuten):** *Iedereen doet stap 1.* De leerlingen openen hun eigen kopie van `Privacyprotocol` en
  zoeken in het kader voor welk kind de ouders nergens toestemming voor gaven (Finn). Duim omhoog als het openstaat.
  Neem wie op dia 7 fout had even apart bij het begin van stap 2.
- **Dia 9 (Keuzewerktijd · 37 minuten):** *Zo werk je verder* met de kloktijden op het bord:
  - **Eerste rondgang (stap 2 en 3):** kijk of iedereen in de lichtblauwe vakken typt en bij *Waarom?* verwijst naar het
    kader (bv. bij 1c: Nora heeft *Nee* bij Facebook) of naar de discretieplicht (bij 2b: Lien is je mentor).
  - **Tweede rondgang (stap 4 en 5):** controleer bij deel 3b of leerlingen niet alleen *Ilyas Benali* schrappen, maar
    ook *14-03-2018*, *Veldstraat 12*, *pinda-allergie/ADHD* en *mama Samira*. Kijk bij deel 4 of ze per onderdeel een
    volledige afspraak schrijven (wat ze wél en níét doen).
- **Dia 10 (Laatste minuut):** Exitvraag over discretieplicht (De Speelboom) versus beroepsgeheim (woonzorgcentrum), en
  uitloggen of **Windows + L**.

## 4. Verbetersleutel

- **Codewoord** bovenaan deel 5: **KLUIS** (ontbreekt of fout = −2; tikfout zoals *KLIUS* telt als juist).
- **Deel 1 (4 punten — 1 punt per rij b tot e: 0,5 voor ja/nee + 0,5 voor de reden):**
  - **b:** **Ja** · Voor zowel Nora als Ilyas gaven de ouders toestemming voor de Speelboom-app, en je gebruikt de
    tablet van De Speelboom.
  - **c:** **Nee** · De ouders van Nora gaven alleen toestemming voor de Speelboom-app en het stageverslag, **niet**
    voor de openbare Facebookpagina (toestemming geldt per plek).
  - **d:** **Nee** · Je neemt als stagiair nooit foto's van kinderen met je **eigen gsm**, alleen met de tablet van De
    Speelboom (ook niet om ze daarna te wissen).
  - **e:** **Nee** · Op je **eigen sociale media** (TikTok) zet je nooit beelden uit de opvang, én Finn is herkenbaar
    door zijn naam op het knutselwerk (bovendien gaven zijn ouders nergens toestemming voor).
- **Deel 2 (4 punten — 1 punt per rij b tot e: 0,5 voor ja/nee + 0,5 voor de reden):**
  - **b:** **Ja** · Lien is je mentor in De Speelboom: **intern overleggen** met een begeleider die het moet weten om
    het kind te begeleiden, hoort bij je stage en mag onder de discretieplicht.
  - **c:** **Nee** · Ook zonder voornaam is het kind **herkenbaar** ("het zoontje van de bakker uit de Kerkstraat") en
    op de bus luisteren buitenstaanders mee (schending van de discretieplicht).
  - **d:** **Nee** · Aan een ouder geef je **nooit de naam van een ander kind** door; je bespreekt met de mama van Nora
    alleen hoe het met Nora gaat.
  - **e:** **Ja** · Je vertelt alleen over je **eigen leerervaring** op stage, zonder namen of herkenbare details over
    kinderen.
- **Deel 3a (2 punten — 0,5 punt per rij, vier van deze vijf):**
  1. *Ilyas Benali* → vervangen door *een jongen van 8 jaar* of een schuilnaam (*kind X*).
  2. *geboren op 14-03-2018* → weglaten of vervangen door *8 jaar*.
  3. *woont in de Veldstraat 12* → weglaten (adres is niet nodig).
  4. *allergisch is voor pinda's en ADHD heeft* → weglaten (gevoelige gezondheidsgegevens die niet nodig zijn voor het
     verhaal over de appel).
  5. *zijn mama Samira* → vervangen door *zijn mama* of *zijn ouder*.
- **Deel 3b (3 punten — 2 punten voor volledige anonimisering, 1 punt voor behoud van wat Kobe deed):**
  > *Op woensdag 18 november begeleidde ik om 15.00 uur het vieruurtje bij De Eekhoorns. Een jongen van 8 jaar wilde
  > geen appel eten. Ik sprak rustig met hem af dat hij eerst één stukje appel proeft en daarna een rijstwafel krijgt.
  > Dat werkte goed. Toen zijn mama om 16.45 uur kwam, vertelde ik dat het proeven goed gelukt was.*
- **Deel 4 (5,5 punten: 1 + 1 + 1 + 1 + 1,5):**
  - **1 · Foto's maken (1 pt):** ik fotografeer alleen met de tablet van De Speelboom (nooit met mijn eigen gsm) en kijk
    eerst in het toestemmingsoverzicht of het mag.
  - **2 · Foto's delen (1 pt):** ik deel een foto alleen op de plek waarvoor de ouders toestemming gaven (zoals de
    Speelboom-app) en zet nooit iets uit de opvang op mijn eigen sociale media.
  - **3 · Klas-groepschat en thuis (1 pt):** ik mag vertellen wat ik zelf bijleerde, maar ik noem nooit namen, foto's of
    herkenbare details over kinderen in een groepschat, op de bus of thuis.
  - **4 · Mijn stageverslag voor school (1 pt):** ik anonimiseer mijn verslag volledig (geen echte namen, adressen,
    geboortedatums of onnodige medische gegevens; alleen een foto als de ouders daarvoor toestemming gaven).
  - **5 · Bij twijfel of vraag van een ouder (1,5 pt):** ik geef aan een ouder nooit de naam van een ander kind, en bij
    twijfel deel ik niets en vraag ik raad aan mijn mentor Lien.
- **Deel 5, slotvraag (1,5 punt):**
  Nee: in De Speelboom (kinderopvang) geldt de **discretieplicht** (een werkafspraak om geen informatie met
  buitenstaanders te delen), maar in een woonzorgcentrum (zorg) geldt het strengere, wettelijke **beroepsgeheim** (wie
  dat schendt, is strafbaar volgens de wet).
- **Extra (niet verplicht):**
  Ja, ouders mogen hun toestemming voor een foto **altijd intrekken** (portretrecht en recht op wissing onder de AVG).
  De Speelboom moet de foto van de Facebookpagina verwijderen.

### Essentiële fouten — geef hier altijd feedback op

- Goedkeuren dat een stagiair foto's maakt met de **eigen gsm** of op **eigen sociale media** plaatst.
- Denken dat toestemming voor de Speelboom-app ook telt voor de **openbare Facebookpagina**.
- Aan een ouder de **naam van een ander kind** meedelen (deel 2d of deel 4.5).
- In het herschreven stageverslag (deel 3b) toch de naam (*Ilyas*), het adres (*Veldstraat*), de diagnose (*ADHD /
  pinda-allergie*) of de voornaam van de mama (*Samira*) laten staan.

## 5. Schermafbeeldingen

De beelden bij de stapjes (`assets/stapjes/`, 19 stuks) zijn uitsneden uit de pdf die Google Documenten van
`Privacyprotocol.docx` maakt, op ware grootte, met één rood kader (`#C5221F` met witte rand erbuiten), gegenereerd door
`werkdocument/maak_stapjes.py`. De opdracht in Classroom, de tabbladen van Chrome en het skelet van het privacyprotocol
zijn tekeningen in HTML en CSS.

## 6. Materiaal opnieuw genereren

```bash
cd "/Volumes/Littlecisboy/Google drive/Toegepaste Informatica/2026-2027/W09 - Les 05 - MW - Wat mag je delen/werkdocument" && python3 maak_werkdocumenten.py
```

Verandert het werkdocument, zet het dan via Drive om naar pdf en draai `python3 maak_stapjes.py <leeg.pdf>` om
`assets/stapjes/` bij te werken.

## 7. Jaaroverzicht

`lesdoelen.json` (klasgroep `3 MW`): `BV2_04.04` en `BK2_02.07.04` (kern) · `BK2_02.07`, `BK2_01.02`, `BK2_01.02.03`
(ondersteunend) · `BV2_04.03` (voorbereidend). De pre-push hook werkt `Leerplandoelen 2026-2027.xlsx` bij.

## 8. Wat nog moet blijken in de klas

- **Aansluiting op les 4 (afstandsles van ma 19-10):** hoeveel leerlingen van 3MWb maakten les 4 thuis op tijd, en werkt
  de lesstart op dia 2 vlot voor wie les 4 niet maakte?
- **Het toestemmingsoverzicht in het kader:** lezen de leerlingen de drie kolommen (Speelboom-app, Facebook,
  stageverslag) bij deel 1 zonder kolommen te verwisselen?
- **Deel 3 (anonimiseren):** vinden de leerlingen zelf dat ook *ADHD*, *allergisch voor pinda's*, *Veldstraat 12* en
  *mama Samira* weg moeten, of schrappen ze alleen de naam *Ilyas Benali*?
- **Deel 4 (vijf losse vakken voor het privacyprotocol):** helpt de opdeling in vijf genummerde rijen met richtvraag om
  concrete wél/níét-afspraken te krijgen in plaats van vage zinnen zoals *"Ik let op privacy"*?
- **De zelftest met het codewoord KLUIS en het filmpje Inleveren:** werkt het slot in lokaal 18 vlot en leveren alle
  leerlingen in zonder te vragen waar de knop zit?
