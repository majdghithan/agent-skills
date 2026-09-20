#!/usr/bin/env python3
"""Check a piece of dialect Arabic before delivering it.

    python3 scripts/check_output.py <dialect> <file>
    cat draft.txt | python3 scripts/check_output.py levantine -

Reports three things, all read live from the guides so they never drift:
  1. MSA leaks  - forms the target guide's leak table says to remove.
  2. Dialect mixing - markers SKILL.md assigns to a DIFFERENT dialect.
  3. Spelling   - tanween, short vowels, em-dashes.

It flags candidates; the writer decides. Exit code 1 if anything is flagged.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
AR = r"[ء-يٱ-ۓ]"          # letters only, no diacritics
TANWEEN = "ًٌٍ"                 # ـً ـٌ ـٍ
HARAKAT = "َُِْ"           # fatha damma kasra sukun


def tokens(cell):
    """Arabic forms in a table cell, minus glosses and punctuation."""
    cell = re.sub(r"\([^)]*\)", " ", cell)
    out = []
    for raw in re.split(r"[/،,]| or ", cell):
        t = "".join(re.findall(AR + r"+|\s", raw)).strip()
        t = re.sub(r"\s+", " ", t)
        if len(t.replace(" ", "")) >= 2:
            out.append(t)
    return out


NOISY = {"\u0644\u0627", "\u0645\u0627"}  # bare laa / maa: core dialect negators, not leaks on their own


def leaks_for(guide):
    """Left column of the guide's 'MSA leaks' table."""
    text = (ROOT / "references" / f"{guide}.md").read_text()
    block = re.search(r"#+ .*leaks.*?\n(.*?)(?=\n#+ |\Z)", text, re.S | re.I)
    found = []
    if block:
        for row in block.group(1).splitlines():
            if row.startswith("|") and "---" not in row:
                first = row.strip().strip("|").split("|")[0]
                found += tokens(first)
    return sorted(set(found) - NOISY, key=len, reverse=True)


def markers():
    """SKILL.md marker table -> {dialect: [forms]}, minus the shared ones."""
    skill = (ROOT / "SKILL.md").read_text()
    block = re.search(r"\| Dialect \| Markers \|\n\s*\|[-| ]+\|\n((?:\s*\|.*\|\n)+)", skill)
    table = {}
    if block:
        for row in block.group(1).strip().splitlines():
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            table[cells[0].lower()] = tokens(cells[1])
    return table


def hits(form, text):
    return re.search(rf"(^|\W){re.escape(form)}(\W|$)", text) is not None


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    dialect, path = sys.argv[1].lower(), sys.argv[2]
    guides = {p.stem for p in (ROOT / "references").glob("*.md")}
    if dialect not in guides:
        sys.exit(f"unknown dialect '{dialect}'. one of: {', '.join(sorted(guides))}")

    text = sys.stdin.read() if path == "-" else pathlib.Path(path).read_text()
    flags = []

    for form in leaks_for(dialect):
        if hits(form, text):
            flags.append(f"MSA leak: '{form}' - see the leak table in {dialect}.md")

    table = markers()
    mine = set(table.get(dialect, []))
    for other, forms in table.items():
        if other == dialect:
            continue
        for form in forms:
            if form not in mine and hits(form, text):
                flags.append(f"dialect mixing: '{form}' belongs to {other}, not {dialect}")

    if any(c in text for c in TANWEEN):
        flags.append("spelling: tanween in dialect text")
    if any(c in text for c in HARAKAT):
        flags.append("spelling: short-vowel marks in dialect text")
    if chr(0x2014) in text or chr(0x2013) in text:
        flags.append("spelling: em/en dash")

    if not flags:
        print(f"clean for {dialect}")
        return
    print(f"{len(flags)} thing(s) to look at for {dialect}:")
    for f in dict.fromkeys(flags):
        print(" -", f)
    sys.exit(1)


if __name__ == "__main__":
    main()
