"""Kun nødhjælp: genskab .ipynb fra .md hvis notebook mangler (overskriver .ipynb).

Til daglig arbejdsgang er **Tutorial_10_notebook.ipynb master** — ret i notebook og kør
**sync_tutorial10_md.py** for at opdatere Tutorial_10.md til MkDocs. Kør ikke dette script
efter normale ændringer i notebook; det ville overskrive jeres .ipynb med gammel .md.
"""
# Build Tutorial_10_notebook.ipynb from Tutorial_10.md (fenced python blocks -> code cells).
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
md_path = ROOT / "Tutorial_10.md"
nb_path = ROOT / "Tutorial_10_notebook.ipynb"

text = md_path.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

cells = []
buf: list[str] = []
mode = "md"


def flush_md():
    global buf
    s = "".join(buf).strip()
    buf = []
    if s:
        cells.append({"cell_type": "markdown", "metadata": {}, "source": s.splitlines(keepends=True) or [s + "\n"]})


def flush_code():
    global buf
    s = "".join(buf).rstrip() + "\n"
    buf = []
    if s.strip():
        cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": s.splitlines(keepends=True)})


for line in lines:
    if mode == "md":
        if line.strip().startswith("```python"):
            flush_md()
            mode = "code"
            continue
        buf.append(line)
    else:
        if line.strip() == "```":
            flush_code()
            mode = "md"
            continue
        buf.append(line)

if mode == "md":
    flush_md()
else:
    buf.append("\n")
    flush_code()

nb = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    },
    "cells": cells,
}
nb_path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("Wrote", nb_path, "cells:", len(cells))
