# Mods nach einem CK3-Spielupdate prüfen und anpassen

Verbindlicher Ablauf für neue Chats, eingeführt am **2026-10-03**. Einstieg: [Documentation](../README.md), [Mod-Prüfblätter](../update-readiness/README.md), [Vanilla-Historie](../reference/vanilla-history.md). Die Regeln in [AGENTS.md](../../AGENTS.md) bleiben maßgeblich.

## Auftrag und Grenzen

**„Prüfe, ob Mod X ein Update benötigt“ autorisiert die Prüfung und die daraus belegbar notwendigen, gezielten Code- und Dokumentationskorrekturen.** Nicht bei einem weiteren Plan stehen bleiben. Vor einer fachlichen Implementierungsentscheidung den vollständigen Audit der betroffenen Funktion abschließen. Eindeutige, belegte Anpassungen selbstständig umsetzen; keine spekulative Änderung an unbekannten Engine-Verträgen.

Bestehende Modabsichten, Zahlenwerte, Kategorien, Kommentare, Namen, Workshop-IDs und Benutzeränderungen erhalten. Eine wesentlich andere Verhaltensentscheidung oder große Umstrukturierung erfordert weiterhin die Rückfrage gemäß AGENTS.md. Keine Mod-Veröffentlichung, Toolinstallation, Änderung der Spielinstallation oder ungefragte Ausweitung auf andere Distributionen. Die unabhängigen Knight-Manager-Pakete und `test` bleiben ausgeschlossen. Eine eigenständige Mod zu prüfen autorisiert keine automatische Übertragung in SerpInteractionsDecisions.

Notwendige Codekorrekturen auch dann abschließen, wenn Spieltests nicht ausführbar sind. Tests konkret als ausstehend dokumentieren. Eine Kompatibilitätsfreigabe und entsprechende `supported_version`-/Release-Metadatenänderungen erst nach den vorgeschriebenen Tests durchführen; eine explizit anderslautende Nutzeranweisung geht vor und muss als Zieldeklaration von Testergebnissen getrennt werden.

## Ablauf bei jedem Auftrag

1. **Aktuellen Zustand erfassen.** `git status --short`, vollständigen relevanten Diff und tatsächliche Dateien lesen. Vorhandene Benutzeränderungen von eigenen Änderungen unterscheiden. Prüfsummen inventarisieren; vor einem Eingriff Sicherung oder nachvollziehbaren ursprünglichen Stand erhalten. Ein Hash ist keine wiederherstellbare Sicherung. Kein Reset, Stash, Checkout-Wechsel oder Überschreiben fremder Arbeit.
2. **Versionen und Modvariante bestimmen.** Installierte Version aus `launcher/launcher-settings.json` neu lesen, beide Moddeskriptoren prüfen und letzte Quellen-/Spielteststände im Prüfblatt feststellen. Eine alte `supported_version` ist kein bewiesener Scriptfehler. Bei mehreren plausiblen Distributionen erst deren tatsächlichen Umfang klären.
3. **Update-Vergleich ausführen.** Den unten beschriebenen lesenden Check mit der ausgewählten Mod starten. Ergebnis vollständig lesen: Objektänderungen, Änderungen außerhalb der Objekte, Aufrufer/Helfer, Assets, lokale Änderungen, fehlende Referenzen und Engine-Export-Frische sind getrennte Befunde. Bei geändertem Spielstand selbst bei unveränderten Dateien die relevanten Engine-Verträge und Regressionstests prüfen.
4. **Feature-Audit abschließen.** Aktuelle komplette Definitionen und `.info`-Verträge, alle Aufrufer, Parameterbindungen und transitive Helfer lesen. Root/Actor/Recipient/Puppet, optionale Ziele, Kosten, unmittelbare/Antwort-/Nachlauf-Effekte, reine Tooltips, Callback-/Listen-/Delay-Lebenszyklus, DLC-/Regierungsbedingungen und GUI-/Localization-Verbraucher nachvollziehen. Aktuelle Exporte mit `Documentation/tools/lookup.py SYMBOL --context 4` heranziehen. Ein Fund oder fehlender Fund beweist keinen vollständigen Vertrag. Neue Spielversionen benötigen frische relevante Exportnachweise; alte Exporte nicht als neue ausgeben.
5. **Entscheidung je Befund dokumentieren.** „Codeanpassung erforderlich“, „Quellenänderung ohne notwendige Codeanpassung“ oder „Vertrag noch ungeklärt“, jeweils mit Ursache und betroffenen Funktionen. Bloße neue Features sind kein Auftrag zur Erweiterung der Mod. Reine Textänderungen können bei einem Override absichtlich nicht übernommen werden; diese Entscheidung begründen.
6. **Gezielt umsetzen und prüfen.** Notwendige belegte Korrekturen durchführen, bestehende Struktur erhalten. Scriptstruktur, IDs, Lademechanismus, Localization, BOM und bestehende Codierung/Zeilenenden prüfen; neue Textdateien gemäß Konvention schreiben. Geeignete bestehende Werkzeuge vorher auf feste Versionen, Schreibwirkungen und historische Baselines prüfen. Quellen-Audit, statische Prüfung, externer Validator und tatsächlicher Spieltest separat ausweisen.
7. **Regressionen ausführen oder offenhalten.** Passende Fälle aus dem Mod-Prüfblatt testen: erfolgreiche/abgelehnte Aktionen, Grenzwerte, fehlende Ziele, wiederholte Ausführung, Kosten/Belohnungen, AI, Save/Reload und bei Bedarf zwei Spieler. Für Event-Overrides vollständigen Neustart; Hot Reload reicht nicht. Frische Logs von vorhandenen Fehlern unterscheiden. Keine tatsächlich nicht ausgeführten Tests als bestanden melden.
8. **Nachweise und Wartungsstand ergänzen.** Neuen datierten Bericht mit Vorher/Nachher, Versionen, Quellen, SHA-256, Auswirkungen, geänderten Dateien und offenen Tests anlegen. Prüfblatt, Verträge und aktuelle Übersichten aktualisieren. Erst nach dem relevanten Quellen-Audit die ausgewählten Watch-Baselines als neuen Stand ergänzen. Historische Berichte, Roh-Exporte und alte Baselines unverändert behalten. Im Abschluss nötige Änderungen, durchgeführte Prüfungen und verbleibende Grenzen nennen.

