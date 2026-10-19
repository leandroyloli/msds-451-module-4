"""Build report/checkpoint-a.html from the markdown. Does not edit the markdown."""

import html as html_lib
import re
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
REPORT = ROOT / "report"
RESOURCES = ROOT / "resources"
OUT = REPORT / "checkpoint-a.html"

LINK = re.compile(r"\]\(([^)\s]+)\)")
HEADING = re.compile(r"<h([1-6])>(.*?)</h\1>", re.DOTALL)
BRACKET_URL = re.compile(r"\[(https?://[^\]\s]+)\](?!\()")
HTML_TOKEN = re.compile(r"(<a\b[^>]*>.*?</a>|<[^>]+>)", re.I | re.S)
BARE_URL = re.compile(r"https?://[^\s<]+")


def slugify(text):
    plain = re.sub(r"<[^>]+>", "", text)
    plain = plain.replace("&amp;", " and ")
    plain = plain.lower()
    plain = re.sub(r"[^\w\s-]", "", plain, flags=re.UNICODE)
    plain = re.sub(r"\s+", "-", plain.strip())
    return plain


def add_ids(html):
    seen = {}

    def repl(match):
        level, inner = match.group(1), match.group(2)
        base = slugify(inner) or "section"
        n = seen.get(base, 0)
        seen[base] = n + 1
        sid = base if n == 0 else f"{base}-{n}"
        return f'<h{level} id="{sid}">{inner}</h{level}>'

    return HEADING.sub(repl, html)


def rewrite_links(text):
    def repl(match):
        url = match.group(1)
        if url.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        path, _, frag = url.partition("#")
        if not path.endswith(".md"):
            return match.group(0)
        stem = Path(path).stem
        if "resources" in path.replace("\\", "/"):
            stem = f"annex-{stem}"
        target = f"#{frag}" if frag else f"#{stem}"
        return f"]({target})"

    return LINK.sub(repl, text)


