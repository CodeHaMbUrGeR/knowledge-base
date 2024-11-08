# MkDocs

## Local Development

run commands from project root directory.

### Python Setup

create (venv)

```bash
python -m venv venv
```

activate (venv)

```bash
source venv/Scripts/activate
```

install dependencies

```bash
pip install -r requirements.txt
```

### Testing

```bash
mkdocs serve
```

by running the build command, mkdocs create the `site` folder containing all the required files.

### Testing (without drafts)

Requirements:

- configure `draft_docs`

local preview

```bash
mkdocs serve --clean
```

## Links

for a better internal linking, i use **markdown anchors** from [mkdocs-autorefs](https://mkdocstrings.github.io/autorefs/){:target="_blank"}.

### Open in new Tab

```markdown
[link](url){:target="_blank"}
```

### Markdown Anchor

Somewhere in target file

```markdown
[](){#foobar}
```

### Hyperlink to Markdown Anchor

Somewhere in any document

```markdown
[paragraph about foobar][foobar]
```
