#!/usr/bin/env python3
"""Consistency checks for the lahja skill. Run: python3 scripts/check_skill.py

Catches the mistakes that actually happened while writing it:
a detection marker that belongs to two dialects, a reference file named in
SKILL.md that does not exist, an em-dash, a guide missing a section, and an
MSA leak word sitting in a dialect line of a worked rewrite.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
GUIDES = sorted((ROOT / "references").glob("*.md"))
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


skill = SKILL.read_text()
guides = {g.stem: g.read_text() for g in GUIDES}

# 1. every reference file named in SKILL.md exists, and every guide is routed to
named = set(re.findall(r"references/([a-z]+)\.md", skill))
check(not (named - guides.keys()), f"SKILL.md points at missing guide(s): {named - guides.keys()}")
check(not (guides.keys() - named), f"guide(s) never routed to from SKILL.md: {guides.keys() - named}")

# 2. no em-dash or en-dash anywhere
for path in [SKILL, *GUIDES, ROOT / "scripts" / "check_skill.py"]:
    DASHES = (chr(0x2014), chr(0x2013))  # built by code point so this file passes its own check
    bad = [i + 1 for i, l in enumerate(path.read_text().splitlines()) if any(d in l for d in DASHES)]
    check(not bad, f"{path.name}: em/en dash on line(s) {bad}")

# 3. detection markers must point to ONE dialect: a marker listed for dialect X
#    must not appear as a word in another dialect's guide. Lines that name another
#    dialect are skipped: a guide naming a foreign form to BAN it ("No عم", "don't
#    import Levantine بكتب") is correct, not a collision.
NAMES = ("Levantine", "Egyptian", "Gulf", "Iraqi", "Maghrebi", "Moroccan", "Tunisian",
         "Algerian", "Kuwaiti", "Emirati", "Najdi", "Hejazi", "Syrian", "Lebanese",
         "Palestinian", "Jordanian", "Baghdadi", "Mosuli", "Libyan", "Sudanese", "Yemeni",
         "Sanaani", "Cairene")
marker_block = re.search(r"\| Dialect \| Markers \|\n\s*\|[-| ]+\|\n((?:\s*\|.*\|\n)+)", skill)
check(marker_block is not None, "SKILL.md: marker table not found")
if marker_block:
    for row in marker_block.group(1).strip().splitlines():
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        dialect, markers = cells[0].lower(), cells[1]
        markers = re.sub(r"\([^)]*\)", "", markers)  # drop parenthetical examples, they are not markers
        toks = re.findall(r"[\u0600-\u06FF\u0750-\u077F]+", markers)
        arabic = [t for t in (tok.strip("\u060C\u061B\u061F") for tok in toks) if len(t) >= 2]
        for m in arabic:
            for stem, text in guides.items():
                if stem.startswith(dialect[:4]):
                    continue
                hits = [l for l in text.splitlines()
                        if re.search(rf"(^|[ ،|(]){re.escape(m)}([ ،.|)؟]|$)", l)
                        and not any(n in l for n in NAMES)]
                if hits:
                    fails.append(f"marker collision: '{m}' listed for {dialect} but used in {stem}.md")

# 4. each guide has the sections the router promises
NEEDED = ["Negation", "Future", "Aspect", "Spelling", "leaks", "Worked rewrites", "Feedback", "Sources"]
for stem, text in guides.items():
    for section in NEEDED:
        check(re.search(rf"^#+ .*{section}", text, re.M | re.I), f"{stem}.md: no '{section}' section")
    check("majd.ghithan20@gmail.com" in text, f"{stem}.md: feedback contact missing")

# 5. no MSA leak word inside a dialect output line of a worked rewrite
LEAKS = ["سوف", "لقد", "ليس", "الذي", "التي", "ماذا", "لماذا", "أين", "الآن", "يريد", "يستطيع", "لا يوجد", "هل "]
for stem, text in guides.items():
    for i, line in enumerate(text.splitlines(), 1):
        if not re.match(r"^- (?!MSA)[A-Z][A-Za-z ]*:", line):
            continue  # only the dialect line of a rewrite pair
        for leak in LEAKS:
            check(leak not in line, f"{stem}.md:{i}: MSA leak '{leak}' in a dialect rewrite line")

print(f"checked {len(guides)} guides")
if fails:
    print("\nFAIL")
    print("\n".join(" - " + f for f in fails))
    sys.exit(1)
print("OK")
