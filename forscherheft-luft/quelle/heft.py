"""Seiten des Schüler-Forscherhefts „Luft“ (Klasse 2)."""
from icons import (svg, place, glas, flasche, ballon, strohhalm, kreide, schwamm, radiergummi, tuete,
                   spritze, ball, schnur, klebeband, stuhl, papier, schuessel, schere, faden, heizung,
                   spirale_icon, uhr, taschenlampe, kind, stern, smiley, lufti, wolke, fahrrad,
                   luftmatratze, schwimmring, stein, buch, baum, fussgaenger, fenster, auto, fabrik)
from common import (HEFT_CSS, kopf, ck, luecke, lineatur, tipp, fuss, icon_box,
                    ICON_FRAGE, ICON_MATERIAL, ICON_VERSUCH, ICON_VERMUTUNG, ICON_BEOBACHTUNG, ICON_ERGEBNIS)
import illus

STUNDEN = {
    1: "Luft ist überall",
    2: "Luft braucht Platz",
    3: "Luft kann man zusammendrücken",
    4: "Luft treibt an und bremst",
    5: "Warme und kalte Luft",
    6: "Wir brauchen Luft",
}

TASCHENTUCH = ('<path d="M24 26 Q50 20 76 26 Q81 50 76 76 Q50 82 24 76 Q19 50 24 26 Z" fill="#ffffff"/>'
               '<path d="M30 32 Q50 52 70 70 M50 24 Q46 50 50 79" stroke-width="2" stroke="#9fb6c7"/>')

LUFTI_ICON = lufti()


def mat(items, eins=False):
    out = '<div class="chips">'
    for ic, text in items:
        out += f'<div class="chip"><span class="pic">{svg(ic)}</span><span>{text}</span></div>'
    return out + '</div>'


def steps(lst):
    return '<ol class="steps">' + "".join(f"<li>{s}</li>" for s in lst) + '</ol>'


def ergebnis(saetze, woerter):
    wk = ('<span class="wortkasten"><span class="lbl">Wörter:</span>'
          + "".join(f'<span class="wort">{w}</span>' for w in woerter) + '</span>')
    out = ('<div class="box ergebnis"><div class="ekopf">'
           + kopf(ICON_ERGEBNIS, "Das habe ich herausgefunden:") + wk + '</div>')
    out += "".join(f'<div class="satz">{s}</div>' for s in saetze)
    return out + '</div>'


def versuch(nr, seite, stunde, frage, material, illu, schritte, vermutung, beobachtung,
            saetze, woerter, tipp_text=None, profi=None, eins=False, vermutung_hint="Kreuze an.",
            vermutung_frage=""):
    out = '<section class="page">'
    out += (f'<div class="vhead"><span>Stunde {stunde} · {STUNDEN[stunde]}</span>'
            f'<span class="vnum">Versuch {nr}</span></div>')
    out += f'<div class="titel">{icon_box(ICON_FRAGE)}<h1>{frage}</h1></div>'
    out += f'<div class="matstrip">{kopf(ICON_MATERIAL, "Das brauchst du:")}{mat(material)}</div>'
    out += '<div class="mitte">'
    out += f'<div class="box">{kopf(ICON_VERSUCH, "So geht es:")}{steps(schritte)}</div>'
    out += f'<div class="box illu">{illu}</div>'
    out += '</div>'
    if vermutung:
        hint = (vermutung_frage + " " + vermutung_hint).strip()
        out += (f'<div class="box vermutung">{kopf(ICON_VERMUTUNG, "Das vermute ich:", hint)}'
                f'<div class="opts">{vermutung}</div></div>')
    out += f'<div class="box beobachtung grow">{beobachtung}</div>'
    out += ergebnis(saetze, woerter)
    if profi:
        out += profi
    if tipp_text:
        out += tipp(tipp_text)
    out += fuss(seite)
    out += '</section>'
    return out


def beob(hint, inner):
    return kopf(ICON_BEOBACHTUNG, "Das beobachte ich:", hint) + inner


def malfeld(scaff=None, ecke=""):
    s = f'<div class="scaff">{scaff}</div>' if scaff else ""
    e = f'<div class="ecke">{ecke}</div>' if ecke else ""
    return f'<div class="malfeld">{s}{e}</div>'


def nebeneinander(links, titel_rechts, rechts):
    return (f'<div class="nebeneinander"><div class="links">{links}</div>'
            f'<div class="rechts"><div class="kopf klein">{titel_rechts}</div>{rechts}</div></div>')


def profi_box(titel, inhalt):
    return (f'<div class="box profi"><div class="kopf"><span class="ico stern">{svg(stern("#ffe27a"))}</span>'
            f'<span>{titel}</span></div>{inhalt}</div>')


def jn():
    return f'{ck("ja")} {ck("nein")}'


# ------------------------------------------------------------------ Sonderseiten

def seite_deckblatt():
    return f'''<section class="page deck">
  <div class="deck-top">Mein Forscherheft</div>
  <div class="deck-luft">LUFT</div>
  <div class="deck-sub">Ich erforsche die Luft!</div>
  <div class="deck-bild">{illus.deckblatt()}</div>
  <div class="deck-felder">
    <div class="feld"><span>Name:</span><span class="strich"></span></div>
    <div class="feld klein"><span>Klasse:</span><span class="strich"></span></div>
  </div>
</section>'''


