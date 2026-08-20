# andrewfoerder.com

Personal site. Quarto, published to GitHub Pages.

## Local preview

```bash
quarto preview
```

## Publishing

Pushes to `main` deploy automatically via `.github/workflows/publish.yml`.
To deploy manually:

```bash
quarto publish gh-pages
```

The workflow needs two repository settings:

- **Settings → Actions → General → Workflow permissions**: read and write
- **Settings → Pages → Build and deployment**: deploy from `gh-pages`, root

## Files

```
_quarto.yml       Site config, navbar, social meta
theme.scss        Design system: color, type, layout
index.qmd         Landing page: hero, project cards, about, publications
projects.qmd      Full project entries
publications.qmd  Complete publication list
field.js          Animated hero background; pipeline stage cycling
images/           Figures and photographs
cv.pdf            Academic CV
resume.pdf        Industry resume
CNAME             Custom domain for GitHub Pages
```
