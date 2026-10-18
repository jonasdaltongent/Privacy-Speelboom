#!/usr/bin/env python3
"""
maak_stapjes.py — de beelden bij de stapjes op de lespagina (assets/stapjes/), uit het werkdocument zelf

Gebruik:  python3 maak_stapjes.py <leeg.pdf>     (vereist PyMuPDF en Pillow)

  leeg.pdf    Privacyprotocol zoals Google Documenten het toont: upload Privacyprotocol.docx in Drive (het wordt
              een Google-document) en kies Bestand › Downloaden › PDF-document (of Drive API files.export).
              De x in het eerste vak van deel 5 (s6-kruis.png) zet het script zelf in de pdf.
"""
import os
import sys

import fitz
from PIL import Image, ImageDraw

HIER = os.path.dirname(os.path.abspath(__file__))
UIT = os.path.join(HIER, "..", "assets", "stapjes")
SCHAAL = 2 * 96 / 72          # eerst op dubbele grootte tekenen, dan verkleinen: scherpe letters
ROOD = (197, 34, 31)
VAK = (0xF3, 0xF5, 0xFC)      # HEX_VAK in huisstijl.py
KADER = (0xEE, 0xF0, 0xF9)    # HEX_KADER


def kleur(fill):
    return tuple(round(c * 255) for c in fill) if fill else None


def vlakken(page, rgb):
    """De gevulde rechthoeken met deze kleur, van boven naar onder en van links naar rechts."""
    uit = []
    for d in page.get_drawings():
        k = kleur(d.get("fill"))
        if k and all(abs(a - b) <= 2 for a, b in zip(k, rgb)):
            uit.append(fitz.Rect(d["rect"]))
    uit.sort(key=lambda r: (round(r.y0), r.x0))
    return uit


def tekst(page, s, nr=0):
    treffers = page.search_for(s)
    if len(treffers) <= nr:
        raise SystemExit(f"'{s}' niet gevonden op bladzijde {page.number + 1}")
    return treffers[nr]


def bladzijde_met(doc, s):
    for p in doc:
        if p.search_for(s):
            return p
    raise SystemExit(f"'{s}' staat in geen enkele bladzijde")


def bewaar(page, naam, uitsnede, kaders=(), boven=None, onder=None):
    """Snijdt uitsnede (in pdf-punten) uit, tekent de rode kaders en bewaart op ware grootte."""
    os.makedirs(UIT, exist_ok=True)
    uitsnede = fitz.Rect(uitsnede) & page.rect
    pix = page.get_pixmap(matrix=fitz.Matrix(SCHAAL, SCHAAL), clip=uitsnede, alpha=False)
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    d = ImageDraw.Draw(im)
    if boven is not None:
        d.rectangle([0, 0, im.width, (boven - uitsnede.y0) * SCHAAL], fill="white")
    if onder is not None:
        d.rectangle([0, (onder - uitsnede.y0) * SCHAAL, im.width, im.height], fill="white")
    for k in kaders:
        k = fitz.Rect(k)
        box = [(k.x0 - uitsnede.x0) * SCHAAL - 6, (k.y0 - uitsnede.y0) * SCHAAL - 6,
               (k.x1 - uitsnede.x0) * SCHAAL + 6, (k.y1 - uitsnede.y0) * SCHAAL + 6]
        wit = [box[0] - 4, box[1] - 4, box[2] + 4, box[3] + 4]
        d.rounded_rectangle(wit, radius=16, outline=(255, 255, 255), width=4)
        d.rounded_rectangle(box, radius=12, outline=ROOD, width=5)
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    im.save(os.path.join(UIT, naam + ".png"), optimize=True)
    print("gemaakt:", naam + ".png", im.size)


def rand(r, x=8, y=8):
    return fitz.Rect(r.x0 - x, r.y0 - y, r.x1 + x, r.y1 + y)


