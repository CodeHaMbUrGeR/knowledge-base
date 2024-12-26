# knowledge-base

Wissensdatenbank mit [MkDocs](https://www.mkdocs.org/)

## Veröffentlichung auf GitHub Pages

1. Repo auf GitHub erstellen und lokal klonen
2. Code schreiben/editieren (mkdocs)
3. commit und push auf GitHub
4. GitHub Repo: **Settings** > **Pages** > **branch**: `gh-pages` (auswählen & speichern)
5. Deploy Key im Repo hinterlegen -- Wie? so: [Deploy Key](#deploy-key)

## Deploy Key

Lokal einen SSH Schlüssel erstellen:

```bash
ssh-keygen -t ed25519 -C "gitlab-to-github" -f ~/.ssh/gitlab_to_github
```

Anschließend den öffentlichen Teil des Schlüssels im GitHub Repo hinterlegen und dabei auch die Schreibrechte vergeben.

- select `Allow write access`.
