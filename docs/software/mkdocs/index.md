---
title: "MkDocs"
---

## Entwicklung

Die nachfolgenden Befehle werden im Wurzelverzeichnis des Projektes ausgeführt.

### Python Umgebung

erstellen

```bash
python -m venv venv
```

aktivieren

```bash
source venv/Scripts/activate
```

Pakete installieren

```bash
pip install -r requirements.txt
```

Lokale Ausführung

=== "mit drafts"

    ```bash
    mkdocs serve
    ```

=== "ohne drafts"

    ```bash
    mkdocs serve --clean
    ```

    - Konfiguration von `draft_docs` in der mkdocs.yaml

Mit Auführung des build commands wird der `site` Ordner samt Inhalt erstellt.

## Links

Über das geschweifte Klammernpaar `{}` lassen sich weiter Attribute und CSS-Klassen übergeben.

```markdown title="Standard"
[link](url)
```

```markdown title="Neuer Tab"
[link](url){:target="_blank"}
```

```markdown title="CSS Klasse"
[link](url){.meine-klasse}
```

!!! success "So geht es richtig!"

    **Absoluter Pfad** | (**ohne**: /docs)
    
    - für Referenz auf andere Location (z.B : `docs/topic-x/index.md`)

    - `#!md [Link](/topic-x/index#heading)`

    **Relavtiver Pfad**
    
    - für interne Referenz (passend zum Kontext), zum Beispiel Bilder.

    - `#!md ![image](./images/example.png)`

    **Eingebettete Dateien / Snippets** | (**mit**: /docs)

    - `#!md --8<-- "docs/snippets/topic-x/index.md:section-x"`

    Benötigt start und end Definition für die Section als Kommentar (md: `#!md <!-- -->`, py: `#!py #`).

    ```md title="docs/snippets/topic-x/index.md"
    # Topic X

    [...]

    <!-- --8<-- [start:section-x] -->
    1 + 1 = 2
    <!-- --8<-- [end:section-x] -->

    [...]
    ```

!!! danger "Kein Relavtiver Pfad für andere Location"

    - `#!md [Link](./../../topic-x/index.md#heading)`

## Code Annotations

Global aktivieren

```yaml
theme:
  features:
    - content.code.annotate # (1)!
```

1. :man_raising_hand: I'm a code annotation!