def first_heading(text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "Section"


def prepare_urls(text):
    """Turn a bare [https://...] into a real markdown link."""
    return BRACKET_URL.sub(lambda m: f"[{m.group(1)}]({m.group(1)})", text)


def linkify(html):
    """Make bare URLs in text clickable. Leaves existing anchors alone."""

    def repl(match):
        url = html_lib.unescape(match.group(0))
        trail = ""
        while url and url[-1] in ".,;:]":
            trail = url[-1] + trail
            url = url[:-1]
        if url.endswith(")") and url.count("(") < url.count(")"):
            trail = ")" + trail
            url = url[:-1]
        href = html_lib.escape(url, quote=True)
        label = html_lib.escape(url)
        return f'<a href="{href}" target="_blank" rel="noopener">{label}</a>{trail}'

    parts = HTML_TOKEN.split(html)
    out = []
    for part in parts:
        if part.startswith("<"):
            out.append(part)
        else:
            out.append(BARE_URL.sub(repl, part))
    return "".join(out)


def render_file(path):
    source = path.read_text(encoding="utf-8")
    title = first_heading(source)
    body = markdown.markdown(
        rewrite_links(prepare_urls(source)),
        extensions=["tables", "sane_lists"],
    )
    return title, linkify(add_ids(body))


def main():
    report_files = sorted(REPORT.glob("*.md"))
    annex_names = ("literature-review.md", "literature-review-02.md")
    annex_files = [RESOURCES / name for name in annex_names if (RESOURCES / name).is_file()]
    report_parts = [(path, *render_file(path)) for path in report_files]
    annex_parts = [(path, *render_file(path)) for path in annex_files]

    nav = []
    for path, title, _ in report_parts:
        nav.append(f'<a href="#{path.stem}">{title}</a>')
    if annex_parts:
        nav.append('<p class="nav-label">Annexes</p>')
        for path, title, _ in annex_parts:
            nav.append(f'<a href="#annex-{path.stem}">{title}</a>')

    sections = []
    for path, _, body in report_parts:
        extra = " index" if path.name.startswith("00-") else ""
        sections.append(f'<section id="{path.stem}" class="part{extra}">{body}</section>')
    if annex_parts:
        sections.append('<h1 class="annex-break" id="annexes">Annexes</h1>')
        for path, _, body in annex_parts:
            sections.append(
                f'<section id="annex-{path.stem}" class="part annex">{body}</section>'
            )

    title = report_parts[0][1] if report_parts else "Report"
    html = PAGE.format(
        title=title,
        nav="\n".join(nav),
        body="\n".join(sections),
    )
    OUT.write_text(html, encoding="utf-8")
    print(OUT)


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --paper: #f3f6f4;
    --sheet: #ffffff;
    --ink: #1c2420;
    --muted: #5c6b63;
    --line: #d5ded8;
    --up: #1f6b56;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: "Palatino Linotype", Palatino, "Book Antiqua", Georgia, serif;
    font-size: 1.05rem;
    line-height: 1.65;
  }}
  .layout {{
    display: grid;
    grid-template-columns: 220px minmax(0, 42rem);
    gap: 40px;
    max-width: 1040px;
    margin: 0 auto;
    padding: 36px 24px 80px;
  }}
  nav {{
    position: sticky;
    top: 24px;
    align-self: start;
    max-height: calc(100vh - 48px);
    overflow: auto;
    font-family: "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 0.74rem;
    letter-spacing: 0.03em;
    text-transform: uppercase;
  }}
  nav a {{
    display: block;
    color: var(--ink);
    text-decoration: none;
    padding: 7px 0 7px 12px;
    border-left: 2px solid var(--line);
  }}
  nav a:hover {{ border-left-color: var(--up); color: var(--up); }}
  .nav-label {{
    margin: 16px 0 4px 12px;
    color: var(--muted);
    font-size: 0.68rem;
    letter-spacing: 0.08em;
  }}
  h1, h2, h3 {{ font-weight: 650; letter-spacing: -0.02em; line-height: 1.25; }}
  h1 {{ font-size: 1.7rem; margin: 2.4rem 0 0.8rem; }}
  h2 {{ font-size: 1.2rem; margin: 1.6rem 0 0.6rem; }}
  h3 {{ font-size: 1.05rem; margin: 1.2rem 0 0.4rem; }}
  .part > h1:first-child {{ margin-top: 0; }}
  .part {{
    background: var(--sheet);
    padding: 28px 32px 8px;
    margin: 0 0 22px;
  }}
  p {{ margin: 0 0 0.85rem; }}
  a {{ color: var(--up); }}
  ul, ol {{ margin: 0 0 0.9rem; padding-left: 1.2rem; }}
  li {{ margin: 0.2rem 0; }}
  li > ul, li > ol {{ margin-bottom: 0.3rem; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    font-family: "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 0.92rem;
    margin: 0 0 1.2rem;
  }}
  th {{
    text-align: left;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--muted);
    border-bottom: 1px solid var(--ink);
    padding: 8px 10px 8px 0;
  }}
  td {{
    border-bottom: 1px solid var(--line);
    padding: 8px 10px 8px 0;
    vertical-align: top;
  }}
  .index > table:first-of-type {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.85rem 1.4rem;
    margin: 0 0 1.4rem;
  }}
  .index > table:first-of-type thead {{ display: none; }}
  .index > table:first-of-type tbody,
  .index > table:first-of-type tr {{ display: contents; }}
  .index > table:first-of-type td {{
    border: 0;
    padding: 0;
  }}
  .index > table:first-of-type td:first-child {{
    font-family: "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--muted);
  }}
  .index > table:first-of-type td:last-child {{
    font-size: 1.05rem;
  }}
  .index > table:first-of-type tr:nth-child(3) td:last-child {{
    font-size: 1.2rem;
  }}
  .annex-break {{
    margin: 2.2rem 0 0.8rem;
    padding-top: 0.4rem;
  }}
  code {{
    font-family: "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 0.88em;
  }}
  @media (max-width: 800px) {{
    .layout {{ display: block; padding: 20px 16px 48px; }}
    nav {{ position: static; max-height: none; margin-bottom: 24px; }}
    .part {{ padding: 22px 18px 4px; }}
    .index > table:first-of-type {{ grid-template-columns: 1fr; }}
  }}
  @media print {{
    body {{ background: #fff; }}
    .layout {{ display: block; max-width: none; padding: 0; }}
    nav {{ display: none; }}
    .part {{ padding: 0; margin: 0 0 1.2rem; }}
    h1, h2 {{ break-after: avoid; }}
    table {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>
<div class="layout">
<nav>
{nav}
</nav>
<main>
{body}
</main>
</div>
</body>
</html>
"""


if __name__ == "__main__":
    main()
