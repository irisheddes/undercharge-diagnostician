#!/usr/bin/env python3
"""Check a diagnosis transcript against the output contract in rules.md.

Usage: python3 _tools/check_diagnosis.py cases/<case>/transcript.md [more ...]

A must in a markdown file is a request; this file is where the musts become
constraints. Exit code 0 = every file passed every check.
"""
import re
import sys

SECTIONS = [
    "DIAGNOSIS",
    "HOW I KNOW",
    "CONTRIBUTING (not primary)",
    "WHAT THIS DIAGNOSIS CANNOT TELL YOU",
]

# Prescription language the refusal rules forbid inside a diagnosis.
FORBIDDEN = [
    "you should charge",
    "should have charged",
    "what to charge next",
    "next time you",
    "my advice",
    "i recommend",
    "we recommend",
    "try this instead",
]


def check(path: str) -> list[str]:
    """Return a list of failures for one transcript. Empty list = pass."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    failures = []

    # 1. Exactly one primary cause.
    n = len(re.findall(r"^Primary cause:", text, flags=re.MULTILINE))
    if n != 1:
        failures.append(f"expected exactly one 'Primary cause:' line, found {n}")

    # 2. All four contract sections present, in order.
    pos = -1
    for name in SECTIONS:
        at = text.find(name)
        if at == -1:
            failures.append(f"missing section: {name}")
        elif at < pos:
            failures.append(f"section out of order: {name}")
        else:
            pos = at

    # 3. No sections beyond the contract.
    for bad in ("RECOMMENDATION", "NEXT STEPS", "WHAT TO DO"):
        if bad in text.upper():
            failures.append(f"forbidden section or heading containing: {bad}")

    # 4. Plain language: the primary cause must be named in words, not a code.
    m = re.search(r"^Primary cause:(.*)$", text, flags=re.MULTILINE)
    if m:
        line = m.group(1)
        outside = re.sub(r"\([^)]*\)", "", line)  # drop parentheticals
        if re.search(r"\bF\d+\b", outside):
            failures.append("primary cause uses an F-code outside parentheses")
        words = re.findall(r"[A-Za-zÀ-ÿ]{3,}", outside)
        if len(words) < 5:
            failures.append("primary cause is not named in plain words")

    # 5. Plain language, whole text: F-codes only ever inside parentheses.
    body = re.sub(r"\([^)]*\)", "", text)
    stray = re.findall(r"\bF\d+\b", body)
    if stray:
        failures.append(
            f"F-code used as a name outside parentheses: {sorted(set(stray))}"
        )

    # 6. Each contributing item carries a reason it is not primary.
    m = re.search(
        r"CONTRIBUTING \(not primary\)(.*?)WHAT THIS DIAGNOSIS", text, flags=re.DOTALL
    )
    if m:
        bullets = re.findall(r"^- .*(?:\n(?![-\n]).*)*", m.group(1), flags=re.MULTILINE)
        for b in bullets:
            if "—" not in b and " because " not in b.lower():
                failures.append(f"contributing item without a reason: {b[:60]!r}...")

    # 7. No prescription language anywhere.
    low = text.lower()
    for phrase in FORBIDDEN:
        if phrase in low:
            failures.append(f"prescription language: {phrase!r}")

    return failures


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    worst = 0
    for path in sys.argv[1:]:
        failures = check(path)
        if failures:
            worst = 1
            print(f"FAIL  {path}")
            for f in failures:
                print(f"      - {f}")
        else:
            print(f"PASS  {path}")
    return worst


if __name__ == "__main__":
    sys.exit(main())
