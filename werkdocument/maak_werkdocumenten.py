#!/usr/bin/env python3
"""
maak_werkdocumenten.py
Genereert het werkdocument voor les 5 "Wat mag je delen?" (De Speelboom, klas 3MWb):

  Privacyprotocol.docx    het werkdocument dat de leerling INLEVERT (wordt in Classroom een Google-document)

Gebruik:  python3 maak_werkdocumenten.py     (vereist python-docx; huisstijl.py en go-dalton-gent.png
          staan ernaast)

Waarom geen zip en geen losse bestanden: per les gebruiken de leerlingen één werkplek naast Classroom en de
lespagina (_afspraken/didactiek.md). Alle casussen, het anonimiseren van het stageverslag van Kobe en het
eigen privacyprotocol voor De Speelboom staan samen in dit werkdocument. Het ruwe verslag van Kobe en de
uitleg over portretrecht en discretieplicht staan op de lespagina.

LET OP bij aanpassen:
 - Deel 1, rij a en deel 2, rij a zijn al ingevuld (de demo uit de instructie). Laat ze ingevuld.
 - De gegevens uit het kader (Nora, Ilyas, Finn en de drie vaste afspraken) staan ook op de lespagina, op
   dia 5 en in lesvoorbereiding.md § 4 en § 14. Verander je ze, doe het overal.
 - De punten in deel 5 komen overeen met lesvoorbereiding.md § 22. Verander je ze, doe het op beide plaatsen.
"""
import os
from huisstijl import *

HERE = os.path.dirname(os.path.abspath(__file__))