FAHRPLAN = [
    (1, "Kann man Luft fangen?", 5), (1, "Kann man Luft sehen?", 6),
    (2, "Bleibt das Taschentuch trocken?", 7), (2, "Kannst du den Ballon in der Flasche aufblasen?", 8),
    (3, "Kann man Luft zusammendrücken?", 9), (3, "Welcher Ball springt höher?", 10),
    (4, "Fliegt die Luftballon-Rakete?", 11), (4, "Welches Papier ist zuerst unten?", 12),
    (5, "Was passiert mit Luft, wenn sie warm wird?", 13), (5, "Tanzt die Schlange über der Heizung?", 14),
    (6, "Wie oft atme ich?", 15), (6, "Ist die Luft immer sauber?", 16),
]


def seite_fahrplan():
    rows = ""
    last = None
    nr = 0
    for st, titel, s in FAHRPLAN:
        nr += 1
        if st != last:
            rows += (f'<tr class="st"><td colspan="3"><span class="badge">Stunde {st}</span> '
                     f'{STUNDEN[st]}</td></tr>')
            last = st
        rows += (f'<tr><td class="nr"><span class="kreisnr">{nr}</span></td><td>{titel} <span class="s">S. {s}</span></td>'
                 f'<td class="stern">{svg(stern("#ffffff"))}</td></tr>')
    rows += ('<tr class="st"><td colspan="3"><span class="badge gold">Zum Schluss</span> Das weiß ich jetzt!</td></tr>'
             f'<tr><td class="nr"><span class="kreisnr gold">Q</span></td><td>Luft-Quiz <span class="s">S. 17</span></td><td class="stern">{svg(stern("#ffffff"))}</td></tr>'
             f'<tr><td class="nr"><span class="kreisnr gold">R</span></td><td>Das kann ich jetzt! <span class="s">S. 18</span></td><td class="stern">{svg(stern("#ffffff"))}</td></tr>')
    return f'''<section class="page">
  <div class="titel">{icon_box(svg_inner_stern())}<h1>Mein Forscher-Fahrplan</h1></div>
  <p class="intro">Hast du einen Versuch geschafft? Dann male den Stern bunt an.</p>
  <table class="fahrplan">{rows}</table>
  {fuss(2)}
</section>'''


def svg_inner_stern():
    return stern("#ffe27a")


def seite_regeln():
    kreis = [
        (ICON_FRAGE, "Frage", "Was will ich wissen?"),
        (ICON_VERMUTUNG, "Vermutung", "Was glaube ich?"),
        (ICON_VERSUCH, "Versuch", "Ich probiere es aus."),
        (ICON_BEOBACHTUNG, "Beobachtung", "Was sehe ich?"),
        (ICON_ERGEBNIS, "Ergebnis", "Was weiß ich jetzt?"),
    ]
    k = '<div class="kreis">'
    for i, (ic, t, u) in enumerate(kreis):
        if i:
            k += '<div class="pfeil">&#10140;</div>'
        k += f'<div class="kschritt"><div class="kico">{svg(ic)}</div><b>{t}</b><span>{u}</span></div>'
    k += '</div>'
    regeln = [
        "Ich höre gut zu und lese die Aufgabe genau.",
        "Ich vermute zuerst. Dann probiere ich aus.",
        "Ich arbeite ruhig und vorsichtig mit meinem Partnerkind.",
        "Ich puste nur in meinen eigenen Luftballon und meinen eigenen Strohhalm.",
        "Ich nehme nichts in den Mund, was nicht dazu gehört.",
        "Wenn Wasser daneben geht, wische ich es gleich auf.",
        "Am Ende räume ich meinen Platz auf.",
    ]
    r = '<ol class="steps regeln">' + "".join(f"<li>{x}</li>" for x in regeln) + '</ol>'
    return f'''<section class="page">
  <div class="titel">{icon_box(ICON_VERSUCH)}<h1>So forschen wir</h1></div>
  <p class="intro">Bei jedem Versuch gehst du diese Schritte. Die Bilder findest du in deinem ganzen Heft.</p>
  {k}
  <div class="titel" style="margin-top:7mm">{icon_box(LUFTI_ICON, vb="4 18 92 74")}<h1>Unsere Forscher-Regeln</h1></div>
  <div class="box">{r}</div>
  <div class="box unterschrift">
    <div>Ich halte mich an die Forscher-Regeln.</div>
    <div class="feld"><span>Unterschrift:</span><span class="strich"></span></div>
  </div>
  {tipp("Vermutungen dürfen auch falsch sein! Auch echte Forscherinnen und Forscher irren sich oft. Wichtig ist, dass du genau hinschaust.")}
  <div class="regelbild grow">{illus.forscherbild()}</div>
  {fuss(3)}
</section>'''