## Vergleichswerkzeug

[check_mod_updates.py](../tools/check_mod_updates.py) liest standardmäßig nur. Es startet kein Spiel, installiert nichts, holt keine Netzwerkdaten, erzeugt keine Dateien und schreibt keine Baselines oder Modpatches. Exakte registrierte Namen mit Leerzeichen übergeben:

    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/check_mod_updates.py --mod 'Mass Demand Conversion'
    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/check_mod_updates.py --mod 'Leave Wars' --mod 'SerpAlerts' --json
    & 'D:\CDesktopLink\Portable\Python\WinPy64\python\python.exe' Documentation/tools/check_mod_updates.py --all --json

`--all` prüft die acht registrierten Distributionen, keine ausgeschlossenen Pakete, und autorisiert keine Modänderung außerhalb des Nutzerauftrags. `--game` erlaubt einen ausdrücklich gewählten anderen game-Ordner. `--manifest` wählt einen bestimmten datierten Vergleichsstand. Ohne diese Option benennt [update-watch-index.json](../update-readiness/update-watch-index.json) den derzeit maßgeblichen [datierten Stand](../update-readiness/update-watch-20261003.json).

Exitcodes: **0** = kein quellenseitiger Prüfanlass in den registrierten Watches und kein Versions-/Export-/lokaler Drift; **1** = Audit/Prüfung erforderlich; **2** = Vergleich unvollständig, Definition fehlt/ist mehrdeutig oder Auswahl/Eingabe ungültig. Kein Exitcode beweist Laufzeitkompatibilität. Auch bekannte offene Modgates bleiben bei Exitcode 0 offen.

