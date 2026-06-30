#!/usr/bin/env python3
"""Convert resume markdown to ATS-friendly PDF."""

import re
import sys
from io import BytesIO
from pathlib import Path

import markdown
from xhtml2pdf import pisa

RESUME_CSS = """
@page {
    size: letter;
    margin: 0.6in 0.7in;
}
body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.35;
    color: #111;
}
h1 {
    font-size: 18pt;
    margin: 0 0 2pt 0;
    border: none;
}
h2 {
    font-size: 11pt;
    margin: 14pt 0 4pt 0;
    padding-bottom: 2pt;
    border-bottom: 1px solid #333;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
}
h3 {
    font-size: 10.5pt;
    margin: 8pt 0 2pt 0;
}
p { margin: 2pt 0 4pt 0; }
ul { margin: 2pt 0 6pt 0; padding-left: 16pt; }
li { margin: 2pt 0; }
hr { border: none; border-top: 1px solid #ccc; margin: 8pt 0; }
strong { font-weight: bold; }
a { color: #111; text-decoration: none; }
"""

HEADER_BLOCK = """
<div style="margin-bottom: 8pt;">
<p style="font-size: 10pt; color: #333; margin: 0;">
{contact}
</p>
</div>
"""


def md_to_html(md_text: str) -> str:
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "smarty"],
    )
    contact_match = re.search(
        r"<p>(.*?@.*?|https?://.*?)</p>",
        html_body,
        re.DOTALL,
    )
    contact = ""
    if contact_match:
        contact = re.sub(r"<[^>]+>", " | ", contact_match.group(1))
        contact = re.sub(r"\s*\|\s*\|\s*", " | ", contact).strip(" |")
        html_body = html_body.replace(contact_match.group(0), "", 1)

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{RESUME_CSS}</style></head>
<body>{HEADER_BLOCK.format(contact=contact) if contact else ""}{html_body}</body></html>"""


def convert_file(input_path: Path, output_path: Path) -> None:
    md_text = input_path.read_text(encoding="utf-8")
    html = md_to_html(md_text)
    with open(output_path, "wb") as pdf_file:
        status = pisa.CreatePDF(html, dest=pdf_file, encoding="utf-8")
    if status.err:
        raise RuntimeError(f"PDF generation failed for {input_path}")


def main() -> int:
    base = Path(__file__).resolve().parent.parent / "resume"
    targets = [
        ("Senior_US_Resume.md", "Senior_US_Resume.pdf"),
        ("Staff_US_Resume.md", "Staff_US_Resume.pdf"),
        ("Master_Resume.md", "Master_Resume.pdf"),
    ]
    if len(sys.argv) > 1:
        targets = [(sys.argv[1], sys.argv[1].replace(".md", ".pdf"))]

    for md_name, pdf_name in targets:
        md_path = base / md_name
        pdf_path = base / pdf_name
        if not md_path.exists():
            print(f"skip: {md_path} not found")
            continue
        convert_file(md_path, pdf_path)
        print(f"generated: {pdf_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