def seite_vorwissen():
    wolke_svg = svg(
        ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="#9db9cf" stroke-width="2.4"/>'
                for x, y, r in [(40, 70, 30), (80, 48, 36), (130, 40, 40), (176, 52, 34), (204, 82, 28),
                                (178, 108, 30), (128, 116, 34), (78, 110, 32), (36, 100, 26)])
        + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" stroke="none"/>'
                  for x, y, r in [(40, 70, 30), (80, 48, 36), (130, 40, 40), (176, 52, 34), (204, 82, 28),
                                  (178, 108, 30), (128, 116, 34), (78, 110, 32), (36, 100, 26)])
        + '<rect x="40" y="56" width="166" height="62" fill="#ffffff" stroke="none"/>',
        vb="4 0 232 152")
    return f'''<section class="page">
  <div class="vhead"><span>Stunde 1 · {STUNDEN[1]}</span><span class="vnum">Start</span></div>
  <div class="titel">{icon_box(ICON_VERMUTUNG)}<h1>Was weiß ich schon über Luft?</h1></div>
  <p class="intro">Male und schreibe in die Wolke: Was weißt du schon über Luft? Wo ist überall Luft?</p>
  <div class="vorwolke grow">{wolke_svg}</div>
  <div class="box">
    {kopf(ICON_FRAGE, "Das möchte ich über Luft herausfinden:")}
    {lineatur(3)}
  </div>
  {fuss(4)}
</section>'''


QUIZ = [
    ("Luft kann man sehen.", "M", "L"),
    ("Luft ist überall.", "U", "A"),
    ("In einer „leeren“ Flasche ist Luft.", "F", "K"),
    ("Luft braucht keinen Platz.", "S", "T"),
    ("Luft kann man zusammendrücken.", "B", "R"),
    ("Wind ist Luft, die sich bewegt.", "A", "E"),
    ("Luft kann Dinge bremsen.", "L", "I"),
    ("Warme Luft sinkt nach unten.", "N", "L"),
    ("Wenn ich renne, atme ich langsamer.", "U", "O"),
    ("Menschen, Tiere und Pflanzen brauchen Luft.", "N", "H"),
]


def seite_quiz():
    rows = ""
    for i, (satz, r, f) in enumerate(QUIZ, 1):
        rows += (f'<tr><td class="c qnr">{i}</td><td>{satz}</td>'
                 f'<td class="c"><span class="ck"></span><span class="bst">{r}</span></td>'
                 f'<td class="c"><span class="ck"></span><span class="bst">{f}</span></td></tr>')
    kaesten = "".join(f'<span class="lk"><i>{i}</i></span>' for i in range(1, 11))
    return f'''<section class="page">
  <div class="vhead"><span>Zum Schluss · Das weiß ich jetzt!</span><span class="vnum">Quiz</span></div>
  <div class="titel">{icon_box(ICON_FRAGE)}<h1>Das Luft-Quiz: richtig oder falsch?</h1></div>
  <p class="intro">Kreuze an. Neben deinem Kreuz steht ein Buchstabe. Schreibe ihn unten in das Kästchen mit der gleichen Nummer.</p>
  <table class="tab quiz">
    <tr><th class="c">Nr.</th><th>Aussage</th><th class="c">richtig</th><th class="c">falsch</th></tr>
    {rows}
  </table>
  <div class="box ergebnis loesung">
    {kopf(ICON_ERGEBNIS, "Das Lösungswort:")}
    <div class="lkasten">{kaesten}</div>
  </div>
  {tipp("Wenn alles stimmt, findest du ein Wort, das du in diesem Heft oft gebraucht hast!")}
  {fuss(17)}
</section>'''


def seite_kann_ich():
    aussagen = [
        "Ich weiß, dass Luft überall ist.",
        "Ich kann erklären, warum das Taschentuch trocken bleibt.",
        "Ich weiß, dass man Luft zusammendrücken kann.",
        "Ich weiß, dass Luft Dinge antreiben und bremsen kann.",
        "Ich weiß, was mit Luft passiert, wenn sie warm wird.",
        "Ich weiß, warum wir saubere Luft brauchen.",
        "Ich kann eine Vermutung ankreuzen und mit meiner Beobachtung vergleichen.",
    ]
    rows = "".join(
        f'<tr><td>{a}</td>'
        + "".join(f'<td class="c sm">{svg(smiley(k))}</td>' for k in ("gut", "mittel", "unsicher"))
        + '</tr>' for a in aussagen)
    return f'''<section class="page">
  <div class="vhead"><span>Zum Schluss · Das weiß ich jetzt!</span><span class="vnum">Rückblick</span></div>
  <div class="titel">{icon_box(svg_inner_stern())}<h1>Das kann ich jetzt!</h1></div>
  <p class="intro">Male das Gesicht an, das zu dir passt.</p>
  <table class="tab kann">
    <tr><th>Das kann ich:</th><th class="c">gut</th><th class="c">ein bisschen</th><th class="c">noch nicht</th></tr>
    {rows}
  </table>
  <div class="box">
    {kopf(ICON_ERGEBNIS, "Mein Lieblingsversuch war:")}
    {lineatur(2)}
  </div>
  <div class="box rueck grow">
    <div class="kopf">{icon_box(LUFTI_ICON, vb="4 18 92 74")}<span>Das sagt meine Lehrerin / mein Lehrer:</span></div>
  </div>
  {fuss(18)}
</section>'''


# ------------------------------------------------------------------ Versuchsseiten