| Befund | Bedeutung und nächster Schritt |
|---|---|
| `unchanged` | Registrierte Quelle/Definition unverändert; bisherige Audit-/Testgrenzen bleiben |
| `format_only` | BOM/Zeilenenden/Whitespace/Kommentare ohne Änderung der erkannten geordneten Script-Tokens; Diff kontrollieren |
| `file_changed_object_unchanged` | Datei geändert, das überwachte Objekt nicht; kein automatischer Eventänderungsalarm. Andere Watches/Helfer und relevante Dateikontexte kontrollieren |
| `object_changed`, `file_changed`, `reference_changed` | Definition, Scriptdatei oder Textvertrag geändert; konkreten Diff lesen und Feature-Audit durchführen |
| `callers_changed` | Script-Aufrufer hinzugefügt/entfernt oder ihr vollständiger Kontext geändert; Empfänger/Scopes/Übergaben neu auditieren |
| `moved_definition` | Definition an anderem Ort gefunden; auch bei gleichen Tokens Zuordnung und Loader-Vertrag neu prüfen |
| `missing_definition`, `ambiguous_definition`, `comparison_incomplete` | Fehlende/mehrdeutige Definition, fehlende Git-Referenz, ungültige Baseline oder nicht lesbare Quelle; nicht als unverändert behandeln |
| `asset_changed` | Binärhash/Header geändert; tatsächliche Verbraucher, Frames, Maße und Rendering prüfen |
| Engine-Referenz veraltet/geändert | Aktuelle relevante Exportnachweise beschaffen und deklarierte Verträge prüfen; unveränderte Scripts allein reichen nicht |
| Lokale Moddateien geändert | Benutzeränderungen und aktuelle Modfunktion gegenüber dem registrierten Stand berücksichtigen; niemals automatisch zurücksetzen |

Der Lexer ist kein vollständiger Jomini-Parser und bewertet keine Gameplay-Semantik. Er erhält Reihenfolge, wiederholte Schlüssel, Strings und Bedingungen; unbekannte/unlesbare Objektsyntax wird als unvollständiger Vergleich ausgewiesen. Direkte `trigger_event = ID` und `trigger_event = { id = ID ... }`-Aufrufer werden erfasst. Dynamische/hartcodierte Engine-Aufrufer sind damit nicht ausgeschlossen. GUI-/Referenzdateien werden überwiegend auf Dateiebene verglichen; Text-Watches erhalten keine behauptete semantische Normalisierung. Bei Binärassets liefern SHA-256 und Header einen Vergleich ohne alte Binärkopie, keinen Pixel-/Rendering-Diff.

## Welche Flächen nach einem Patch besonders wichtig sind

| Oberfläche | Wartungsregel |
|---|---|
| Vollständige native Dateien/Objekte ersetzt | Eigenes gewünschtes Delta auf aktuelle vollständige Vanilla-Basis übertragen; neue native Folgen/Optionen dürfen nicht verloren gehen. Objekt-ID und tatsächlichen Lademechanismus festhalten |
| Native Helfer/Interaktionen delegiert | Caller-, Parameter-, Kosten-, Schutz-, Scope- und Lebenszyklusänderungen beachten, auch wenn kein Modfile direkt überschreibt |
| Engine-Effekte/Trigger/GUI-APIs | Aktuelle Signatur, Typen, erlaubte Kontexte und Semantik nachweisen; fehlende Suchtreffer nicht als Entfernung interpretieren |
| GUI/Localization | Typen, Datacontext, Fensterverbraucher, Texte/Scopes, alle vorhandenen Sprachen und Auswahl-/Klicklogik kontrollieren |
| Assets | Pfad- und Verbraucheränderungen, Symbolzuordnung, Frames, Container/Maße, öffentliche/lokale Varianten und Renderverhalten prüfen |

Die spezifischen Quellen, Absichten, offenen Fragen und Regressionen stehen in den acht [Mod-Prüfblättern](../update-readiness/README.md). Die Watch-Liste ist ein Früherkennungswerkzeug, keine vollständige automatisch bewiesene Abhängigkeitsclosure. Bei neu gefundenen relevanten Abhängigkeiten die Überwachung nach abgeschlossener Quellenprüfung erweitern.

## Baselines erhalten und nach einem Audit fortschreiben

Jedes Element hat Mod/Funktion, `kind`/`surface`, lokale Definitionen, `native_path`, gegebenenfalls `symbol`, `baseline_version`, SHA-256 und `comparison_reference`. Objekt-Watches haben zusätzlich geordnete Token-Prüfsummen; Aufrufer-Watches ein Inventar mit Besitzer-Tokenhash; Assets Originalhash und Header. `audit_scope`, Mod-`coverage` und `open_gates` kennzeichnen tatsächliche Grenzen. Der erste Stand ist **1.20.0.3**, mit Quellenregistrierung für alle acht Mods und dem bereits abgeschlossenen engen MDC-Notification-Audit; keine pauschale semantische Auditfreigabe.

