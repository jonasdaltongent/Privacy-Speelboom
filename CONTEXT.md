# _sjablonen/lespakket — de basis van een nieuwe les

Een nieuwe les begint als **kopie van deze map**, nooit met een lege map. Welke bestanden een lesmap
heeft en waarvoor: `_afspraken/lespakket.md`.

## Een nieuwe les maken

1. Kopieer deze map naar `2026-2027/W<week> - Les <nr> - <klas> - <titel>/` (zonder dit bestand).
2. Neem uit de **vorige les van dezelfde klas** (zie `_index/lessen.md`) over: `index.html`,
   `presentatie.html`, `dalton-lesfiche.html`, de logo's van de context (`assets/<context>-logo.svg`,
   `assets/<context>-icon.svg`) en `werkdocument/maak_werkdocumenten.py`. Vervang daarna de inhoud.
   `werkdocument/huisstijl.py` en `go-dalton-gent.png` komen uit dit sjabloon (de kopie hierboven).
3. Pas de lesgegevens aan:
   - `index.html`: het tabblad-icoon `assets/logos/lespagina-icon.png` (de bever, niet het icoon van de context); `<title>Lespagina · Les <nr> · <titel> · <context></title>` (zo heet de link in de
     opdracht en het tabblad); `<body data-storage="<lesid>_v1_" data-laatste-stap="<N>" data-ai-hulp="uit" data-modus-start="kort">` (laat `uit`: geen AI-hulp meer sinds 18-10-2026, `_afspraken/ai-hulp.md`; `kort`: de lespagina begint in *Kort*, sinds 18-10-2026 — een vorige les heeft vaak nog `"stap"`, en nog de knop `<div class="modus">`: weg ermee);
     voor een Chromebook-les
     `<meta name="toestel" content="chromebook">` (`_afspraken/toestel.md`);
   - `js/slides.js`: de sleutel `dia_LESID`;
   - de kopregel bovenaan `css/*.css` en `js/*.js`;
   - `lesdoelen.json`, `classroom.json`, `README.md`, `lesvoorbereiding.md` (alles tussen `< >`).
4. `git init`, dan de hook: `cp ../../_sjablonen/pre-push .git/hooks/pre-push` en
   `chmod +x .git/hooks/pre-push`.
5. Controle: `python3 _tools/controleer_les.py "2026-2027/<lesmap>"` (`_afspraken/controle.md`).
   Daarna meteen publiceren: GitHub, en Classroom als concept (`_afspraken/publiceren.md`).

Wat hier staat (css, js, lettertypes, Dalton-logo, mascotte, `.gitignore`) komt uit les 06 ORLO (08-10-2026),
de nieuwste versie: met `.btn-dl`, `.clip` en de gecentreerde dia's. Sinds 09-10-2026 (les 3 MW) ook:
de startpagina *Wat heb je nodig?* (`.nodig`, `.mock-…`, `.vast`), de AI-hulp (`.ai-hulp`, verborgen
tot `data-ai-hulp="aan"`), het e-mailvenster (`.mail`, `.ccb`, `.bouwplan`) en de vaste startdia
(`.startroute` in `css/slides.css`). Neem de startpagina en dia 1 over uit les 3 MW of les 07–08 ORLO
(`_afspraken/lespagina.md`, `_afspraken/presentatie.md`). Verbeter je iets in die bestanden in een les,
zet het dan ook hier.

Sinds 10-10-2026 ook de mascotte Dalton de bever: `assets/mascotte/` met de `.webp`'s (de bronbeelden en de
prompts staan in `_sjablonen/mascotte/`), en in de css `.met-mascotte`, `.mascotte-kop`, `.mascotte-ico`,
`.mascotte-klaar` en `.slide .mascotte`. Waar de mascotte komt: `_afspraken/vormgeving-en-techniek.md`.

Sinds 11-10-2026 ook de logo's in `assets/logos/` (`classroom.svg`, `docs.svg`, `lespagina.webp`, `lespagina-icon.png` voor het tabblad, `drive.svg`) en `.logo`
in beide css-bestanden. Waar ze komen: `_afspraken/vormgeving-en-techniek.md`.

Sinds 12-10-2026 ook `werkdocument/huisstijl.py` met `go-dalton-gent.png`: de huisstijl van het werkdocument
(logo, puntenvak /20, vakken waarin de leerling typt, A4, Calibri en Montserrat), met `mailvenster` (MW les 3)
en `appvenster` (een bericht in een ouderapp, MW les 4). Waarom en hoe:
`_afspraken/werkdocument-en-bronbestanden.md`, § *Het werkdocument*. Voorbeeld: MW les 3.

Sinds 13-10-2026 ook het **infokader** (`.info`, uit MW les 4: leesmateriaal bij een vraag) en het blok
*Startpagina groter* (grotere beelden en logo's; drie of vier beelden in twee kolommen) in `css/style.css`.
Waarom: `_afspraken/lespagina.md` (*Groot genoeg*, *Bijgestuurd in de praktijk*). Voorbeelden: ORLO les 07 en 09.

Sinds 15-10-2026 ook `assets/video/inleveren.mp4` en `.jpg`: het filmpje *Inleveren* voor de laatste stap van elke les
(`_afspraken/filmpjes-en-schermafbeeldingen.md`). En op de startpagina *Dit maak je vandaag* (`_afspraken/lespagina.md`,
*Een beeld van het resultaat*): nog geen opmaak in dit sjabloon; de eerste les die het bouwt, zet ze hier.

Sinds 18-10-2026 ook de **handelingen met stapjes** (Jonas: "Pas het sjabloon aan. Dat is heel belangrijk."), uit
MW les 03 en ORLO les 07–11: in `css/style.css` het blok *Handelingen met stapjes* (`.todo-head`, `ol.doe`,
`details.stapjes`, `ol.klein`, `.mini-mock`, `.wijs`, `.doe > li > .sub`), in `js/script.js` § 3b (met `data-dicht`).
De lespagina begint in **Kort** (alles dicht), ook zonder `data-modus-start`, en heeft **geen knop *Stap voor stap /
Kort*** meer (Jonas: "Doe maar voor iedereen"): haal `<div class="modus">` weg als je `index.html` van een oudere les
overneemt; zonder opmaak voor `.modus` meldt `controleer_les.py` hem. Niet hier: de tekeningen van Drive en de
Verkenner (`.teken-ui`, `.teken-delen`, ORLO les 07–11) en wat maar bij één les hoort. Waarom en hoe:
`_afspraken/lespagina.md` (*Handelingen met stapjes*).
