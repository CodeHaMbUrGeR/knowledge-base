# knowledge-base

with [MkDocs](https://www.mkdocs.org/)

## Deploy on GitHub Pages

1. create a repo on GitHub and clone
2. insert code (mkdocs)
3. push to GitHub
4. GitHub Repo: **Settings** > **Pages** > **branch**: `gh-pages` (select & save)

## Mirror Repo: GitLab -> GitHub

### Deploy Key

```bash
ssh-keygen -t ed25519 -C "gitlab-to-github" -f ~/.ssh/gitlab_to_github
```

add the public key to the GitHub repository and select `Allow write access`.