def privacyprotocol():
    doc = nieuw_document()
    kopblok(doc, "PRIVACYPROTOCOL", punten=20)

    kader(doc, "Toestemming voor foto's in De Eekhoorns", [
        ("Jouw rol:", "stagiair in groep De Eekhoorns (6 tot 9 jaar), mentor Lien Verhoeven. De Speelboom stuurt de ouders berichtjes en foto's via een eigen app: de Speelboom-app (alleen voor ouders van De Eekhoorns), en heeft een openbare Facebookpagina."),
        ("Nora Peeters (7 jaar):", "Speelboom-app: JA  ·  openbare Facebookpagina: NEE  ·  stageverslag voor school: JA"),
        ("Ilyas Benali (8 jaar):", "Speelboom-app: JA  ·  openbare Facebookpagina: JA  ·  stageverslag voor school: NEE"),
        ("Finn Jacobs (6 jaar):", "Speelboom-app: NEE  ·  openbare Facebookpagina: NEE  ·  stageverslag voor school: NEE"),
        ("Drie vaste afspraken:", "1) Ouders geven op papier toestemming per plek.  2) Foto's maak je alleen met de tablet van De Speelboom, nooit met je eigen gsm.  3) Op je eigen sociale media (Instagram, TikTok, Snapchat, BeReal) komt nooit een foto uit de opvang."),
    ])

    # ---- Bladzijde 1: Deel 1 (past volledig op bladzijde 1 samen met het kader)
    deel(doc, 1, "Welke foto mag waar?")
    tabel(doc, ["Situatie", "Mag dit? (ja of nee)", "Waarom? Geef één reden."], [
        ("a.  Je neemt met de tablet een foto van Nora, Ilyas en Finn in het speelbos voor in de Speelboom-app.",
         "Nee", "De ouders van Finn gaven geen toestemming voor de Speelboom-app."),
        ("b.  Je neemt met de tablet van De Speelboom een foto van Nora en Ilyas in een kamp. Je zet ze in de Speelboom-app.", "", ""),
        ("c.  De foto van Nora en Ilyas in het kamp is heel mooi. Je zet ze ook op de openbare Facebookpagina van De Speelboom.", "", ""),
        ("d.  De tablet ligt binnen. Je neemt snel met je eigen gsm een foto van Ilyas voor de Speelboom-app en wist ze daarna.", "", ""),
        ("e.  Je maakt een selfie voor je eigen TikTok. Op de achtergrond zit Finn: zijn gezicht is vaag, maar zijn naam staat groot op zijn knutselwerk.", "", ""),
    ], [8.2, 2.2, BREEDTE - 8.2 - 2.2], invul=(1, 2), rijhoogte=1.15, voorbeeld_rij=1)

    # ---- Bladzijde 2: Deel 2 en Deel 3 samen op één bladzijde
    deel(doc, 2, "Wat mag je vertellen of sturen?", nieuwe_pagina=True)
    tabel(doc, ["Situatie", "Mag dit? (ja of nee)", "Waarom? Geef één reden."], [
        ("a.  In de WhatsApp-groepschat van je klas stuurt Kobe: “Zware dag! Ilyas Benali moest om 14 uur zijn pilletje Rilatine nemen en gooide zijn beker om 😂”",
         "Nee", "De naam en medicatie van een kind zijn gevoelige gegevens; die deel je nooit in een groepschat."),
        ("b.  In de personeelskamer vertel je aan je mentor Lien dat Finn vandaag twee keer wegliep naar de gang, en vraag je hoe je daar morgen op reageert.", "", ""),
        ("c.  Op de bus vertel je aan een vriendin over “het zoontje van de bakker uit de Kerkstraat” in De Eekhoorns dat straf kreeg. Je noemt zijn voornaam niet.", "", ""),
        ("d.  De mama van Nora vraagt bij het afhalen: “Wie heeft mijn dochter vanmiddag geduwd? Was het weer Finn?” Je zegt: “Ja, het was Finn.”", "", ""),
        ("e.  In de WhatsApp-groepschat van je klas schrijf je: “Vandaag voor het eerst zelf een kringspel geleid bij de 6- tot 9-jarigen. Het lukte goed!”", "", ""),
    ], [8.2, 2.2, BREEDTE - 8.2 - 2.2], invul=(1, 2), rijhoogte=1.1, voorbeeld_rij=1)

    deel(doc, 3, "Het stageverslag van Kobe anonimiseren")
    vraag(doc, "a.  Welke vier persoonsgegevens of herkenbare details in het verslag van Kobe (stap 4 op de lespagina) moeten weg of anders?")
    tabel(doc, ["", "Staat in het verslag van Kobe", "Vervang ik door / laat ik weg"], [
        ("1", "", ""),
        ("2", "", ""),
        ("3", "", ""),
        ("4", "", ""),
    ], [0.8, 7.6, BREEDTE - 0.8 - 7.6], invul=(1, 2), rijhoogte=0.85)
    vraag(doc, "b.  Schrijf het verslag van Kobe opnieuw, zodat niemand nog kan raden over welk kind het gaat, maar je leraar wél leest wat Kobe deed.")
    antwoordvak(doc, 2.0)

    # ---- Bladzijde 3: Deel 4 en Extra
    deel(doc, 4, "Mijn privacyprotocol voor De Speelboom", nieuwe_pagina=True)
    tekst(doc, "Schrijf bij elk onderdeel jouw afspraak voor je stage in De Speelboom (één of twee volledige zinnen: wat doe je wél en wat doe je níét?).", na=4)
    tabel(doc, ["Onderdeel", "Mijn afspraak voor stage in De Speelboom"], [
        ("1 · Foto's maken\n(met welk toestel, en wat kijk je eerst na?)", ""),
        ("2 · Foto's delen\n(waar mag een foto wel, en waar nooit?)", ""),
        ("3 · Klas-groepschat en thuis\n(wat vertel je wel en niet over je stagedag?)", ""),
        ("4 · Mijn stageverslag voor school\n(hoe schrijf je over een kind in een verslag?)", ""),
        ("5 · Bij twijfel of vraag van een ouder\n(wat zeg je als een ouder naar een ander kind vraagt, en aan wie vraag je hulp?)", ""),
    ], [5.8, BREEDTE - 5.8], invul=(1,), rijhoogte=1.35, vet=(0,))

    # ---- Bladzijde 4: Deel 5 en Extra
    deel(doc, 5, "Nalezen", nieuwe_pagina=True)
    vraag(doc, "Het codewoord van de zelftest (stap 6 op de lespagina):")
    antwoordvak(doc, 0.9)
    controletabel(doc, [
        ("Deel 1: bij situatie b tot e staat *ja* of *nee*, met een juiste reden uit het kader of de regels.", 4),
        ("Deel 2: bij situatie b tot e staat *ja* of *nee*, met een juiste reden over discretieplicht of persoonsgegevens.", 4),
        ("Deel 3a: ik vond vier persoonsgegevens of herkenbare details in het verslag van Kobe en schreef erbij hoe ik ze aanpas.", 2),
        ("Deel 3b: het verslag van Kobe is volledig geanonimiseerd (geen naam, geboortedatum, adres, diagnose of naam van de mama), maar zegt nog wat Kobe deed.", 3),
        ("Deel 4, afspraak 1 en 2: ik schreef met welk toestel ik fotografeer, dat ik de toestemming nakijk en waar foto's wel en nooit mogen.", 2),
        ("Deel 4, afspraak 3 en 4: ik schreef wat wel en niet in een groepschat of thuis mag, en hoe ik mijn stageverslag anonimiseer.", 2),
        ("Deel 4, afspraak 5 en de slotvraag hieronder zijn ingevuld.", 3),
    ])
    vraag(doc, "Een medeleerling loopt stage in een woonzorgcentrum en zegt: “Voor mij gelden precies dezelfde regels als voor jou in De Speelboom.” Klopt dat? Geef in één zin het verschil tussen discretieplicht en beroepsgeheim.")
    antwoordvak(doc, 1.5)

    # ---- Extra — niet verplicht
    deel(doc, None, "Extra — niet verplicht")
    vraag(doc, "De mama van Ilyas ziet op de openbare Facebookpagina van De Speelboom een foto van vorige maand. Ze had toen toestemming gegeven, maar stuurt nu een berichtje: “Ik wil die foto van Ilyas toch liever weg van Facebook. Kan dat nog?” Mag de mama haar toestemming intrekken, en wat moet De Speelboom doen?")
    antwoordvak(doc, 1.8)

    doc.save(os.path.join(HERE, "Privacyprotocol.docx"))


if __name__ == "__main__":
    privacyprotocol()
    print("Gemaakt: Privacyprotocol.docx")