Für einen neuen geprüften Stand ein neues datiertes JSON ausschließlich als neue Datei anlegen. Nur tatsächlich auditierte Watches/Mod-Snapshots erneuern; übrige Einträge einschließlich ihrer eigenen Versionen und Git-Commits erhalten. Pro-Watch-Referenzen erlauben unterschiedliche Prüfstände je Mod. Den neuen Manifeststand gegen aktuelle Quellen und Regressionen prüfen, dann den Indexzeiger und seine Historienliste ausdrücklich ergänzen. Alte Dateien nicht überschreiben oder ihren letzten Prüfstand auf den bloß installierten Patch setzen. Ein sources-geprüfter Stand kann ausstehende Spieltests enthalten, darf aber keine Kompatibilitätsfreigabe behaupten.

Alte Texte aus gepinnten Git-Blobs lesen, ohne den lokalen Checkout umzuschalten oder fremde Skripte auszuführen. Fehlt die Referenz, [Vanilla-Historie](../reference/vanilla-history.md) zur Wiederbeschaffung nutzen; ein fehlender Binärblob im Mirror ist von fehlenden installierten Assets zu unterscheiden. Die neue Prüfung übernimmt keine festen Abbruchbedingungen der alten datierten MDC-Collector. Diese bleiben historische Nachweise und können nach absichtlichen Workspace-Änderungen erwartbar von ihren Erhaltungsbaselines abweichen.

## MDC: vollständige Event-Overrides besonders prüfen

[Aktuelle Umsetzung und Effektzuordnung](../update-readiness/mods/mass-demand-conversion-notifications-20261003.md), [Prüfblatt](../update-readiness/mods/mass-demand-conversion.md), [Spieltests](../update-readiness/mods/mass-demand-conversion-tests.md).

| Moddefinition | Vollständig ersetzte native Definition |
|---|---|
| `Mass Demand Conversion/events/religion_events/accept_conversion_notification.txt` → `religious_interaction.2002` | `events/religion_events/religious_interaction_events.txt` → dieselbe ID |
| `Mass Demand Conversion/events/interaction_events/mdc_house_conversion_notification.txt` → `char_interaction.0181` | `events/interaction_events/character_interaction_events.txt` → dieselbe ID |

Die beiden Overrides ersetzen ganze Eventdefinitionen, keine zusammengeführten Felder. Native neue `immediate`-/Antwort-/`after`-Folgen, neue Entscheidungen und sonstige Bedingungen explizit vergleichen. Eine neue echte Spielerentscheidung darf nicht durch den versteckten Ablauf entfallen; in diesem Fall die wesentlich unterschiedliche Verhaltensentscheidung dem Nutzer vorlegen. Den bisherigen Eventempfänger und alle Actor-/Recipient-/Puppet-Bindungen aus sämtlichen aktuellen Aufrufern nachvollziehen. Der jetzige Empfänger ist `scope:puppet_or_actor`; nicht pauschal auf actor umstellen.

Minister-, Eifer- und Prestigebelohnungen und den nativen Puppet-Notifier unter denselben Bedingungen genau einmal erhalten. Alte Tooltip-Konvertierungsaufrufe bleiben Vorschauen; `send_interface_message` kann enthaltene Effekte ausführen und darf keine zweite Konvertierung/Belohnung verursachen. Konvertierung, Familien-/Secret-Faith-/Studienabläufe bleiben native Aufgaben. Annahme und spätere tatsächliche Konvertierung getrennt erfassen.

Aufrufer, Notifier-Guards, Konvertierungshelfer und deren Werte, Event-Prioritätsvertrag und Nachrichtenschema werden zusätzlich überwacht. Aktuelle IDs gelten für alle nativen Aufrufer, einschließlich manueller Anfragen. Gleiche IDs/Prioritäten anderer Mods können kollidieren. Vollständig neu starten; Hot Reload kann Prioritäten ignorieren. `combine_into_one` verspricht weder Gesamtzahl noch vollständige Empfängerliste. Bei jeder Änderung diese Grenzen und MC-N01–MC-N11 sowie passende MC-T-Fälle erneut prüfen.
