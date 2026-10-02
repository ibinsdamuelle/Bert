# Forscherheft „Luft“ – 2. Klasse (Grundschule Bayern, HSU)

Unterrichtssequenz für **6 Unterrichtsstunden** zum Thema Luft. Alle Versuche brauchen nur Alltagsmaterial,
sind schnell vorbereitet und dauern jeweils 5–15 Minuten.

| Datei | Inhalt | Drucken |
|---|---|---|
| `Forscherheft_Luft_Klasse2.pdf` | Schülerheft, 18 Seiten: Deckblatt, Forscher-Fahrplan, Forscherregeln, 12 Versuche, Quiz, Rückblick | 1× pro Kind (A4, Schwarz-Weiß geht auch) |
| `Lehrerhandreichung_Luft_Klasse2.pdf` | S. 1–11: Lehrplanbezug, Sequenzübersicht, Organisation und Sicherheit, Materialliste, Verlaufsplan jeder Stunde, Lösungen. Danach 9 Kopiervorlagen: Elternbrief, Wärme-Schlange, 8 Expertenkarten, Merksätze für die Tafel, Forscher-Urkunde | Planung für die Lehrkraft, Kopiervorlagen nach Bedarf |

## Die Sequenz

| Stunde | Thema | Versuche |
|---|---|---|
| 1 | Luft ist überall | Luft fangen (Tüte) · Luft sichtbar machen (Strohhalm, Kreide, Schwamm) |
| 2 | Luft braucht Platz | Trockenes Taschentuch im Glas · Ballon in der Flasche |
| 3 | Luft kann man zusammendrücken | Spritze (Luft und Wasser) · Ball-Test |
| 4 | Luft treibt an und bremst | Luftballon-Rakete · Papier-Wettrennen |
| 5 | Warme und kalte Luft | Zauber-Ballon (warmes und kaltes Wasser) · Wärme-Schlange |
| 6 | Wir brauchen Luft | Atem-Detektive · Staub im Lichtstrahl, saubere Luft · Quiz und Urkunde |

Lehrplanbezug: LehrplanPLUS Grundschule Bayern, HSU Jahrgangsstufe 1/2, Lernbereich 3 „Natur und Umwelt“, 3.3 „Luft, Wasser, Wetter“.

## Selbst anpassen

Die PDFs werden aus den Python-Dateien in `quelle/` erzeugt (Texte in `heft.py` und `lehrer.py`, Zeichnungen in
`icons.py` und `illus.py`). Neu erzeugen:

```bash
cd quelle
python3 build.py        # braucht Python 3, Node.js mit Playwright (Chromium) und pdfunite
node check.mjs forscherheft.html   # prüft, ob jede Seite aufs Blatt passt
```

Schrift: [Andika](https://software.sil.org/andika/) (SIL Open Font License, siehe `quelle/fonts/OFL-Andika.txt`).
Sie wurde für Leseanfänger entwickelt und hat z. B. das einfache „a“ und „g“.