def main(leeg):
    doc = fitz.open(leeg)

    # ---- bladzijde 1: kader en Deel 1
    p = bladzijde_met(doc, "Toestemming voor foto's")
    kdr = vlakken(p, KADER)[0]
    nora, finn = tekst(p, "Nora Peeters"), tekst(p, "Finn Jacobs")
    finn_regel = tekst(p, "stageverslag voor school: NEE", nr=1)
    bewaar(p, "s1-kader", rand(kdr, 10, 5),
           [fitz.Rect(kdr.x0 + 2, nora.y0 - 2, kdr.x1 - 2, max(finn.y1, finn_regel.y1) + 2)],
           boven=kdr.y0 - 1)

    kop1 = tekst(p, "Deel 1")
    vakken1 = [v for v in vlakken(p, VAK) if v.y0 > kop1.y1]
    rij_a = tekst(p, "a.  Je neemt")
    rechts_x = max(v.x1 for v in vakken1)
    links_x = tekst(p, "Situatie").x0 - 4
    deel1 = fitz.Rect(links_x, kop1.y0, rechts_x, vakken1[-1].y1)
    kopregel = tekst(p, "(ja of nee)")
    bewaar(p, "s2-deel1", rand(deel1),
           [fitz.Rect(links_x, max(rij_a.y0 - 4, kopregel.y1 + 2), rechts_x, vakken1[0].y0)])
    bewaar(p, "s2-mag-b", rand(deel1), [vakken1[0]])
    bewaar(p, "s2-waarom-b", rand(deel1), [vakken1[1]])

    # ---- bladzijde 2: Deel 2 en Deel 3
    p = bladzijde_met(doc, "Deel 2")
    kop2, kop3 = tekst(p, "Deel 2"), tekst(p, "Deel 3")
    vakken2 = [v for v in vlakken(p, VAK) if kop2.y1 < v.y0 < kop3.y0]
    rij2_a = tekst(p, "a.  In de WhatsApp")
    links2 = tekst(p, "Situatie").x0 - 4
    rechts2 = max(v.x1 for v in vakken2)
    deel2 = fitz.Rect(links2, kop2.y0, rechts2, vakken2[-1].y1)
    kopregel2 = tekst(p, "(ja of nee)")
    bewaar(p, "s3-deel2", rand(deel2),
           [fitz.Rect(links2, max(rij2_a.y0 - 4, kopregel2.y1 + 2), rechts2, vakken2[0].y0)])
    bewaar(p, "s3-mag-b", rand(deel2), [vakken2[0]])
    bewaar(p, "s3-waarom-b", rand(deel2), [vakken2[1]])

    vakken3 = [v for v in vlakken(p, VAK) if v.y0 > kop3.y1]
    # 4 rijen van 2 vakken bij vraag a (8 vakken), dan 1 groot vak bij vraag b
    qa = tekst(p, "a.  Welke vier")
    qb = tekst(p, "b.  Schrijf het verslag")
    links3, rechts3 = vakken3[-1].x0, vakken3[-1].x1
    vraag_a = rand(fitz.Rect(links3, qa.y0, rechts3, vakken3[7].y1), 8, 8)
    bewaar(p, "s4-deel3a-staat", vraag_a, [vakken3[0]])
    bewaar(p, "s4-deel3a-vervang", vraag_a, [vakken3[1]])
    bewaar(p, "s4-deel3b-verslag", rand(fitz.Rect(links3, qb.y0, rechts3, vakken3[8].y1), 8, 8),
           [fitz.Rect(links3, qb.y0 - 2, rechts3, vakken3[8].y1)])

    # ---- bladzijde 3: Deel 4 (5 vakken)
    p = bladzijde_met(doc, "Deel 4")
    kop4 = tekst(p, "Deel 4")
    vakken4 = [v for v in vlakken(p, VAK) if v.y0 > kop4.y1]
    links4 = tekst(p, "Onderdeel").x0 - 4
    rechts4 = max(v.x1 for v in vakken4)
    deel4 = rand(fitz.Rect(links4, kop4.y0, rechts4, vakken4[-1].y1), 8, 8)
    namen4 = ("s5-deel4-foto-maken", "s5-deel4-foto-delen", "s5-deel4-chat",
              "s5-deel4-verslag", "s5-deel4-twijfel")
    for naam, v in zip(namen4, vakken4):
        bewaar(p, naam, deel4, [v])

    # ---- bladzijde 4: Deel 5 en Extra
    p = bladzijde_met(doc, "Deel 5")
    kop5 = tekst(p, "Deel 5")
    kopx = tekst(p, "Extra")
    code = tekst(p, "Het codewoord")
    slot = tekst(p, "Een medeleerling loopt stage")
    vakken5 = [v for v in vlakken(p, VAK) if kop5.y1 < v.y0 < kopx.y0]
    antw_code = vakken5[0]
    vinkjes = vakken5[1:-1]
    antw_slot = vakken5[-1]
    links5, rechts5 = antw_code.x0, antw_code.x1

    bewaar(p, "s6-codewoord", rand(fitz.Rect(links5, kop5.y0, rechts5, antw_code.y1), 8, 10),
           [fitz.Rect(links5, code.y0 - 2, rechts5, antw_code.y1)], onder=antw_code.y1 + 4)
    tab5 = fitz.Rect(links5, kop5.y0, rechts5, vinkjes[-1].y1)
    bewaar(p, "s6-deel5", rand(tab5), onder=vinkjes[-1].y1 + 1)
    bewaar(p, "s6-slotvraag", rand(fitz.Rect(links5, slot.y0, rechts5, antw_slot.y1), 8, 10),
           [fitz.Rect(links5, slot.y0 - 2, rechts5, antw_slot.y1)])

    # de x in het eerste vak van deel 5 (alleen in het geheugen, voor s6-kruis.png)
    v = vinkjes[0]
    p.insert_textbox(fitz.Rect(v.x0, v.y0 + (v.height - 14) / 2 - 1, v.x1, v.y1), "x", fontsize=12,
                     fontname="helv", align=1)
    bewaar(p, "s6-kruis", rand(fitz.Rect(links5, vinkjes[0].y0, rechts5, vinkjes[2].y1), 8, 8), [vinkjes[0]],
           boven=vinkjes[0].y0 - 1, onder=vinkjes[2].y1 + 1)

    # Extra
    vx = [v for v in vlakken(p, VAK) if v.y0 > kopx.y1][0]
    qx = tekst(p, "De mama van Ilyas")
    bewaar(p, "s7-extra", rand(fitz.Rect(links5, kopx.y0, rechts5, vx.y1), 8, 10),
           [fitz.Rect(links5, qx.y0 - 2, rechts5, vx.y1)])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
