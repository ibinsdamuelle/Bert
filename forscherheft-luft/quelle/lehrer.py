"""Lehrerhandreichung (Sequenzplanung) und Kopiervorlagen zum Forscherheft „Luft“."""
import math
from icons import (svg, place, lufti, ballon, stern, glas, flasche, strohhalm, schuessel, spritze, papier,
                   feder, fallschirm, muenze, uhr, schere, wolke, drachen, windrad, kind, INK, WATER_LINE)
from common import BASE_CSS, HEFT_CSS, ck, lineatur, icon_box, kopf, tipp, ICON_MATERIAL, ICON_VERSUCH, ICON_ERGEBNIS, ICON_FRAGE

# ---------------------------------------------------------------------------- Planung (Fließtext)

PLAN_CSS = BASE_CSS + """
body { font-size: 10.4pt; line-height: 1.42; }
h1 { font-size: 21pt; color: var(--blue); margin: 0 0 1mm; line-height: 1.15; }
h2 { font-size: 14.5pt; color: var(--blue); margin: 6mm 0 2mm; padding-bottom: 1mm; border-bottom: 0.5mm solid var(--sky2); break-after: avoid; }
h3 { font-size: 12pt; margin: 4mm 0 1.5mm; break-after: avoid; }
p { margin: 1.2mm 0 2mm; }
ul, ol { margin: 1mm 0 2mm; padding-left: 5.5mm; }
li { margin: 0.6mm 0; }
.sub { font-size: 12.5pt; color: var(--muted); margin-bottom: 4mm; }
.kopfband { display: flex; align-items: center; gap: 5mm; background: var(--sky); border-radius: 4mm; padding: 4mm 5mm; margin-bottom: 4mm; }
.kopfband .lu { width: 26mm; height: 22mm; flex: none; }
.info { display: grid; grid-template-columns: 34mm 1fr; gap: 1mm 3mm; margin: 2mm 0 3mm; }
.info b { color: var(--blue); }
.kasten { border: 0.5mm solid var(--sky2); background: #f7fbfe; border-radius: 3mm; padding: 2.5mm 4mm; margin: 2.5mm 0; break-inside: avoid; }
.kasten.gelb { background: var(--yellow-t); border-color: #ecd27a; }
.kasten.gruen { background: var(--green-t); border-color: #a9d8ba; }
.kasten.rot { background: #fdeeee; border-color: #f0b8b6; }
.kasten h3 { margin-top: 0; }
table.t { width: 100%; border-collapse: collapse; margin: 2mm 0 3mm; font-size: 9.6pt; line-height: 1.35; }
table.t th, table.t td { border: 0.35mm solid #c3d6e4; padding: 1.4mm 2mm; vertical-align: top; text-align: left; }
table.t th { background: var(--sky); color: var(--blue); }
table.t tr { break-inside: avoid; }
table.t td.z { white-space: nowrap; width: 11mm; text-align: center; }
table.t td.ph { width: 19mm; font-weight: 700; hyphens: auto; }
table.t td.sf { width: 16mm; }
table.t td.mt { width: 30mm; }
.std { break-before: page; }
.stunde { font-size: 10.2pt; line-height: 1.38; }
.stunde h3 { font-size: 10.8pt; margin: 2mm 0 1mm; }
.stunde p { margin: 0.8mm 0 1.2mm; }
.stunde ul { margin: 0.6mm 0 1mm; }
.stunde li { margin: 0.3mm 0; }
.stunde table.t { font-size: 9.7pt; line-height: 1.32; margin: 1.5mm 0 2mm; }
.stunde table.t th, .stunde table.t td { padding: 1.1mm 1.8mm; }
.stunde .kasten { padding: 2mm 3mm; margin: 1.5mm 0; }
.stunde .zwei { gap: 3mm; break-inside: avoid; }
.stunde .merksatz { font-size: 11.5pt; margin: 1.5mm 0 1mm; }
.stunde.eng { font-size: 9.6pt; }
.stunde.eng table.t { font-size: 9.2pt; }
.stdkopf { display: flex; justify-content: space-between; align-items: baseline; background: var(--blue); color: #fff;
  border-radius: 3mm; padding: 2.5mm 4mm; margin-bottom: 3mm; }
.stdkopf b { font-size: 15pt; }
.stdkopf span { font-size: 10pt; }
.zwei { display: grid; grid-template-columns: 1fr 1fr; gap: 4mm; }
.merksatz { font-size: 12.5pt; font-weight: 700; color: var(--green); }
.klein { font-size: 9pt; color: var(--muted); }
.loesung td:first-child { width: 30mm; font-weight: 700; }
"""


def stunde_kopf(nr, titel, seiten):
    return (f'<div class="stdkopf"><b>Stunde {nr}: {titel}</b><span>Forscherheft {seiten} · 45 Minuten</span></div>')


def verlauf(rows):
    h = ('<table class="t"><tr><th>Phase</th><th>Zeit</th><th>Unterrichtsgeschehen</th>'
         '<th>Sozialform</th><th>Material</th></tr>')
    for ph, z, inhalt, sf, mt in rows:
        h += f'<tr><td class="ph">{ph}</td><td class="z">{z}</td><td>{inhalt}</td><td class="sf">{sf}</td><td class="mt">{mt}</td></tr>'
    return h + '</table>'


