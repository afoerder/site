# Personal site

Quarto site published to GitHub Pages.

## Local preview

```bash
quarto preview
```

## First-time publish

The GitHub Action will not work until the `gh-pages` branch exists, so run this
once from your machine before relying on CI:

```bash
quarto publish gh-pages
```

After that, pushes to `main` trigger `.github/workflows/publish.yml`.

Two settings to check in the repository, both under Settings:

- **Actions → General → Workflow permissions** must be set to read and write.
- **Pages → Build and deployment** should deploy from the `gh-pages` branch, root.

## Custom domain

Add a `CNAME` file at the project root containing only your domain, and point
your DNS at GitHub Pages. Then set `site-url` in `_quarto.yml` to match.

## Files

```
_quarto.yml      Site config, navbar, fonts
theme.scss       Design system (colors, type, annotation brackets)
index.qmd        Landing page
projects.qmd     Project entries
publications.qmd Publication list
about.qmd        Bio and contact
images/          Figures. hero-detection.png is referenced by index.qmd
cv.pdf           Referenced by index.qmd and about.qmd; not yet added
```

## Before publishing

Search the project for `REPLACE` and resolve every instance.

```bash
grep -rn "REPLACE" --include="*.qmd" --include="*.yml" .
```