def alle_versuche():
    p = []
    # Versuch 1
    p.append(versuch(
        1, 5, 1, "Kann man Luft fangen?",
        [(tuete(), "1 Gefrierbeutel"), (LUFTI_ICON, "Luft (ist schon da!)")],
        illus.v1(),
        ["Öffne die Tüte ganz weit.",
         "Schwinge die Tüte schnell durch die Luft.",
         "Drehe die Tüte oben fest zu.",
         "Drücke vorsichtig auf die Tüte."],
        ck("Die Tüte wird ganz flach.") + " " + ck("Die Tüte bleibt dick."),
        beob("Male deine Tüte.", malfeld()),
        [f"In der Tüte ist {luecke()}.",
         f"Ich kann Luft nicht {luecke()}, aber ich kann sie {luecke()}.",
         f"Luft ist {luecke()}."],
        ["Luft", "sehen", "spüren", "überall"],
        tipp_text="<b>Achtung:</b> Eine Tüte nie über den Kopf ziehen!", eins=True,
        vermutung_frage="Was passiert, wenn du auf die Tüte drückst?"))
    # Versuch 2
    tabelle = ('<table class="tab"><tr><th>Steigen Luft-Bläschen auf?</th><th class="c">Ich vermute:</th>'
               '<th class="c">Ich beobachte:</th></tr>'
               + "".join(f'<tr><td><span class="pic">{svg(ic)}</span>{t}</td><td class="c">{jn()}</td>'
                         f'<td class="c">{jn()}</td></tr>'
                         for ic, t in [(strohhalm(), "Ich puste mit dem Strohhalm."),
                                       (kreide(), "Kreide im Wasser"),
                                       (schwamm(), "Schwamm im Wasser"),
                                       (radiergummi(), "Radiergummi im Wasser")])
               + '</table>')
    p.append(versuch(
        2, 6, 1, "Kann man Luft sehen?",
        [(glas(True), "1 Glas mit Wasser"), (strohhalm(), "1 Strohhalm"), (kreide(), "1 Stück Kreide"),
         (schwamm(), "1 Stück Schwamm"), (radiergummi(), "1 Radiergummi")],
        illus.v2(),
        ["Puste mit dem Strohhalm vorsichtig ins Wasser.",
         "Lege nacheinander Kreide, Schwamm und Radiergummi ins Wasser.",
         "Schau genau hin: Steigen Bläschen auf?"],
        None,
        kopf(ICON_VERMUTUNG, "Erst vermuten, dann beobachten:", "Kreuze an.")
        + nebeneinander(tabelle, "Male die Bläschen in das Glas.", malfeld(illus.scaff_v2())),
        [f"Im Wasser kann ich Luft als {luecke()} sehen.",
         f"Auch in Kreide und im Schwamm steckt {luecke()}.",
         f"Luft ist {luecke()} – sogar in vielen Dingen!"],
        ["Bläschen", "Luft", "überall"],
        tipp_text="Nur ins Wasser pusten – nicht trinken!"))
    # Versuch 3
    p.append(versuch(
        3, 7, 2, "Bleibt das Taschentuch trocken?",
        [(glas(False), "1 Glas"), (TASCHENTUCH, "1 Papier-Taschentuch"), (schuessel(), "1 Schüssel mit Wasser")],
        illus.v3(),
        ["Knülle das Taschentuch zusammen.",
         "Drücke es ganz fest unten in das Glas.",
         "Drehe das Glas um. Die Öffnung zeigt nach unten.",
         "Drücke das Glas ganz gerade ins Wasser.",
         "Ziehe das Glas gerade heraus. Fühle das Taschentuch."],
        ck("Das Taschentuch wird nass.") + " " + ck("Das Taschentuch bleibt trocken."),
        beob("Male das Glas mit dem Taschentuch in die Schüssel.", malfeld(illus.scaff_v3())),
        [f"Das Taschentuch bleibt {luecke()}.",
         f"Im Glas ist {luecke()}. Die Luft braucht {luecke()}.",
         f"Darum kann das {luecke()} nicht in das Glas."],
        ["trocken", "Luft", "Platz", "Wasser"],
        tipp_text="Halte das Glas ganz gerade! Was passiert, wenn du es schief hältst?", eins=True))
    # Versuch 4
    p.append(versuch(
        4, 8, 2, "Kannst du den Ballon in der Flasche aufblasen?",
        [(flasche(cap=False), "1 leere Flasche"), (ballon(), "1 Luftballon")],
        illus.v4(),
        ["Stecke den Luftballon in die Flasche.",
         "Stülpe das Ende vom Luftballon über den Flaschenhals.",
         "Puste kräftig in den Luftballon."],
        ck("Der Luftballon wird groß.") + " " + ck("Der Luftballon bleibt klein."),
        beob("Male, was du beobachtest.", malfeld(illus.scaff_v4())),
        [f"Der Luftballon bleibt {luecke()}.",
         f"In der Flasche ist schon {luecke()}.",
         f"Die Luft braucht {luecke()}. Sie kann nicht heraus."],
        ["klein", "Luft", "Platz"],
        profi=profi_box("Profi-Versuch: Die Flasche mit Loch",
                        '<div>Probiere es mit der Flasche, die ein kleines Loch hat. Was passiert?</div>'
                        f'<div class="opts" style="margin-top:1mm">{ck("Der Luftballon wird groß.")} {ck("Der Luftballon bleibt klein.")}</div>'
                        '<div style="margin-top:1mm">Halte danach das Loch mit dem Finger zu. Nimm den Mund weg. Staune!</div>'),
        eins=True))
    # Versuch 5
    tab5 = ('<table class="tab"><tr><th>Kann ich den Kolben hineindrücken?</th><th class="c">Ich vermute:</th>'
            '<th class="c">Ich beobachte:</th></tr>'
            f'<tr><td><span class="pic">{svg(spritze())}</span>Spritze mit Luft</td><td class="c">{jn()}</td><td class="c">{jn()}</td></tr>'
            f'<tr><td><span class="pic">{svg(glas(True))}</span>Spritze mit Wasser</td><td class="c">{jn()}</td><td class="c">{jn()}</td></tr>'
            '</table>')
    p.append(versuch(
        5, 9, 3, "Kann man Luft zusammendrücken?",
        [(spritze(), "1 Spritze ohne Nadel"), (glas(True), "1 Becher mit Wasser"), (schuessel(), "1 Schüssel")],
        illus.v5(),
        ["Ziehe den Kolben weit zurück, aber nicht ganz heraus. Jetzt ist Luft in der Spritze.",
         "Halte vorne die Öffnung mit dem Finger fest zu.",
         "Drücke den Kolben hinein. Lass ihn dann los.",
         "Fülle die Spritze mit Wasser. Halte zu und drücke wieder."],
        None,
        kopf(ICON_VERMUTUNG, "Erst vermuten, dann beobachten:", "Kreuze an.")
        + nebeneinander(tab5 + '<div class="mini">' + kopf(ICON_BEOBACHTUNG, "Ich lasse den Kolben los. Was passiert?")
                        + f'<div class="opts col">{ck("Der Kolben bleibt stehen.")} {ck("Der Kolben springt zurück.")}</div></div>',
                        "Male die Spritze mit Luft.", malfeld()),
        [f"Luft kann man {luecke('lang')}.",
         f"Die Luft drückt zurück wie eine {luecke()}.",
         f"{luecke()} kann man nicht zusammendrücken."],
        ["zusammendrücken", "Feder", "Wasser"],
        tipp_text="Spritze das Wasser nur in die Schüssel!", eins=True))
    # Versuch 6
    alltag = [(fahrrad(), "Fahrrad"), (ball(), "Ball"), (luftmatratze(), "Luftmatratze"),
              (schwimmring(), "Schwimmring"), (stein(), "Stein"), (buch(), "Buch")]
    alltag_html = '<div class="bildreihe">' + "".join(
        f'<div class="bild"><span class="bico">{svg(ic)}</span><span>{t}</span></div>' for ic, t in alltag) + '</div>'
    p.append(versuch(
        6, 10, 3, "Welcher Ball springt höher?",
        [(ball(), "1 Ball mit viel Luft"), (ball("#a8e0b5", 0.8), "1 Ball mit wenig Luft")],
        illus.v6(),
        ["Halte beide Bälle gleich hoch.",
         "Lass beide Bälle gleichzeitig los.",
         "Schau genau: Welcher Ball springt höher?"],
        ck("Der Ball mit viel Luft.") + " " + ck("Der Ball mit wenig Luft."),
        beob("Welcher Ball ist höher gesprungen?",
             f'<div class="opts">{ck("Der Ball mit viel Luft.")} {ck("Der Ball mit wenig Luft.")}</div>'
             + '<div class="mini">' + kopf(ICON_FRAGE, "Wo steckt zusammengedrückte Luft drin?", "Kreise ein.")
             + alltag_html + '</div>'
             + '<div class="malfeld" style="margin-top:2mm"><div class="ecke">Male, wie hoch die beiden Bälle springen.</div></div>'),
        [f"Im Ball ist zusammengedrückte {luecke()}.",
         f"Sie drückt von innen und macht den Ball {luecke()}.",
         f"Der Ball mit viel Luft springt {luecke()}."],
        ["Luft", "prall", "höher"],
        tipp_text="Mit einer Ballpumpe drückt man Luft in den Ball.", eins=True,
        vermutung_frage="Welcher Ball springt höher?"))
    # Versuch 7
    p.append(versuch(
        7, 11, 4, "Fliegt die Luftballon-Rakete?",
        [(ballon(), "1 Luftballon"), (strohhalm(), "1 Strohhalm"), (schnur(), "1 lange Schnur"),
         (klebeband(), "Klebestreifen"), (stuhl(), "2 Stühle")],
        illus.v7(),
        ["Fädelt die Schnur durch den Strohhalm.",
         "Bindet die Schnur straff an zwei Stühlen fest.",
         "Blast den Luftballon auf. Haltet ihn zu – nicht zuknoten!",
         "Klebt den Luftballon an den Strohhalm.",
         "3 – 2 – 1 – los: Lasst den Luftballon los!"],
        ck("Die Rakete saust los.") + " " + ck("Die Rakete bleibt hängen."),
        beob("Male die Rakete. Zeichne Pfeile: Wohin strömt die Luft? Wohin fliegt der Ballon?",
             malfeld(illus.scaff_v7())
             + f'<div class="satz" style="margin-top:1.5mm">Unsere Rakete ist {luecke("kurz")} Schritte weit geflogen.</div>'),
        [f"Die Luft strömt hinten aus dem Ballon {luecke()}.",
         f"Dabei schiebt sie den Ballon nach {luecke()}.",
         f"Luft kann Dinge {luecke()}."],
        ["heraus", "vorne", "antreiben"],
        tipp_text="Echte Raketen fliegen genauso: Hinten strömt etwas heraus – und die Rakete fliegt nach vorne."))
    # Versuch 8
    p.append(versuch(
        8, 12, 4, "Welches Papier ist zuerst unten?",
        [(papier(), "2 gleiche Blätter Papier")],
        illus.v8(),
        ["Knülle ein Blatt zu einer Kugel.",
         "Halte das glatte Blatt und die Papier-Kugel gleich hoch.",
         "Lass beide gleichzeitig los."],
        ck("das glatte Blatt") + " " + ck("die Papier-Kugel") + " " + ck("beide gleich"),
        beob("Was war zuerst unten?",
             f'<div class="opts">{ck("das glatte Blatt")} {ck("die Papier-Kugel")} {ck("beide gleich")}</div>'
             + '<div class="malfeld" style="margin-top:2mm"><div class="ecke">Male, wie das glatte Blatt nach unten fällt.</div></div>'),
        [f"Das glatte Blatt fällt {luecke()}.",
         f"Die Luft drückt von unten dagegen. Sie {luecke()} das Blatt.",
         f"So funktioniert auch ein {luecke()}."],
        ["langsam", "bremst", "Fallschirm"],
        profi=profi_box("Profi-Versuch: Baue einen Fallschirm!",
                        "Die Anleitung steht auf der Expertenkarte. Lass deinen Fallschirm und eine Büroklammer gleichzeitig fallen."),
        eins=True, vermutung_frage="Was ist zuerst auf dem Boden?"))
    # Versuch 9
    p.append(versuch(
        9, 13, 5, "Was passiert mit Luft, wenn sie warm wird?",
        [(flasche(cap=False), "1 leere Flasche"), (ballon(), "1 Luftballon"),
         (schuessel("warm"), "warmes Wasser"), (schuessel("kalt"), "kaltes Wasser")],
        illus.v9(),
        ["Puste den Luftballon einmal auf. Lass die Luft wieder heraus.",
         "Stülpe den Luftballon über den Flaschenhals.",
         "Stelle die Flasche in das warme Wasser. Warte kurz.",
         "Stelle die Flasche danach in das kalte Wasser."],
        ck("Der Ballon wird dicker.") + " " + ck("Der Ballon bleibt schlapp."),
        beob("Male den Luftballon auf die Flaschen.", malfeld(illus.scaff_v9())),
        [f"Warme Luft dehnt sich {luecke()}. Sie braucht mehr {luecke()}.",
         f"Kalte Luft zieht sich {luecke()}."],
        ["aus", "Platz", "zusammen"],
        tipp_text="Das warme Wasser gießt ein Erwachsener ein.", eins=True,
        vermutung_frage="Was passiert im warmen Wasser mit dem Luftballon?"))
    # Versuch 10
    p.append(versuch(
        10, 14, 5, "Tanzt die Schlange über der Heizung?",
        [(spirale_icon(), "Schlangen-Vorlage"), (schere(), "1 Schere"), (faden(), "1 Faden"),
         (heizung(), "warme Heizung")],
        illus.v10(),
        ["Male die Schlange bunt an.",
         "Schneide sie an der Linie entlang aus.",
         "Stich mit dem Bleistift ein Loch in den Kopf. Ziehe den Faden durch und mache einen Knoten.",
         "Halte die Schlange am Faden über die warme Heizung. Halte ganz still und warte."],
        ck("Die Schlange dreht sich.") + " " + ck("Die Schlange bewegt sich nicht."),
        beob("Male die Schlange über die Heizung. Zeichne Pfeile: Wohin strömt die warme Luft?",
             malfeld(illus.scaff_v10())),
        [f"Die Heizung macht die Luft {luecke()}.",
         f"Warme Luft steigt nach {luecke()}.",
         f"Sie bringt die Schlange zum {luecke()}."],
        ["warm", "oben", "Drehen"],
        tipp_text="Nicht pusten! Die Luft soll die Schlange ganz allein bewegen."))
    # Versuch 11
    p.append(versuch(
        11, 15, 6, "Atem-Detektive: Wie oft atme ich?",
        [(kind("bauch"), "du selbst"), (uhr(), "eine Uhr")],
        illus.v11(),
        ["Setz dich ruhig hin. Lege eine Hand auf deinen Bauch.",
         "Beim Start-Zeichen zählst du deine Atemzüge, bis „Stopp!“ kommt.",
         "Mache eine Minute lang Hampelmann.",
         "Zähle gleich danach wieder deine Atemzüge."],
        ck("schneller") + " " + ck("langsamer") + " " + ck("gleich schnell"),
        beob("Schreibe die Zahlen auf.",
             '<div class="atem">'
             f'<div class="az"><span class="aico">{svg(kind("bauch"))}</span><span>In Ruhe:<br>{luecke("kurz")} Atemzüge</span></div>'
             f'<div class="az"><span class="aico">{svg(kind("hoch", shirt="#ffd27a"))}</span><span>Nach dem Hampelmann:<br>{luecke("kurz")} Atemzüge</span></div>'
             '</div>'
             + '<div class="malfeld" style="margin-top:2mm"><div class="ecke">Platz für deine Notizen oder ein Bild</div></div>'),
        [f"Wir atmen Luft {luecke('kurz')} und wieder {luecke('kurz')}.",
         f"Wenn wir uns bewegen, brauchen wir mehr {luecke()}.",
         f"Menschen, Tiere und Pflanzen brauchen Luft zum {luecke()}."],
        ["ein", "aus", "Luft", "Leben"],
        tipp_text="Ein Atemzug heißt: einmal einatmen und einmal ausatmen.", eins=True,
        vermutung_frage="Nach dem Hampelmann atme ich …"))
    # Versuch 12
    gut = [(fussgaenger(), "zu Fuß gehen"), (fahrrad(), "Rad fahren"), (baum(), "Bäume pflanzen"),
           (fenster(), "Fenster öffnen und lüften"), (auto(), "Auto-Motor laufen lassen"), (fabrik(), "viel Rauch")]
    gut_html = '<div class="bildreihe kreis">' + "".join(
        f'<div class="bild"><span class="bico">{svg(ic)}</span><span>{t}</span><span class="punkt"></span></div>'
        for ic, t in gut) + '</div>'
    p.append(versuch(
        12, 16, 6, "Ist die Luft immer sauber?",
        [(taschenlampe(False), "1 Taschenlampe"), (fenster(), "ein dunkles Zimmer")],
        illus.v12(),
        ["Macht das Zimmer dunkel.",
         "Leuchtet mit der Taschenlampe quer durch das Zimmer.",
         "Schaut ganz genau in den Licht-Strahl."],
        ck("Ich sehe nichts.") + " " + ck("Ich sehe kleine Körnchen."),
        beob("Was siehst du im Licht-Strahl?",
             f'<div class="opts">{ck("Ich sehe nichts.")} {ck("Ich sehe kleine Staub-Körnchen tanzen.")}</div>'
             + '<div class="mini">' + kopf(ICON_FRAGE, "Was ist gut für saubere Luft?",
                                           "Male den Kreis grün (gut) oder rot (nicht gut) an.")
             + gut_html + '</div>'
             + '<div class="malfeld" style="margin-top:2mm"><div class="ecke">Male, was du im Licht-Strahl gesehen hast.</div></div>'),
        [f"In der Luft schwebt oft {luecke()}.",
         f"Beim Lüften kommt frische {luecke()} ins Klassenzimmer.",
         f"Ich helfe der Luft: Ich gehe zu {luecke('kurz')} oder fahre mit dem {luecke()}."],
        ["Staub", "Luft", "Fuß", "Fahrrad"], eins=True,
        vermutung_frage="Was siehst du im Licht-Strahl?"))
    return p


