# Noldor Technologies — noldor.tech

The public website for **Noldor Technologies**, a company building **vector
symbolic architecture for analog hardware and edge AI**.

The site is a static page deployed to **GitHub Pages** at
[noldor.tech](https://noldor.tech) via GitHub Actions.

## Structure

```
index.html              # landing page (wordmark inlined for currentColor theming)
404.html                # branded not-found page (served by Pages for unknown paths)
styles.css              # styling, light + dark via prefers-color-scheme
robots.txt, sitemap.xml # SEO
CNAME                   # custom domain (noldor.tech)
assets/
  noldor-wordmark.svg   # full "Ñoldor" tengwar wordmark (Quenya mode)
  noldor-mark.svg       # brand mark — first two tengwar "Ñol" — favicon source
  favicon.svg, favicon-32.png, apple-touch-icon.png, icon-512.png
tools/build_logos.py    # regenerates the logo assets from data_lake/Noldor.png
tests/                  # pytest checks for the assets + page
data_lake/              # source material (not served on the site)
```

## The logo

The wordmark is **Ñoldor** written in Tengwar (Quenya mode), matching the
[tecendil](https://www.tecendil.com/?q=%C3%91oldor&mode=quenya) rendering. The
SVGs are vector outlines (no font file shipped); the wordmark uses
`fill="currentColor"` so it follows the page theme. The brand mark
(`noldor-mark.svg`, the favicon source) is the first two tengwar — *Ñol* (the
archaic *ñ* / *ñoldo* + *lambe*).

To regenerate the assets from the source PNG (needs `potrace`, Pillow, cairosvg):

```
python tools/build_logos.py
```

## Development

```
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

CI runs the test suite on every push/PR; merges to `main` deploy to Pages.

## Project workflow

See `CLAUDE.md`, `queue.md` (current work), `todo.md` (long-horizon), and
`devlog.md` (history).