def build_planung():
    lu = svg(lufti(), vb="4 18 92 74")
    h = []
    h.append(f'''
<div class="kopfband"><span class="lu">{lu}</span><div>
<h1>Luft – Forscherheft für die 2. Klasse</h1>
<div class="sub" style="margin:0">Lehrerhandreichung mit Sequenzplanung für 6 Unterrichtsstunden · HSU · Grundschule Bayern</div>
</div></div>

<div class="info">
<b>Fach</b><span>Heimat- und Sachunterricht (HSU), Jahrgangsstufe 2 (auch in Jahrgangsstufe 1/2 einsetzbar)</span>
<b>Umfang</b><span>6 Unterrichtsstunden à 45 Minuten</span>
<b>Arbeitsform</b><span>überwiegend Partnerarbeit, die Luftballon-Rakete in Vierergruppen</span>
<b>Material</b><span>Alltagsmaterial; Vorbereitung je Stunde ca. 5–15 Minuten, jeder Versuch dauert 5–15 Minuten</span>
<b>Bestandteile</b><span>Forscherheft (18 Seiten, Kopiervorlage pro Kind) · diese Handreichung · Kopiervorlagen:
Elternbrief, Wärme-Schlange, 8 Expertenkarten, Merksätze für die Tafel, Forscher-Urkunde</span>
</div>

<h2>1. Lehrplanbezug und Ziele</h2>
<p><b>LehrplanPLUS Grundschule Bayern, HSU, Jahrgangsstufe 1/2 – Lernbereich 3 „Natur und Umwelt“, Teilbereich 3.3 „Luft, Wasser, Wetter“.</b>
Die Sequenz bedient vor allem diese Kompetenzerwartungen (sinngemäß):</p>
<ul>
<li>Die Schülerinnen und Schüler wenden am Beispiel der Luft einfache naturwissenschaftliche Arbeitsweisen an:
vermuten, ausprobieren, beobachten, Ergebnisse festhalten.</li>
<li>Sie erklären die Bedeutung der Luft als natürliche Lebensgrundlage und beschreiben, was verantwortungsvolles Handeln im Umgang mit ihr bedeutet.</li>
<li>Inhalte u. a.: Luft und ihre Wirkungen, z. B. Gegenstände antreiben oder bremsen und Wasser verdrängen.</li>
</ul>
<p class="klein">Den genauen Wortlaut finden Sie im Fachlehrplan HSU auf lehrplanplus.bayern.de. Passend dazu gibt es vom ISB die
illustrierende Aufgabe „Luft – überall und doch nirgends“ (HSU 1/2).</p>

<div class="kasten gelb">
<h3>Der rote Faden: der Forscherkreislauf</h3>
<p>Jede Versuchsseite im Heft ist gleich aufgebaut:
<b>Frage → Material → So geht es → Vermutung → Beobachtung → Ergebnis</b>.
Die Symbole dafür werden auf Seite 3 eingeführt. Weil sich der Ablauf in jeder Stunde wiederholt, wird er zum Ritual.
So üben die Kinder ganz nebenbei die naturwissenschaftliche Arbeitsweise.</p>
<p style="margin-bottom:0">Wichtig: Die Vermutung wird <b>vor</b> dem Versuch angekreuzt, und falsche Vermutungen sind ausdrücklich erlaubt
(„Auch echte Forscher irren sich“). Am Ende jeder Stunde vergleichen die Kinder kurz: „Was habe ich vermutet – was ist passiert?“</p>
</div>

<h3>Didaktischer Aufbau</h3>
<p>Die Sequenz geht vom Phänomen zur Einsicht. Zuerst erleben die Kinder, dass die unsichtbare Luft „da“ ist (Std. 1).
Dann lernen sie Luft als Stoff kennen, der Platz braucht (Std. 2) und sich zusammendrücken lässt (Std. 3).
Danach geht es um ihre Wirkungen: Luft treibt an und bremst (Std. 4), und Wärme verändert Luft (Std. 5).
Zum Schluss geht es um die Bedeutung der Luft für das Leben und um den Umweltschutz (Std. 6).
Die Stunden bauen aufeinander auf: „Luft braucht Platz“ aus Stunde 2 erklärt in Stunde 5, warum sich der Ballon auf der warmen Flasche aufrichtet.</p>
''')

    # Übersicht
    h.append('''
<h2>2. Die Sequenz auf einen Blick</h2>
<table class="t">
<tr><th>Std.</th><th>Thema</th><th>Versuche im Heft</th><th>Merksatz (Tafel)</th><th>Heft</th></tr>
<tr><td class="z">1</td><td><b>Luft ist überall</b></td><td>Einstieg und Vorwissen (S. 4)<br>V1 Kann man Luft fangen? (Tüte)<br>V2 Kann man Luft sehen? (Strohhalm, Kreide, Schwamm)</td><td>Luft ist überall. Man kann sie nicht sehen, aber spüren.</td><td class="z">S. 1–6</td></tr>
<tr><td class="z">2</td><td><b>Luft braucht Platz</b></td><td>V3 Bleibt das Taschentuch trocken?<br>V4 Ballon in der Flasche (+ Profi: Flasche mit Loch)</td><td>Luft braucht Platz.</td><td class="z">S. 7–8</td></tr>
<tr><td class="z">3</td><td><b>Luft kann man zusammendrücken</b></td><td>V5 Die Spritze: Luft oder Wasser?<br>V6 Welcher Ball springt höher?</td><td>Luft kann man zusammendrücken.</td><td class="z">S. 9–10</td></tr>
<tr><td class="z">4</td><td><b>Luft treibt an und bremst</b></td><td>V7 Die Luftballon-Rakete<br>V8 Das Papier-Wettrennen</td><td>Luft kann Dinge antreiben und bremsen.</td><td class="z">S. 11–12</td></tr>
<tr><td class="z">5</td><td><b>Warme und kalte Luft</b></td><td>V9 Der Zauber-Ballon (warmes/kaltes Wasser)<br>V10 Die Wärme-Schlange</td><td>Warme Luft dehnt sich aus und steigt nach oben.</td><td class="z">S. 13–14</td></tr>
<tr><td class="z">6</td><td><b>Wir brauchen Luft</b></td><td>V11 Atem-Detektive<br>V12 Ist die Luft immer sauber?<br>Quiz, Rückblick, Urkunde</td><td>Wir alle brauchen saubere Luft zum Leben.</td><td class="z">S. 15–18</td></tr>
</table>
<p class="klein">Tipp: Teilen Sie das Heft vollständig in Stunde 1 aus, oder geben Sie die Seiten Stunde für Stunde aus und heften sie in einem Schnellhefter ab.
Für schnelle Kinder liegen in jeder Stunde Expertenkarten bereit (Kopiervorlagen, einmal pro Gruppe kopieren und laminieren).</p>
''')

    # Organisation & Sicherheit
    h.append('''
<h2>3. Organisation, Sicherheit und Hygiene</h2>
<div class="zwei">
<div>
<h3>So sparen Sie Zeit</h3>
<ul>
<li><b>Feste Forscherpaare</b> für die ganze Sequenz. Für die Rakete arbeiten zwei Paare zusammen.</li>
<li><b>Materialkisten:</b> Packen Sie vor der Stunde für jedes Paar eine Kiste (Schuhkarton, Tablett).
Ein Materialdienst holt und bringt sie zurück.</li>
<li><b>Wasserversuche</b> (Std. 1, 2, 3, 5): Tische mit Wachstuch oder Zeitung abdecken, Schüsseln nur halb füllen,
Lappen und Handtücher bereitlegen.</li>
<li><b>Lesehilfe:</b> Lesen Sie die Schritte gemeinsam. Bei Bedarf zeigen Sie den Aufbau kurz vor, ohne das Ergebnis zu verraten.</li>
<li><b>Flaschen und Luftballons</b> mit Namen beschriften. Sie werden in Stunde 2 und Stunde 5 gebraucht.</li>
<li>Die Seite 3 (Forscherkreislauf) vergrößert als Plakat an die Tafel hängen.</li>
</ul>
</div>
<div class="kasten rot" style="margin-top:4mm">
<h3>Sicherheit und Hygiene</h3>
<ul style="margin-bottom:0">
<li><b>Latex:</b> Luftballons enthalten meist Latex. Fragen Sie Allergien vorher ab (Elternbrief) und nehmen Sie bei Bedarf latexfreie Ballons.
Geplatzte Ballonreste sofort einsammeln.</li>
<li><b>Hygiene:</b> Jedes Kind pustet nur in den eigenen Ballon und den eigenen Strohhalm.</li>
<li><b>Plastiktüten</b> nie über den Kopf ziehen. Sprechen Sie das vor Versuch 1 ausdrücklich an.</li>
<li><b>Spritzen</b> nur ohne Nadel verwenden (Einwegspritzen aus der Apotheke).</li>
<li><b>Warmes Wasser</b> (Std. 5) höchstens ca. 50 °C. Die Lehrkraft gießt es ein.</li>
<li><b>Glas:</b> Wo möglich stabile, durchsichtige Kunststoffbecher nehmen.</li>
<li><b>Bewegung</b> (Std. 6): Achten Sie auf genug Abstand. Kinder mit Asthma o. Ä. hüpfen langsamer oder zählen nur.</li>
</ul>
</div>
</div>
''')

    # Materialliste
    mat_rows = [
        ("Gefrierbeutel (ca. 3 l)", "24 + Reserve", "1", "Supermarkt"),
        ("Durchsichtige Gläser oder stabile Kunststoffbecher", "12–24", "1, 2, 3", "Schulküche, Elternbrief"),
        ("Schüsseln (Salat- oder Spülschüssel, 2–3 l)", "12", "1, 2, 3, 5", "Schulküche, Elternbrief"),
        ("Strohhalme (Papier oder Mehrweg)", "30", "1, 4", "Supermarkt"),
        ("Tafelkreide (Stücke) · trockene Schwammstücke · Radiergummi", "je 12", "1", "Klassenzimmer; Küchenschwamm zerschneiden"),
        ("Papiertaschentücher", "1 Packung", "2", ""),
        ("Leere Plastikflaschen 0,5 l (ohne Deckel)", "24 + 1 mit Loch", "2, 5", "Kinder bringen sie mit (Elternbrief)"),
        ("Luftballons, rund, mittelgroß", "ca. 40", "2, 4, 5", "Drogerie; 1 pro Kind + 6 Raketen + Reserve"),
        ("Einwegspritzen ohne Nadel (10 oder 20 ml)", "12", "3", "Apotheke, wenige Cent pro Stück"),
        ("2 gleiche Bälle + Ballpumpe mit Ventilnadel", "1 Satz (oder 1 pro Gruppe)", "3", "Sporthalle"),
        ("Schnur oder Wolle, je ca. 4 m · Klebefilm", "6 · 6 Rollen", "4", ""),
        ("Schmierpapier A4", "2 pro Kind", "4", ""),
        ("Thermoskanne mit warmem Wasser (ca. 50 °C) · Eiswürfel", "1 · 1 Beutel", "5", "Lehrerzimmer"),
        ("Kopien Wärme-Schlange · Scheren · Buntstifte · Faden (je ca. 40 cm)", "je Kind", "5", "Kopiervorlage"),
        ("Uhr mit Sekundenzeiger oder Stoppuhr", "1", "6", ""),
        ("Taschenlampe(n), Verdunkelung", "1–6", "6", ""),
        ("Für die Expertenkarten zusätzlich: Postkarte oder Bierdeckel, Korken, Zahnstocher, Feder oder Watte, Murmel, "
         "Büroklammern, Stück Plastiktüte, Glasflasche (Kühlschrank), Münze, Taschenspiegel", "je 1–2", "2–6", ""),
    ]
    rows = "".join(f'<tr><td>{a}</td><td>{b}</td><td class="z">{c}</td><td>{d}</td></tr>' for a, b, c, d in mat_rows)
    h.append(f'''
<h2>4. Materialliste für die ganze Sequenz</h2>
<p>Die Mengen gelten für 24 Kinder (12 Paare, 6 Gruppen).</p>
<table class="t"><tr><th>Material</th><th>Menge</th><th>Std.</th><th>Woher?</th></tr>{rows}</table>
''')

    # ---------------- Stunden
    h.append('<div class="std stunde eng"><h2 style="margin-top:0">5. Die sechs Stunden im Detail</h2>')
    # Stunde 1
    h.append(stunde_kopf(1, "Luft ist überall", "S. 1–6"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erfahren, dass Luft überall ist, obwohl man sie nicht sieht,</li>
<li>nehmen Luft mit den Sinnen wahr (spüren, hören),</li>
<li>machen Luft im Wasser als Bläschen sichtbar,</li>
<li>lernen das Forscherheft und die Forscherregeln kennen.</li></ul>
</div><div>
<h3>Vorbereitung (ca. 10 Min.)</h3>
<ul><li>Gefrierbeutel (1 pro Kind)</li>
<li>pro Paar: Glas mit Wasser, 2 Strohhalme, 1 Stück Kreide, 1 trockenes Schwammstück</li>
<li>für den Einstieg: 1 Tüte oder 1 Luftballon</li>
<li>Merksatz-Streifen 1 (Kopiervorlage)</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "5'", "<b>Die „leere“ Tüte:</b> L hält eine Tüte hoch: „Was ist hier drin?“ – „Nichts!“ – L dreht die Tüte zu und drückt darauf: "
         "„Wirklich nichts?“ (Alternative: Luftballon aufblasen und zischend fliegen lassen.) Die Kinder äußern Ideen. Das Thema „Luft“ wird genannt.",
         "Sitzkreis", "Tüte oder Luftballon"),
        ("Hinführung", "8'", "Forscherheft austeilen, Namen eintragen. Forscherkreislauf und Forscherregeln (S. 3) besprechen und unterschreiben. "
         "S. 4: Vorwissen malen und schreiben (kann auch als Hausaufgabe beendet werden).", "Plenum, EA", "Heft S. 1–4"),
        ("Erarbeitung I", "10'", "<b>V1 Kann man Luft fangen?</b> Erst Vermutung ankreuzen, dann ausprobieren und die Tüte malen. "
         "Hinweis auf die Sicherheitsregel (Tüte nie über den Kopf).", "PA", "Gefrierbeutel, Heft S. 5"),
        ("Erarbeitung II", "12'", "<b>V2 Kann man Luft sehen?</b> In der Tabelle zuerst die Spalte „Ich vermute“ ausfüllen, dann testen. "
         "Bläschen in das Glas malen.", "PA", "Glas, Strohhalm, Kreide, Schwamm, Radiergummi, S. 6"),
        ("Sicherung", "8'", "Ergebnisse besprechen: Wo haben wir Luft gespürt, gehört und gesehen? Lückentexte S. 5/6. "
         "Merksatz an die Tafel.", "Plenum", "Merksatz 1"),
        ("Ausklang", "2'", "Aufräumen, im Forscher-Fahrplan (S. 2) die Sterne anmalen.", "", ""),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0">Luft ist ein Gasgemisch: etwa 78 % Stickstoff, 21 % Sauerstoff, dazu Argon und ein wenig Kohlenstoffdioxid. Sie ist farblos,
durchsichtig und geruchlos, deshalb „sehen“ wir sie nicht. Bewegte Luft können wir spüren (Wind) und hören (Rauschen, Zischen).
Kreide, Schwamm, Erde oder Ziegel haben viele kleine Hohlräume voller Luft. Unter Wasser wird diese Luft verdrängt.
Sie steigt als Bläschen nach oben, weil sie viel leichter ist als Wasser.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Normale Tafelkreide blubbert besonders gut.</li>
<li>Der Schwamm muss trocken sein. Unter Wasser kneten, dann kommen viele Blasen.</li>
<li>Der Radiergummi ist das Gegenbeispiel: kaum Bläschen. Das schult das genaue Beobachten.</li>
<li>Erinnern Sie daran: nur pusten, nicht saugen.</li>
<li><b>Für schnelle Kinder:</b> weitere Dinge testen (Erde, Stein, Würfelzucker) oder S. 4 weiter gestalten.</li></ul></div>
</div>
<p class="merksatz">Merksatz: Luft ist überall. Man kann sie nicht sehen, aber spüren.</p>
<p class="klein">Optionaler Langzeitversuch „Staubfänger“: Kleben Sie heute Karteikarten mit Klebefilm (Klebeseite nach außen)
an verschiedene Orte (Fensterbank innen, Schulhof, Straßenseite). In Stunde 6 vergleichen die Kinder sie mit der Lupe.</p>
</div>''')
    # Stunde 2
    h.append('<div class="std stunde">' + stunde_kopf(2, "Luft braucht Platz", "S. 7–8"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erkennen, dass Luft Platz braucht und Wasser verdrängt,</li>
<li>übertragen diese Erkenntnis auf den Ballon in der Flasche,</li>
<li>vergleichen ihre Vermutung mit dem Ergebnis.</li></ul>
</div><div>
<h3>Vorbereitung (ca. 15 Min.)</h3>
<ul><li>Schüsseln halb mit Wasser füllen, Gläser und Taschentücher bereitlegen</li>
<li>Flaschen (von den Kindern) und Luftballons mit Namen</li>
<li><b>1 Flasche mit Loch</b> für den Profi-Versuch: Mit einem heißen Nagel oder einer Scherenspitze ein ca. 3 mm großes Loch
in die untere Hälfte bohren (nur die Lehrkraft).</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "5'", "Merksatz der letzten Stunde wiederholen. Impuls: L stopft ein Taschentuch in ein Glas. „Ich tauche das Glas mit der Öffnung "
         "nach unten ins Wasser. Was passiert mit dem Taschentuch?“ Vermutungen sammeln, <b>nicht</b> auflösen.", "Sitzkreis", "Glas, Taschentuch"),
        ("Erarbeitung I", "15'", "<b>V3 Bleibt das Taschentuch trocken?</b> Vermutung, Versuch, Beobachtung malen. "
         "Impuls für Schnelle: „Was passiert, wenn du das Glas schief hältst?“ (Blasen steigen auf, das Tuch wird nass.)", "PA", "Glas, Taschentuch, Schüssel, S. 7"),
        ("Zwischen&shy;sicherung", "5'", "Kinder erklären: „Im Glas ist Luft. Sie lässt das Wasser nicht hinein.“ Die Lehrkraft zeigt das schräge Glas "
         "mit den aufsteigenden Blasen.", "Plenum", ""),
        ("Erarbeitung II", "12'", "<b>V4 Ballon in der Flasche.</b> Danach als Profi-Versuch an der Lehrerflasche mit Loch: Jetzt klappt es! "
         "Loch zuhalten, Mund weg: Der Ballon bleibt aufgeblasen.", "PA / EA", "Flasche, Ballon, Flasche mit Loch, S. 8"),
        ("Sicherung", "8'", "Lückentexte S. 7/8, Merksatz an die Tafel, Sterne im Fahrplan anmalen.", "Plenum", "Merksatz 2"),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0">Luft ist ein Stoff und nimmt Raum ein. Taucht man das Glas senkrecht ein, kann die Luft nicht entweichen. Sie wird nur ein wenig
zusammengedrückt, deshalb steigt das Wasser ein kleines Stück ins Glas. Kippt man das Glas, entweicht Luft als Blase und Wasser strömt nach.
In der „leeren“ Flasche ist Luft. Damit der Ballon größer werden kann, müsste diese Luft hinaus, doch der Ballon verschließt den Flaschenhals.
Durch ein Loch kann die Luft entweichen. Hält man das Loch zu, kann keine Luft zurückströmen, und der Ballon bleibt groß.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Das Taschentuch fest in den Glasboden drücken, damit es beim Umdrehen nicht herausfällt.</li>
<li>Das Glas ganz senkrecht eintauchen und herausziehen. Die Schüssel muss tief genug sein.</li>
<li>Bei V4 gelingt der Kontrast am besten, wenn der Ballon vorher einmal aufgeblasen (vorgedehnt) wurde.</li>
<li><b>Für schnelle Kinder:</b> Expertenkarte 1 „Kannst du Luft umfüllen?“</li></ul></div>
</div>
<p class="merksatz">Merksatz: Luft braucht Platz. Wo Luft ist, kann nichts anderes sein.</p>
</div>''')
    # Stunde 3
    h.append('<div class="std stunde">' + stunde_kopf(3, "Luft kann man zusammendrücken", "S. 9–10"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erfahren, dass man Luft zusammendrücken kann und dass sie wie eine Feder zurückdrückt,</li>
<li>vergleichen Luft mit Wasser,</li>
<li>entdecken zusammengedrückte Luft im Alltag.</li></ul>
</div><div>
<h3>Vorbereitung (ca. 10 Min.)</h3>
<ul><li>pro Paar: 1 Spritze ohne Nadel, 1 Becher Wasser, 1 Schüssel</li>
<li>2 gleiche Bälle. Aus einem mit der Ventilnadel einen Teil der Luft ablassen.</li>
<li>Ballpumpe, evtl. Luftpolsterfolie, Luftmatratze oder Schwimmring zum Zeigen</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "5'", "L zeigt eine Luftpumpe: „Wofür braucht man die?“ Die Kinder erzählen (Fahrrad, Ball, Luftmatratze). "
         "„Wie passt so viel Luft in einen Fahrradreifen?“", "Sitzkreis", "Luftpumpe"),
        ("Erarbeitung I", "15'", "<b>V5 Die Spritze.</b> Zuerst mit Luft, dann mit Wasser (über der Schüssel). Tabelle: erst vermuten, dann beobachten.",
         "PA", "Spritze, Becher, Schüssel, S. 9"),
        ("Erarbeitung II", "10'", "<b>V6 Welcher Ball springt höher?</b> Vorführung mit zwei Kindern vor der Klasse (oder in Gruppen). "
         "Danach den schlaffen Ball aufpumpen und noch einmal testen.", "Plenum / GA", "2 Bälle, Pumpe, S. 10"),
        ("Sicherung", "12'", "Alltagsaufgabe S. 10 (Was ist mit Luft gefüllt?). Luftpolsterfolie zum Fühlen herumgeben. "
         "Lückentexte, Merksatz an die Tafel.", "EA, Plenum", "Merksatz 3"),
        ("Ausklang", "3'", "Aufräumen, Sterne anmalen.", "", ""),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0">Gase lassen sich zusammendrücken, weil zwischen ihren Teilchen viel Platz ist. Flüssigkeiten lassen sich praktisch nicht
zusammendrücken. Zusammengedrückte Luft drückt zurück („Luftfeder“). Das nutzt man bei Reifen, Bällen, Luftmatratzen, Hüpfburgen und
Luftpolsterfolie. Ein prall gefüllter Ball springt höher, weil die Luft darin beim Aufprall wie eine Feder wirkt.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Bei der Wasser-Spritze darf keine Luftblase drin sein, sonst lässt sich der Kolben doch etwas drücken.
Am besten mehrmals aufziehen und ausdrücken.</li>
<li>Beim Ball-Test beide Bälle aus gleicher Höhe (z. B. Schulterhöhe) auf harten Boden fallen lassen.</li>
<li><b>Für schnelle Kinder:</b> Expertenkarte 2 „Der Wasser-Zaubertrick“ und Expertenkarte 3 „Die Strohhalm-Pipette“ (Luft drückt).</li></ul></div>
</div>
<p class="merksatz">Merksatz: Luft kann man zusammendrücken. Sie drückt zurück wie eine Feder.</p>
</div>''')
    # Stunde 4
    h.append('<div class="std stunde">' + stunde_kopf(4, "Luft treibt an und bremst", "S. 11–12"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erfahren, dass ausströmende Luft etwas antreiben kann (Rückstoß),</li>
<li>erfahren, dass Luft fallende Dinge bremst,</li>
<li>vergleichen und messen (Flugweite in Schritten).</li></ul>
</div><div>
<h3>Vorbereitung (ca. 10 Min.)</h3>
<ul><li>6 Schnüre à ca. 4 m, 6 Strohhalme (auf ca. 8 cm kürzen), Klebestreifen vorschneiden und an die Tischkante kleben</li>
<li>Luftballons, Platz für die Raketenbahnen (Gang, Flur oder Tische zur Seite)</li>
<li>Schmierpapier (2 Blätter pro Kind)</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "5'", "L bläst einen Luftballon auf und lässt ihn los. Er saust kreuz und quer durch die Klasse. "
         "„Wie können wir den Ballon lenken, damit er geradeaus fliegt?“ Idee: an einer Schnur.", "Sitzkreis", "Luftballon"),
        ("Erarbeitung I", "17'", "<b>V7 Die Luftballon-Rakete</b> in Vierergruppen: Vermutung, Bau, Start. Flugweite in Schritten messen, "
         "Rakete mit Pfeilen malen. Mehrere Starts sind erlaubt.", "GA", "Schnur, Strohhalm, Ballon, Klebefilm, 2 Stühle, S. 11"),
        ("Erarbeitung II", "10'", "<b>V8 Welches Papier ist zuerst unten?</b> Vermutung, Versuch (mehrmals wiederholen), Beobachtung.",
         "PA", "Papier, S. 12"),
        ("Sicherung", "10'", "Gespräch: Wo treibt Luft etwas an? (Segelboot, Windrad, Drachen) Wo bremst Luft? (Fallschirm, Pusteblume, "
         "Ahornsamen) Lückentexte, Merksatz.", "Plenum", "Merksatz 4"),
        ("Ausklang", "3'", "Aufräumen, Sterne anmalen.", "", ""),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0"><b>Rückstoß:</b> Die zusammengedrückte Luft strömt hinten aus dem Ballon heraus. Dabei wird der Ballon in die
Gegenrichtung geschoben, genau wie bei einer Rakete. <b>Luftwiderstand:</b> Ein fallender Gegenstand muss die Luft vor sich zur Seite schieben.
Je größer seine Fläche im Verhältnis zum Gewicht ist, desto stärker bremst ihn die Luft. Das glatte Blatt und die Papierkugel sind gleich schwer,
nur ihre Form ist verschieden.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Die Schnur straff spannen. Die Ballonöffnung zeigt zum Startstuhl.</li>
<li>Den Ballon nicht zuknoten: Ein Kind hält zu, ein anderes klebt zwei Klebestreifen quer über den Ballon an den Strohhalm.</li>
<li>Die Raketen fliegen meist 2–4 Meter.</li>
<li><b>Für schnelle Kinder:</b> Expertenkarten 4 „Puste-Test“, 5 „Fallschirm“ und 6 „Puste-Boot“.</li></ul></div>
</div>
<p class="merksatz">Merksatz: Luft kann Dinge antreiben und bremsen.</p>
</div>''')
    # Stunde 5
    h.append('<div class="std stunde">' + stunde_kopf(5, "Warme und kalte Luft", "S. 13–14 + Kopiervorlage"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erfahren, dass sich Luft beim Erwärmen ausdehnt und beim Abkühlen zusammenzieht,</li>
<li>beobachten, dass warme Luft nach oben steigt,</li>
<li>wenden „Luft braucht Platz“ auf eine neue Situation an.</li></ul>
</div><div>
<h3>Vorbereitung (ca. 15 Min.)</h3>
<ul><li>Wasser im Wasserkocher erhitzen, mit kaltem Wasser auf ca. 50 °C mischen und in die Thermoskanne füllen</li>
<li>Kaltes Wasser mit Eiswürfeln, Schüsseln</li>
<li>Flaschen und Ballons aus Stunde 2</li>
<li>Kopien der Wärme-Schlange, Scheren, Faden; Heizung einschalten</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "5'", "Bild eines Heißluftballons zeigen: „Wie kommt der Ballon in die Luft?“ Vermutungen sammeln und für später festhalten.",
         "Sitzkreis", "Bild Heißluftballon"),
        ("Erarbeitung I", "15'", "<b>V9 Was passiert mit Luft, wenn sie warm wird?</b> L gießt das warme Wasser ein. Erst ins warme, dann ins kalte Wasser. "
         "Beobachtung in die vorgezeichneten Flaschen malen.", "PA", "Flasche, Ballon, 2 Schüsseln, S. 13"),
        ("Erarbeitung II", "17'", "<b>V10 Die Wärme-Schlange:</b> anmalen, ausschneiden, Faden befestigen, über der Heizung testen. "
         "Tipp: Ausmalen und Ausschneiden vorher in Kunst oder als Hausaufgabe erledigen.", "EA", "Kopiervorlage, Schere, Faden, S. 14"),
        ("Sicherung", "8'", "Lückentexte. Zurück zum Heißluftballon: „Warme Luft steigt nach oben.“ Merksatz an die Tafel.", "Plenum", "Merksatz 5"),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0">Beim Erwärmen bewegen sich die Luftteilchen schneller und brauchen mehr Platz: Die Luft dehnt sich aus, der Ballon richtet sich auf.
Beim Abkühlen zieht sie sich wieder zusammen. Warme Luft ist dadurch leichter als die kalte Luft um sie herum und steigt nach oben.
Über der Heizung entsteht so ein aufsteigender Luftstrom, der die Spirale dreht. Beim Heißluftballon erhitzt ein Brenner die Luft im Ballon.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Den Ballon vorher einmal aufblasen (vordehnen). Je größer die Flasche (z. B. 1,5 l), desto deutlicher der Effekt.</li>
<li>Das Wasser nicht heißer als ca. 50 °C machen: Dünne PET-Flaschen verformen sich sonst, und es besteht Verbrühungsgefahr.</li>
<li>Den Faden ca. 30–40 cm lang machen und die Schlange ruhig halten.</li>
<li><b>Heizung aus?</b> Dann hält die Lehrkraft die Schlange zur Vorführung mit mindestens 30 cm Abstand über ein brennendes Teelicht.</li>
<li><b>Für schnelle Kinder:</b> Expertenkarte 7 „Die hüpfende Münze“ (Glasflasche vorher 1 Stunde in den Kühlschrank oder 10 Minuten ins Gefrierfach legen).</li></ul></div>
</div>
<p class="merksatz">Merksatz: Warme Luft dehnt sich aus und steigt nach oben.</p>
</div>''')
    # Stunde 6
    h.append('<div class="std stunde">' + stunde_kopf(6, "Wir brauchen Luft", "S. 15–18 + Urkunde"))
    h.append('''
<div class="zwei"><div>
<h3>Ziele</h3>
<p>Die Kinder …</p>
<ul><li>erfahren, dass sie Luft zum Leben brauchen und bei Bewegung mehr Luft brauchen,</li>
<li>erkennen, dass Luft verschmutzt sein kann, und nennen, was der Luft hilft,</li>
<li>schätzen ihren eigenen Lernzuwachs ein.</li></ul>
</div><div>
<h3>Vorbereitung (ca. 5 Min.)</h3>
<ul><li>Uhr oder Stoppuhr, Taschenlampe(n), Verdunkelung prüfen</li>
<li>Forscher-Urkunden ausfüllen und unterschreiben</li>
<li>evtl. Staubfänger-Karten aus Stunde 1 und Lupen</li></ul>
</div></div>
''' + verlauf([
        ("Einstieg", "3'", "Alle sind ganz still. Die Kinder halten eine Hand vor den Mund und spüren ihren Atem: „Was spürt ihr?“", "Plenum", ""),
        ("Erarbeitung I", "12'", "<b>V11 Atem-Detektive:</b> L gibt Start und Stopp (30 Sekunden). Die Kinder zählen ihre Atemzüge. "
         "Dann 1 Minute Hampelmann und noch einmal zählen.", "EA / PA", "Uhr, S. 15"),
        ("Erarbeitung II", "10'", "<b>V12 Ist die Luft immer sauber?</b> Raum verdunkeln, L leuchtet: Staub tanzt im Lichtstrahl. "
         "Gespräch: Was ist gut für saubere Luft? Bilder grün oder rot anmalen. Lüften im Klassenzimmer besprechen.",
         "Plenum, EA", "Taschenlampe, S. 16"),
        ("Abschluss", "17'", "Luft-Quiz mit Lösungswort (S. 17), Rückblick mit Smileys (S. 18). Alle Merksätze an der Tafel noch einmal lesen. "
         "Feierliche Übergabe der Forscher-Urkunden.", "EA, Plenum", "S. 17–18, Urkunden"),
        ("Ausklang", "3'", "Letzte Sterne im Fahrplan anmalen.", "", ""),
    ]) + '''
<div class="zwei">
<div class="kasten"><h3>Sachinformation</h3>
<p style="margin:0">Beim Einatmen gelangt Luft in die Lunge. Der Körper entnimmt ihr Sauerstoff und gibt Kohlenstoffdioxid ab.
Bei Bewegung brauchen die Muskeln mehr Sauerstoff, deshalb atmen wir schneller und tiefer. Grundschulkinder atmen in Ruhe
etwa 15- bis 25-mal pro Minute. Fische nehmen den im Wasser gelösten Sauerstoff mit den Kiemen auf. Pflanzen brauchen Kohlenstoffdioxid und
geben bei Licht Sauerstoff ab. Staub und Abgase aus Verkehr, Heizungen und Industrie verschmutzen die Luft.
Regelmäßiges Stoßlüften (im Unterricht etwa alle 20 Minuten) sorgt für frische Luft im Klassenzimmer.</p></div>
<div class="kasten gelb"><h3>Damit es klappt</h3>
<ul style="margin:0"><li>Die Kinder zählen am besten ihre eigenen Atemzüge mit der Hand auf dem Bauch und geschlossenen Augen.
Die Zahlen schwanken stark. Es kommt auf den Vergleich an, nicht auf die genaue Zahl.</li>
<li>Staub im Licht: Am deutlichsten wird es mit einem Sonnenstrahl durch einen Spalt im Rollo oder einer hellen Taschenlampe.
Ein kurz ausgeschüttelter Pullover verstärkt den Effekt.</li>
<li><b>Für schnelle Kinder:</b> Expertenkarte 8 „Der Hauch-Test“.</li></ul></div>
</div>
<p class="merksatz">Merksatz: Wir alle brauchen saubere Luft zum Leben.</p>
</div>''')

    # Lösungen
    loes = [
        ("V1 (S. 5)", "Die Tüte bleibt dick. – Luft · sehen · spüren · überall"),
        ("V2 (S. 6)", "Pusten: ja · Kreide: ja · Schwamm: ja · Radiergummi: nein (höchstens einzelne Bläschen) – Bläschen · Luft · überall"),
        ("V3 (S. 7)", "Das Taschentuch bleibt trocken. – trocken · Luft · Platz · Wasser"),
        ("V4 (S. 8)", "Der Ballon bleibt klein. – klein · Luft · Platz. Profi-Versuch: Mit Loch wird der Ballon groß; "
                      "hält man das Loch zu, bleibt er groß."),
        ("V5 (S. 9)", "Luft: ja (ein Stück weit) · Wasser: nein · Der Kolben springt zurück. – zusammendrücken · Feder · Wasser"),
        ("V6 (S. 10)", "Der Ball mit viel Luft springt höher. Mit Luft gefüllt: Fahrrad(reifen), Ball, Luftmatratze, Schwimmring "
                       "(nicht: Stein, Buch). – Luft · prall · höher"),
        ("V7 (S. 11)", "Die Rakete saust los. – heraus · vorne · antreiben"),
        ("V8 (S. 12)", "Die Papierkugel ist zuerst unten. – langsam · bremst · Fallschirm"),
        ("V9 (S. 13)", "Im warmen Wasser richtet sich der Ballon auf und wird etwas dicker, im kalten Wasser wird er wieder schlapp. – aus · Platz · zusammen"),
        ("V10 (S. 14)", "Die Schlange dreht sich. – warm · oben · Drehen"),
        ("V11 (S. 15)", "Nach dem Hampelmann atmen wir schneller. – ein · aus · Luft · Leben"),
        ("V12 (S. 16)", "Man sieht kleine Staubkörnchen. Grün: zu Fuß gehen, Rad fahren, Bäume pflanzen, lüften. "
                        "Rot: Auto-Motor laufen lassen, viel Rauch. – Staub · Luft · Fuß · Fahrrad"),
        ("Quiz (S. 17)", "1 falsch (L) · 2 richtig (U) · 3 richtig (F) · 4 falsch (T) · 5 richtig (B) · 6 richtig (A) · "
                         "7 richtig (L) · 8 falsch (L) · 9 falsch (O) · 10 richtig (N) → Lösungswort: <b>LUFTBALLON</b>"),
    ]
    h.append('<h2 style="break-before: page">6. Lösungen zum Forscherheft</h2><table class="t loesung">'
             + "".join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in loes) + '</table>')
    h.append('''
<h2>7. Ideen zum Weiterarbeiten</h2>
<div class="zwei"><div>
<ul>
<li><b>Wetter:</b> Windrad oder Windsack bauen und auf dem Schulhof testen: Woher kommt der Wind, wie stark ist er?</li>
<li><b>Seifenblasen:</b> Luft in einer dünnen Hülle wird sichtbar.</li>
<li><b>Luft hat Gewicht:</b> Balkenwaage mit zwei aufgeblasenen Luftballons, dann einen vorsichtig anstechen.</li>
<li><b>Feuer braucht Luft</b> (nur als Lehrerversuch): Ein Glas über ein Teelicht stülpen, die Flamme erlischt. Das ist ein Ausblick auf Jgst. 3/4.</li>
</ul></div><div>
<ul>
<li><b>Deutsch:</b> Wind-Wörter sammeln (pusten, wehen, säuseln, stürmen), ein Elfchen zum Thema „Luft“ schreiben.</li>
<li><b>Kunst:</b> Pustebilder: flüssige Farbe mit dem Strohhalm über das Blatt pusten.</li>
<li><b>Musik:</b> Luft macht Töne (Flaschenorgel, Blasinstrumente).</li>
<li><b>Mathematik:</b> Raketen-Flugweiten in Schritten und Metern messen und vergleichen.</li>
</ul></div></div>
<div class="kasten gruen"><p style="margin:0"><b>Hinweis zur Bewertung:</b> Das Forscherheft eignet sich als Lerndokumentation. Beobachtungskriterien sind z. B.:
Vermutung vor dem Versuch angekreuzt, sorgfältig beobachtet und gemalt, Ergebnis richtig formuliert, im Team zusammengearbeitet.
Die Selbsteinschätzung auf S. 18 kann Grundlage für ein kurzes Lerngespräch sein.</p></div>
''')
    return ('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Lehrerhandreichung Luft</title>'
            f'<style>{PLAN_CSS}</style></head><body>' + "\n".join(h) + '</body></html>')


# ---------------------------------------------------------------------------- Kopiervorlagen (feste Seiten)

KV_CSS = HEFT_CSS + """
.kvkopf { display: flex; justify-content: space-between; align-items: center; font-size: 10pt; color: var(--muted); }
.kvkopf b { color: var(--blue); }
.half { height: 135mm; position: relative; display: flex; flex-direction: column; }
.schnitt { border-top: 0.5mm dashed #9aa8b4; margin: 3mm -14mm; position: relative; }
.schnitt span { position: absolute; left: 12mm; top: -3.4mm; background: #fff; padding: 0 1.5mm; font-size: 10pt; color: #9aa8b4; }
.brief { font-size: 12pt; line-height: 1.45; }
.brief h2 { font-size: 16pt; color: var(--blue); margin: 2mm 0 2mm; }
.brief .zeile { display: flex; gap: 3mm; align-items: flex-end; margin-top: 4mm; }
.brief .zeile .strich { flex: 1; border-bottom: 0.4mm solid var(--ink); height: 7mm; }
.brief ul { list-style: none; padding: 0; margin: 2mm 0; }
.brief li { margin: 1.2mm 0; }
.karte { height: 131mm; border: 0.7mm solid #e8c64a; border-radius: 5mm; padding: 4mm 5mm 3mm; background: #fffdf3;
  display: flex; flex-direction: column; position: relative; overflow: hidden; font-size: 12.8pt; line-height: 1.28; }
.karte .kk { display: flex; justify-content: space-between; align-items: center; }
.karte .kk .badge { background: #d99a1e; color: #fff; border-radius: 6mm; padding: 0.5mm 3.5mm; font-weight: 700; font-size: 11pt; }
.karte .kk .st { font-size: 10.5pt; color: var(--muted); font-weight: 700; }
.karte h2 { font-size: 18pt; margin: 0.5mm 0 1.2mm; display: flex; align-items: center; gap: 2.5mm; }
.karte h2 .bild { width: 16mm; height: 14mm; margin-left: auto; flex: none; }
.karte h2 .ico { width: 10mm; height: 10mm; }
.karte .spalten { display: grid; grid-template-columns: 1fr 1.6fr; gap: 4mm; }
.karte .mliste { margin: 0; padding-left: 4.5mm; font-size: 12pt; }
.karte .mliste li { margin: 0.6mm 0; }
.karte ol.steps li { margin: 0.6mm 0; }
.karte .was { margin-top: 2mm; border-top: 0.4mm solid #ecd9a0; padding-top: 1.5mm; }
.karte .kopfueber { margin-top: auto; transform: rotate(180deg); font-size: 10.5pt; color: #5d6c78; background: #fff6d6;
  border-radius: 3mm; padding: 1.5mm 3mm; line-height: 1.3; }
.karte .kopfueber b { color: #9a6b00; }

.schlangen { display: flex; flex-direction: column; justify-content: space-between; align-items: center; height: 100%; }
.schlangen svg { width: 182mm; height: 120mm; }
.schlangen .hinweis { font-size: 11pt; color: var(--muted); text-align: center; }
.merk { height: 84mm; border: 0.8mm solid var(--sky2); border-radius: 6mm; display: flex; align-items: center; gap: 7mm;
  padding: 0 9mm; margin-bottom: 4mm; background: #fff; }
.merk .nr { font-size: 15pt; font-weight: 700; color: #fff; background: var(--blue); border-radius: 50%; width: 13mm; height: 13mm;
  display: flex; align-items: center; justify-content: center; flex: none; }
.merk .txt { font-size: 31pt; font-weight: 700; line-height: 1.15; }
.merk .lu { width: 34mm; height: 28mm; flex: none; margin-left: auto; }
.urkunde { border: 2.2mm double var(--blue); border-radius: 6mm; height: 100%; padding: 10mm 12mm; display: flex; flex-direction: column;
  align-items: center; text-align: center; position: relative; }
.urkunde .u1 { font-size: 15pt; color: var(--muted); letter-spacing: 1mm; }
.urkunde .u2 { font-size: 40pt; font-weight: 700; color: var(--blue); line-height: 1.1; margin: 2mm 0 4mm; }
.urkunde .name { width: 130mm; border-bottom: 0.6mm solid var(--ink); height: 16mm; margin: 4mm 0 6mm; }
.urkunde .txt { font-size: 15pt; line-height: 1.45; max-width: 150mm; }
.urkunde .liste { text-align: left; font-size: 13.5pt; margin: 4mm 0; line-height: 1.5; }
.urkunde .bild { width: 150mm; height: 62mm; }
.urkunde .unter { display: flex; gap: 14mm; width: 150mm; margin-top: auto; font-size: 11pt; color: var(--muted); }
.urkunde .unter div { flex: 1; border-top: 0.4mm solid var(--ink); padding-top: 1mm; }
"""


def kv_kopf(nr, titel):
    return f'<div class="kvkopf"><span><b>Kopiervorlage {nr}</b> · {titel}</span><span>Forscherheft Luft · Klasse 2</span></div>'


def elternbrief():
    teil = '''<div class="half brief">
<h2>Liebe Eltern,</h2>
<p style="margin:0 0 2mm">in den nächsten Wochen erforschen wir im Heimat- und Sachunterricht das Thema <b>„Luft“</b>.
Dafür machen die Kinder viele kleine Versuche. Bitte geben Sie Ihrem Kind bis zum <span style="display:inline-block;width:32mm;border-bottom:0.4mm solid #24323f"></span> mit
(bitte alles mit Namen beschriften):</p>
<ul>
<li><span class="ck"></span>1 leere, saubere Plastikflasche (0,5 Liter)</li>
<li><span class="ck"></span>1 durchsichtiges Glas oder einen stabilen, durchsichtigen Plastikbecher</li>
<li><span class="ck"></span>wenn vorhanden: 1 Schüssel (wir brauchen etwa 12 Stück)</li>
</ul>
<p style="margin:1mm 0">Wir verwenden Luftballons. Diese enthalten meist Latex. Bitte geben Sie den Abschnitt unten ausgefüllt zurück.</p>
<p style="margin:1mm 0">Vielen Dank für Ihre Unterstützung!</p>
<div class="zeile"><span>Ihre Klassenleitung:</span><span class="strich"></span></div>
<div style="margin-top:auto;border-top:0.4mm dashed #9aa8b4;padding-top:2mm;font-size:11.5pt">
<b>Rückmeldung</b> · Name des Kindes: <span style="display:inline-block;width:52mm;border-bottom:0.4mm solid #24323f"></span><br>
Mein Kind hat <span class="ck"></span>keine Latexallergie <span class="ck"></span>eine Latexallergie.
Unterschrift: <span style="display:inline-block;width:42mm;border-bottom:0.4mm solid #24323f"></span>
</div>
</div>'''
    return (f'<section class="page">{kv_kopf(1, "Elternbrief (2 pro Seite)")}{teil}'
            f'<div class="schnitt"><span>✂ hier abschneiden</span></div>{teil}</section>')


def schlange_svg():
    R, r0, pitch = 60.0, 8.5, 10.3
    cx = cy = 64.0
    b = pitch / (2 * math.pi)
    th_max = (R - r0) / b
    pts = []
    n = 900
    for i in range(n + 1):
        th = th_max * i / n
        r = r0 + b * th
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
    d = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts)
    s = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#ffffff" stroke="#24323f" stroke-width="0.6"/>'
    s += f'<path d="{d}" stroke="#24323f" stroke-width="0.6" fill="none"/>'
    # Muster (Punkte) zum Anmalen
    th = 2.2
    while th < th_max - 0.6:
        r = r0 + b * th + pitch / 2
        if r < R - 2.5:
            s += (f'<circle cx="{cx + r*math.cos(th):.2f}" cy="{cy + r*math.sin(th):.2f}" r="1.3" '
                  f'fill="none" stroke="#9aa8b4" stroke-width="0.35"/>')
        th += 9.5 / max(r, 1)
    # Kopf
    s += (f'<circle cx="{cx-2.6}" cy="{cy-2.2}" r="1.5" fill="#24323f"/><circle cx="{cx+2.6}" cy="{cy-2.2}" r="1.5" fill="#24323f"/>'
          f'<path d="M{cx-2.4} {cy+2.4} Q{cx} {cy+4.2} {cx+2.4} {cy+2.4}" stroke="#24323f" stroke-width="0.5" fill="none"/>'
          f'<circle cx="{cx}" cy="{cy+6.5}" r="0.9" fill="#d9534f"/>')
    # Startmarke außerhalb des Kreises
    a = th_max % (2 * math.pi)
    sx, sy = cx + R * math.cos(a), cy + R * math.sin(a)
    lx, ly = cx + (R + 5) * math.cos(a), cy + (R + 5) * math.sin(a)
    s += f'<circle cx="{sx:.2f}" cy="{sy:.2f}" r="1.6" fill="#d9534f"/>'
    anchor = "start" if math.cos(a) >= 0 else "end"
    s += (f'<text x="{lx:.1f}" y="{ly+1.2:.1f}" font-size="4" font-weight="700" text-anchor="{anchor}" fill="#d9534f">'
          f'✂ hier anfangen</text>')
    return f'<svg viewBox="-36 -2 200 132" xmlns="http://www.w3.org/2000/svg">{s}</svg>'


def _schere_inner():
    return (f'<g fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">'
            + schere() + '</g>')


def kv_schlange():
    sv = schlange_svg()
    return (f'<section class="page">{kv_kopf(2, "Wärme-Schlange zu Versuch 10 (2 pro Seite)")}'
            f'<div class="schlangen grow">{sv}<div class="hinweis">Erst den Kreis ausschneiden, dann immer an der Linie entlang bis zum Kopf. '
            f'Mit dem Bleistift ein Loch in die Mitte stechen und den Faden verknoten.</div>{sv}</div></section>')


EXPERTEN = [
    (1, 2, "Kannst du Luft umfüllen?", ["2 Gläser", "1 große Schüssel mit Wasser"],
     ["Tauche Glas 1 ganz unter Wasser, bis es voll ist.",
      "Drehe Glas 1 unter Wasser um. Hebe es ein Stück hoch. Der Rand bleibt im Wasser!",
      "Drücke Glas 2 mit der Öffnung nach unten gerade ins Wasser. Darin ist Luft.",
      "Kippe Glas 2 langsam unter Glas 1."],
     "Was passiert mit der Luft?",
     "Die Luft blubbert nach oben in Glas 1. Luft ist leichter als Wasser und steigt nach oben. Sie braucht Platz und drückt das Wasser aus dem Glas.",
     glas(True)),
    (2, 3, "Der Wasser-Zaubertrick", ["1 Glas", "1 Postkarte oder Bierdeckel", "Wasser", "1 Schüssel"],
     ["Fülle das Glas bis zum Rand mit Wasser.",
      "Lege die Karte auf das Glas.",
      "Halte die Karte fest. Drehe das Glas über der Schüssel um.",
      "Nimm die Hand ganz vorsichtig weg."],
     "Was passiert mit dem Wasser?",
     "Das Wasser bleibt im Glas! Die Luft drückt von unten gegen die Karte und hält sie fest.",
     glas(True)),
    (3, 3, "Die Strohhalm-Pipette", ["1 Strohhalm", "1 Glas mit Wasser", "1 leeres Glas"],
     ["Stecke den Strohhalm ins Wasser.",
      "Halte oben mit dem Finger fest zu.",
      "Hebe den Strohhalm über das leere Glas.",
      "Nimm den Finger weg."],
     "Was passiert, wenn du zuhältst? Was passiert, wenn du loslässt?",
     "Solange du zuhältst, drückt die Luft von unten gegen das Wasser. Es bleibt im Strohhalm. "
     "Lässt du los, drückt die Luft auch von oben, und das Wasser läuft heraus.",
     strohhalm()),
    (4, 4, "Puste-Test: Was kann die Luft bewegen?", ["1 Strohhalm", "Feder oder Watte", "Papierkugel", "Radiergummi", "Bleistift", "Murmel"],
     ["Lege die Dinge nacheinander auf den Tisch.",
      "Vermute: Kannst du es wegpusten?",
      "Puste mit dem Strohhalm dagegen.",
      "Male einen Smiley, wenn es geklappt hat."],
     "Was konntest du wegpusten?",
     "Leichte Dinge kann die Luft leicht bewegen. Für schwere Dinge braucht man viel mehr Wind. Runde Dinge rollen leichter.",
     feder()),
    (5, 4, "Baue einen Fallschirm!", ["1 Stück Plastiktüte (ca. 30 × 30 cm)", "4 Fäden (je ca. 25 cm)", "Klebestreifen", "2 Büroklammern"],
     ["Klebe an jede Ecke einen Faden.",
      "Knote die 4 Fäden unten zusammen.",
      "Hänge eine Büroklammer an den Knoten.",
      "Lass den Fallschirm und die zweite Büroklammer gleichzeitig fallen."],
     "Was ist zuerst unten?",
     "Die Büroklammer ohne Fallschirm ist zuerst unten. Der Fallschirm fängt viel Luft, und die Luft bremst ihn.",
     fallschirm()),
    (6, 4, "Das Puste-Boot", ["1 Korken", "1 Zahnstocher", "1 kleines Papier-Segel", "1 Schüssel mit Wasser", "1 Strohhalm"],
     ["Stecke den Zahnstocher oben und unten durch das Segel.",
      "Stecke den Zahnstocher in den Korken.",
      "Setze das Boot auf das Wasser.",
      "Puste mit dem Strohhalm gegen das Segel."],
     "Was passiert mit dem Boot?",
     "Die bewegte Luft drückt gegen das Segel und treibt das Boot an. So fahren auch echte Segelboote.",
     schuessel()),
    (7, 5, "Die hüpfende Münze", ["1 Glasflasche aus dem Kühlschrank", "1 Münze", "etwas Wasser"],
     ["Mache den Rand der Flaschenöffnung mit Wasser nass.",
      "Lege die Münze auf die Öffnung.",
      "Umfasse die Flasche mit beiden Händen.",
      "Warte ganz still und schau genau hin."],
     "Was macht die Münze?",
     "Die Münze klappert und hüpft! Deine warmen Hände wärmen die Luft in der Flasche. Warme Luft dehnt sich aus und drückt die Münze kurz hoch.",
     muenze()),
    (8, 6, "Der Hauch-Test", ["1 Taschenspiegel oder 1 Löffel"],
     ["Hauche den Spiegel mit offenem Mund an.",
      "Schau genau hin: Was siehst du?",
      "Hauche in deine Hand. Puste dann mit spitzem Mund in die Hand.",
      "Was fühlt sich wärmer an?"],
     "Was passiert mit dem Spiegel?",
     "Der Spiegel beschlägt. Unsere Atemluft ist warm und feucht. Am kalten Spiegel werden daraus winzige Wassertröpfchen. "
     "Hauchen fühlt sich warm an, Pusten kühler.",
     kind("bauch")),
]


def karte(nr, stunde, titel, material, schritte, frage, loesung, bild):
    ml = "".join(f"<li>{m}</li>" for m in material)
    st = "".join(f"<li>{x}</li>" for x in schritte)
    return f'''<div class="karte">
<div class="kk"><span class="badge">★ Expertenkarte {nr}</span><span class="st">für Stunde {stunde}</span></div>
<h2>{icon_box(stern("#ffe27a"))}{titel}<span class="bild">{svg(bild)}</span></h2>
<div class="spalten">
<div>{kopf(ICON_MATERIAL, "Das brauchst du:")}<ul class="mliste">{ml}</ul></div>
<div>{kopf(ICON_VERSUCH, "So geht es:")}<ol class="steps">{st}</ol></div>
</div>
<div class="was"><b>{frage}</b> Erzähle es deinem Partnerkind oder schreibe es auf.<div style="height:1.5mm"></div>{lineatur(1)}</div>
<div class="kopfueber"><b>Weißt du, warum?</b> {loesung}</div>
</div>'''


def kv_experten():
    out = []
    for i in range(0, len(EXPERTEN), 2):
        a, b = EXPERTEN[i], EXPERTEN[i + 1]
        out.append(f'<section class="page">{kv_kopf(3 + i // 2, "Expertenkarten (laminieren und ausschneiden)")}'
                   f'{karte(*a)}<div class="schnitt"><span>✂</span></div>{karte(*b)}</section>')
    return out


MERKSAETZE = [
    "Luft ist überall. Man kann sie nicht sehen, aber spüren.",
    "Luft braucht Platz.",
    "Luft kann man zusammendrücken.",
    "Luft kann Dinge antreiben und bremsen.",
    "Warme Luft dehnt sich aus und steigt nach oben.",
    "Wir alle brauchen saubere Luft zum Leben.",
]


def kv_merksaetze():
    lu = svg(lufti(), vb="4 18 92 74")
    out = []
    for p in range(2):
        strips = "".join(f'<div class="merk"><span class="nr">{p*3+i+1}</span><span class="txt">{MERKSAETZE[p*3+i]}</span>'
                         f'<span class="lu">{lu}</span></div>' for i in range(3))
        out.append(f'<section class="page">{kv_kopf(7 + p, "Merksätze für die Tafel")}<div style="margin-top:4mm">{strips}</div></section>')
    return out


def kv_urkunde():
    bild = (place(wolke(), 0, 10, 0.6) + place(ballon("#ffe27a"), 40, 0, 0.8, rot=-8) + place(ballon("#9ccbf0"), 70, -6, 0.9)
            + place(lufti(), 110, 0, 1.0) + place(ballon("#ff9f9f"), 200, -2, 0.85, rot=8) + place(windrad(), 236, 4, 0.8)
            + place(wolke(), 280, 12, 0.55))
    return f'''<section class="page">{kv_kopf(9, "Forscher-Urkunde")}
<div class="urkunde grow" style="margin-top:3mm">
<div class="u1">URKUNDE</div>
<div class="u2">Luft-Forscher-Diplom</div>
<div class="bild">{svg(bild, vb="0 -8 340 112")}</div>
<div class="txt">für</div>
<div class="name"></div>
<div class="txt">Du hast die Luft erforscht und viele Versuche geschafft. Jetzt weißt du:</div>
<div class="liste">★ Luft ist überall und braucht Platz.<br>
★ Luft kann man zusammendrücken.<br>
★ Luft kann Dinge antreiben und bremsen.<br>
★ Warme Luft steigt nach oben.<br>
★ Wir alle brauchen saubere Luft.</div>
<div class="txt"><b>Herzlichen Glückwunsch!</b></div>
<div class="unter"><div>Datum</div><div>Unterschrift</div></div>
</div></section>'''


def build_kopiervorlagen():
    pages = [elternbrief(), kv_schlange()] + kv_experten() + kv_merksaetze() + [kv_urkunde()]
    return ('<!DOCTYPE html><html lang="de"><head><meta charset="utf-8"><title>Kopiervorlagen Luft</title>'
            f'<style>{KV_CSS}</style></head><body>' + "\n".join(pages) + '</body></html>')