EXTRA_CSS = """
.deck { align-items: center; text-align: center; padding-top: 16mm; }
.deck-top { font-size: 30pt; font-weight: 700; color: var(--blue); }
.deck-luft { font-size: 124pt; font-weight: 700; line-height: 1; letter-spacing: 6mm; color: #ffffff;
  -webkit-text-stroke: 1.4mm var(--ink); paint-order: stroke fill; margin-top: 2mm; padding-left: 6mm; }
.deck-sub { font-size: 20pt; margin-top: 1mm; }
.deck-bild { width: 172mm; margin-top: 4mm; flex: 1 1 auto; min-height: 0; display: flex; align-items: center; }
.deck-bild svg { width: 100%; height: 100%; }
.deck-felder { width: 168mm; display: flex; gap: 8mm; margin-bottom: 4mm; font-size: 17pt; }
.feld { display: flex; align-items: flex-end; gap: 3mm; flex: 3; }
.feld.klein { flex: 1.2; }
.feld .strich { flex: 1; border-bottom: 0.5mm solid var(--ink); height: 10mm; }
.intro { margin: 1mm 0 3mm; font-size: 13.5pt; }
table.fahrplan { width: 100%; border-collapse: separate; border-spacing: 0 0.9mm; font-size: 13pt; }
table.fahrplan td { padding: 0.6mm 2.5mm; background: #fff; border-top: 0.4mm solid var(--sky2); border-bottom: 0.4mm solid var(--sky2); }
table.fahrplan tr td:first-child { border-left: 0.4mm solid var(--sky2); border-radius: 2.5mm 0 0 2.5mm; }
table.fahrplan tr td:last-child { border-right: 0.4mm solid var(--sky2); border-radius: 0 2.5mm 2.5mm 0; }
table.fahrplan tr.st td { background: var(--sky); font-weight: 700; color: var(--blue); border-color: var(--sky); padding: 0.8mm 2.5mm; font-size: 12.5pt; }
table.fahrplan .kreisnr { display: inline-flex; width: 7mm; height: 7mm; border-radius: 50%; border: 0.5mm solid var(--blue); color: var(--blue);
  align-items: center; justify-content: center; font-weight: 700; font-size: 11pt; }
table.fahrplan .kreisnr.gold { border-color: #d99a1e; color: #b07a10; }
table.fahrplan .badge { background: var(--blue); color: #fff; border-radius: 6mm; padding: 0.2mm 3mm; margin-right: 2mm; font-size: 11pt; }
table.fahrplan .badge.gold { background: #d99a1e; }
table.fahrplan .nr { width: 12mm; text-align: center; }
table.fahrplan .s { color: var(--muted); font-size: 10.5pt; white-space: nowrap; }
table.fahrplan td.stern { width: 14mm; height: 10mm; }
table.fahrplan td.stern svg { width: 8.5mm; height: 8.5mm; margin: 0 auto; }
.kreis { display: flex; align-items: stretch; justify-content: space-between; gap: 1mm; }
.kschritt { flex: 1; display: flex; flex-direction: column; align-items: center; text-align: center; background: var(--sky);
  border-radius: 4mm; padding: 3.5mm 1.5mm; font-size: 12pt; line-height: 1.2; }
.kschritt b { font-size: 13pt; margin-top: 1.5mm; }
.kico { width: 20mm; height: 20mm; }
.pfeil { align-self: center; font-size: 15pt; color: var(--blue); font-family: 'DejaVu Sans', sans-serif; }
.regeln { font-size: 15pt; }
.regeln li { margin: 3.2mm 0; }
.regeln li::before { top: 0.6mm; }
.unterschrift { display: flex; flex-direction: column; gap: 3mm; }
.unterschrift .feld { font-size: 13pt; }
.vorwolke { display: flex; align-items: center; justify-content: center; margin: 2mm 0; }
.vorwolke svg { width: 100%; height: 100%; }
.mini { margin-top: 2mm; }
.box.beobachtung .tab { font-size: 12pt; }
.box.beobachtung .tab th, .box.beobachtung .tab td { padding: 1mm 2mm; }
.tab .ck { margin-right: 0.8mm; }
.tab td.c .opt { margin: 0 1.2mm; }
.bildreihe { display: grid; grid-template-columns: repeat(6, 1fr); gap: 2mm; text-align: center; font-size: 10.5pt; line-height: 1.15; }
.bildreihe .bild { display: flex; flex-direction: column; align-items: center; gap: 1mm; background: #fff; border-radius: 3mm; padding: 1.5mm 1mm; border: 0.4mm solid #ddd3f2; }
.bildreihe .bico { width: 16mm; height: 16mm; }
.bildreihe .punkt { width: 6mm; height: 6mm; border-radius: 50%; border: 0.5mm solid var(--ink); background: #fff; margin-top: auto; }
.atem { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm; }
.atem .az { display: flex; align-items: center; gap: 2mm; background: #fff; border-radius: 3mm; padding: 1.5mm 2mm; border: 0.4mm solid #ddd3f2; font-size: 12.5pt; line-height: 1.6; }
.atem .aico { width: 15mm; height: 15mm; flex: none; }
table.quiz { font-size: 14.5pt; }
table.quiz th, table.quiz td { border-color: var(--sky2); padding: 2.6mm 2.4mm; }
table.quiz th { background: var(--sky); }
table.quiz .qnr { width: 10mm; font-weight: 700; color: var(--blue); }
table.quiz td.c { width: 25mm; white-space: nowrap; }
table.quiz .bst { display: inline-block; font-weight: 700; color: var(--ink); font-size: 13pt; margin-left: 1.2mm; }
.lkasten { display: flex; gap: 2mm; justify-content: center; }
.lk { width: 15mm; height: 17mm; border: 0.5mm solid var(--ink); border-radius: 2mm; background: #fff; position: relative; }
.lk i { position: absolute; top: 0.4mm; left: 1mm; font-size: 8pt; color: var(--muted); font-style: normal; }
table.kann { font-size: 12.5pt; }
table.kann th, table.kann td { border-color: var(--sky2); }
table.kann th { background: var(--sky); }
table.kann td.sm { width: 22mm; }
table.kann td.sm svg { width: 10mm; height: 10mm; margin: 0 auto; }
.rueck { min-height: 30mm; border-style: dashed; }
"""


