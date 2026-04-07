"""Opdater Tutorial_9.md fra Tutorial_9_notebook.ipynb — **.ipynb er master** (MkDocs læser .md).

Kør efter du har rettet notebook:  python sync_tutorial9_md.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
nb_path = ROOT / "Tutorial_9_notebook.ipynb"
md_path = ROOT / "Tutorial_9.md"

nb = json.loads(nb_path.read_text(encoding="utf-8"))
parts: list[str] = []
open_fence = "\n```python\n"
close_fence = "\n```\n"

for cell in nb["cells"]:
    src = cell.get("source", [])
    text = "".join(src) if isinstance(src, list) else (src or "")
    if cell["cell_type"] == "markdown":
        parts.append(text.rstrip() + "\n")
    elif cell["cell_type"] == "code":
        text = text.rstrip()
        if text:
            parts.append(open_fence + text + close_fence)

body = "\n".join(parts).strip() + "\n"
insert = "**Notebook-version:** [Tutorial_9_notebook.ipynb](Tutorial_9_notebook.ipynb)\n\n"
if "**Notebook-version:**" not in body[:1500]:
    idx = body.find("\n\n## ")
    if idx != -1:
        body = body[: idx + 1] + insert + body[idx + 1 :]

md_path.write_text(body, encoding="utf-8")
print("Synced", md_path)
