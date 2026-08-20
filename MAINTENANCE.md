# Maintenance notes

Written 2026-08-20, right after launch, for whoever edits this next
(probably me, months from now, having forgotten all of it).

## Making a change

Edit the `.qmd` or `.scss` files directly, then:

```bash
cd ~/site
quarto preview          # check it locally
```

When it looks right:

```bash
cd ~/site
rm -rf _site            # see "stale output" below — do not skip this
git add -A && git commit -m "what changed"
git push                # the Action deploys automatically
```

`quarto publish gh-pages` still works and does the same job manually.
Either is fine; don't do both for one change.

## Two traps that already cost real time

**Stale output.** `_site/` keeps files from previous renders. Deleting a
page's source does not delete the built HTML, and publish copies whatever
is in `_site`. Four old draft pages went live this way. Always
`rm -rf _site` before publishing when anything was renamed or removed.

**Silent no-ops.** A copy or edit that doesn't land looks identical to one
that did. Live placeholder text sat on the publications page for days
because an update never got copied. After any batch of edits, grep for
what should and shouldn't be there:

```bash
grep -rn "REPLACE\|TODO\|FIXME" *.qmd *.yml
```

## Numbers

Every number about the dust storm project comes from
`~/Downloads/mars-dust-storm/LICENSED_NUMBERS.md` and nowhere else. Not
from memory, not from a chat, not from an older version of this site. A
retired figure reached both a slide and this site by traveling through
conversation instead of the ledger. Numbers travel with their riders or
they don't travel.

Verify with:

```bash
cd ~/Downloads/mars-dust-storm
.venv/bin/python src/step06_repro_extract.py --check-only
```

## Regenerating figures

`tools/storm_figure.py` builds `images/predictability-gap.png` (projects
page) and `tools/storm_card.py` builds `images/predictability-gap-card.png`
(homepage card). Both need `tools/fonts/` — Space Grotesk and IBM Plex
Mono, instanced from the Google Fonts variable font. Neither font has a
sigma glyph, so the scripts register DejaVu Sans as a fallback for that
one character.

```bash
cd ~/site/tools && python3 storm_figure.py && python3 storm_card.py
```

The other figures are crops of source images, not generated.

## Decisions that are deliberate, not oversights

- **The headline is broad on purpose.** Earlier versions boxed me into
  Mars or into mapping work. Specificity was traded away knowingly.
- **No plain-language summaries under citations** on the publications
  page.
- **Status labels are literal.** Unpublished stays unpublished; the
  corpus run stays "scheduled" until it has run.
- **Limitations sit next to results,** including the leakage bug and the
  tile-level split caveat. That pairing is what makes the honesty read as
  rigor rather than weakness.
- **No autoplay on the labeler video.** The animated background already
  carries the page's motion, and autoplay ignores reduced-motion
  preferences.
- **Code is withheld until publication.** TYXN Labeler stays private
  until it runs on a machine other than mine.
- **Figures sit on white inside dark trim** even though the page is warm
  off-white. That's the print convention of a plate, and it keeps the
  evidence visually separate from the prose.

## CSS gotchas specific to this site

- Quarto applies a **vertical margin to images** (~22px). It makes any
  frame taller than its picture and shows as a band. Every figure rule
  carries `margin: 0 !important` because of it.
- Use **`outline` with `outline-offset: -1px`**, not `border`, for trim on
  images. Borders get clipped by the container; inset box-shadows paint
  *behind* an image and are invisible under opaque content.
- The pipeline stage frame has **no aspect-ratio**. The first image sits in
  normal flow and sets the height; the rest are absolutely positioned over
  it. Anything else produces letterboxing or cropping.

## Things left undone at launch

- GitHub profile README.
- Résumé says "deploy at survey scale" while the corpus run is only
  scheduled. Fix to "built and validated deployment for."
- The paleobiology collaboration appears on the site but on neither PDF,
  so it can't be verified.
- FINESST line on the CV says decision pending; update when it lands.