def build():
    pages = [seite_deckblatt(), seite_fahrplan(), seite_regeln(), seite_vorwissen()]
    pages += alle_versuche()
    pages += [seite_quiz(), seite_kann_ich()]
    return ('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8">'
            '<title>Mein Forscherheft: Luft (Klasse 2)</title>'
            f'<style>{HEFT_CSS}{EXTRA_CSS}</style></head><body>' + "\n".join(pages) + '</body></html>')

EXTRA_CSS += """
.nebeneinander { display: flex; gap: 3mm; flex: 1 1 auto; min-height: 0; }
.box.beobachtung > .nebeneinander { flex: 1 1 auto; }
.nebeneinander .links { flex: 1 1 auto; }
.nebeneinander .rechts { width: 44mm; flex: none; display: flex; flex-direction: column; }
.nebeneinander .tab { font-size: 11.5pt; }
.nebeneinander .tab td.c, .nebeneinander .tab th.c { width: 27mm; white-space: nowrap; }
.nebeneinander .tab td.c .opt { margin: 0 0.6mm; }
.nebeneinander .tab .ck { width: 4.8mm; height: 4.8mm; margin-right: 0.6mm; }
.nebeneinander .tab .pic { width: 8mm; height: 8mm; }
.nebeneinander .rechts .malfeld { flex: 1 1 auto; min-height: 25mm; }
.kopf.klein { font-size: 11.5pt; margin-bottom: 1mm; }
.regelbild { display: flex; align-items: center; justify-content: center; }
.regelbild svg { height: 100%; width: auto; max-width: 100%; }
"""
