# Noldor Technologies — noldor.tech

The public website for **Noldor Technologies**, a company building **vector
symbolic architecture for analog hardware and edge AI**.

The site is a static page deployed to **GitHub Pages** at
[noldor.tech](https://noldor.tech) via GitHub Actions.

## Structure

```
index.html              # landing page (wordmark inlined for currentColor theming)
styles.css              # styling, light + dark via prefers-color-scheme
CNAME                   # custom domain (noldor.tech)
assets/
  noldor-wordmark.svg   # full "Ñoldor" tengwar wordmark (Quenya mode)
  noldor-letter.svg     # first tengwa (archaic ñ) — monogram / favicon source
  favicon.svg, favicon-32.png, apple-touch-icon.png, icon-512.png
tools/build_logos.py    # regenerates the logo assets from data_lake/Noldor.png
tests/                  # pytest checks for the assets + page
data_lake/              # source material (not served on the site)
```

## The logo

The wordmark is **Ñoldor** written in Tengwar (Quenya mode), matching the
[tecendil](https://www.tecendil.com/?q=%C3%91oldor&mode=quenya) rendering. The
SVGs are vector outlines (no font file shipped); the wordmark uses
`fill="currentColor"` so it follows the page theme. The monogram is the first
tengwa — the archaic *ñ* (*ñoldo*).

To regenerate the assets from the source PNG (needs `potrace`, Pillow, cairosvg):

```
python tools/build_logos.py
```

## Development

```
python -m pip install pytest
python -m pytest -q
```

CI runs the test suite on every push/PR; merges to `main` deploy to Pages.

## Project workflow

See `CLAUDE.md`, `queue.md` (current work), `todo.md` (long-horizon), and
`devlog.md` (history).
