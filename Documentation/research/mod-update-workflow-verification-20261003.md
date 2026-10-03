# Mod-Update-Ablauf: Implementierungsnachweis — 2026-10-03

Der verbindliche Einstieg in [AGENTS.md](../../AGENTS.md) führt zur [allgemeinen Update-Anleitung](../handbook/mod-update-workflow.md). Die acht bestehenden Mod-Prüfblätter enthalten ergänzende Wartungsverträge. Benutzeränderungen, ältere Berichte und bestehende Spieltestgrenzen bleiben erhalten.

## Quellenvergleich und Prüfstand

Der [lesende Checker](../tools/check_mod_updates.py) verwendet den [datierten Quellenstand](../update-readiness/update-watch-20261003.json), ausgewählt über den [Baseline-Index](../update-readiness/update-watch-index.json). Die Vergleichstexte stammen aus gepinnten Git-Blobs des lokalen Vanilla-Mirrors, Commit `0ec13350cde9e410b37a46d3616966838f4ba994`; der Checkout wird nicht umgeschaltet. Binärassets werden über dokumentierte Originalhashes und Header verglichen.

Der vollständige Standardlauf `--all --json` gegen die installierte Version **1.20.0.3** endete mit Exitcode **0**: **491 registrierte Quellen unverändert**, keine lokale Modquellenabweichung und keine Exportabweichung. Ein Vorher/Nachher-Hashvergleich aller Dateien in Documentation und den acht Modpaketen belegt die Schreibfreiheit des Checker-Laufs. Erst der aufrufende Prüfrahmen schrieb anschließend den [Quellenprüfbericht](../update-readiness/evidence/mod-update-source-check-20261003.json).

| Mod | Unveränderte Watches |
|---|---:|
| CustomDefines | 8 |
| Gender Colour | 4 |
| GFX-Mod | 8 |
| GFX-Mod Serp | 377 |
| Leave Wars | 9 |
| Mass Demand Conversion | 40 |
| SerpAlerts | 17 |
| SerpInteractionsDecisions | 28 |

MDC ordnet `religious_interaction.2002` eindeutig `events/religion_events/religious_interaction_events.txt` und `char_interaction.0181` eindeutig `events/interaction_events/character_interaction_events.txt` zu. Beide vollständigen nativen Definitionen sind unverändert. Die Registrierung berücksichtigt außerdem Interaktionen, Aufrufer, Puppet-Notifier, Konvertierungshelfer, Belohnungswerte sowie Event-/Nachrichtenverträge. Der zuvor dokumentierte enge Notification-Audit wurde anhand seiner 14 unveränderten Quellenhashes und der vollständigen Event-/Notifierdefinitionen überprüft. Andere Modregistrierungen sind ausdrücklich Quelleninventare mit offenen fachlichen und Laufzeitgates.

## Werkzeugprüfung

Die [isolierten Fixture-Tests](../tools/test_check_mod_updates.py) bestanden: **33 Tests**. Sie decken unveränderte Definitionen, BOM/Zeilenenden/Kommentare, Änderungen außerhalb des Events, neue Belohnungen/Optionen, Bedingungen, Reihenfolge und wiederholte Schlüssel, Helfer und Aufrufer, verschobene/fehlende/mehrdeutige Definitionen, unlesbare Quellen, fehlende Referenzen, Assets, Versions-/Exportdrift, Modauswahl und Schreibfreiheit ab. Ein echter gepinnter Git-Blob wird auch bei abweichendem Arbeitsbaum korrekt gelesen. CLI-Tests prüfen die Exitcodes 0, 1 und 2.

Ausführung mit dem vorhandenen portablen Interpreter:

    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/test_check_mod_updates.py

Dokumentationslinks, Codierung/Zeilenenden der bearbeiteten Dateien, Python-Syntax und `git diff --check` wurden kontrolliert. Der [Erhaltungsnachweis](mod-update-workflow-verification-20261003.json) vergleicht den Arbeitsstand mit den zu Auftragsbeginn erfassten 1200 Dateien; erlaubt sind ausschließlich die darin aufgeführten Dokumentationsänderungen und neuen Wartungswerkzeuge/Nachweise. Bestehende Moddateien und historische Baselines wurden nicht geändert.

## Grenzen und offene Tests

Ein unveränderter registrierter Quellenstand ist keine Kompatibilitätsfreigabe und kein vollständiger automatischer Abhängigkeitsaudit. Nicht registrierte, dynamische oder Engine-interne Abhängigkeiten bleiben fachlich zu prüfen. Es wurden keine Modanpassungen, Metadatenfreigaben, Installationen oder Hintergrundmonitore vorgenommen. Gameplay-, GUI- und Mehrspielertests sowie gegebenenfalls weitere statische Modprüfungen bleiben gemäß den jeweiligen Prüfblättern offen. Nach zukünftigen Event-Override-Anpassungen ist ein vollständiger Spielneustart vorgeschrieben.
