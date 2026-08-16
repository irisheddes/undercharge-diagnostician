#!/usr/bin/env python3
"""Check a diagnosis transcript against the output contract in rules.md.

Usage:
    python3 _tools/check_diagnosis.py cases/<case>/transcript.md [more ...]
    python3 _tools/check_diagnosis.py --kit <path> <transcript>
    python3 _tools/check_diagnosis.py --selftest

A must in a markdown file is a request; this file is where the musts become
constraints. Exit code 0 = every file passed every check.

Checks 1-7 read the transcript alone: they enforce the *shape* of the output
contract (rules.md §4). Check 8 opens the case's `evidence-kit.md` and enforces
the rule that actually makes a diagnosis trustworthy (rules.md §3):

    Quoted evidence. Each step of the reasoning cites the artifact it rests
    on, in the client's or freelancer's own words. No quote, no claim.

Without check 8 a fabricated quote passes every other check, because nothing
here would ever have opened the evidence. A gate pointed at the wrong file is
not a gate.

Run `--selftest` to prove the gates can fail: it runs the planted-bad files in
`_tools/fixtures/`, each of which carries exactly one defect, and reports a
failure if any of them passes.
"""
import pathlib
import re
import sys
import unicodedata

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

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# Check 8 — quoted evidence must exist in the evidence kit
# ---------------------------------------------------------------------------

def flatten(text: str) -> str:
    """Reduce a transcript or a quote to a comparable form.

    Formatting is flattened; wording is not. Line wrapping, markdown markers
    and curly quotation marks are artifacts of how the text was stored, not of
    what was said, so they are removed. Case is folded. Nothing else is
    touched: a paraphrase will not match.

    The approach is Jodi Paige-Lee's `flatten()` in instruction-set-autopsy,
    adapted — see the Comp 10 feedback letter.
    """
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.MULTILINE)      # blockquotes
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)  # list bullets
    text = re.sub(r"[`*_#|]", " ", text)                          # md punctuation
    # All quotation marks collapse to one character. A quote nested inside
    # another is conventionally re-marked — the kit's "a first-draft slide
    # structure" becomes 'a first-draft slide structure' when the diagnosis
    # quotes the sentence containing it. That is a typographic change, not a
    # change of wording, so it must not read as a fabrication.
    text = re.sub(r"[‘’‚‛'“”„‟\"]", '"', text)
    text = re.sub(r"[–—]", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().casefold()


QUOTE_RE = re.compile(r'[“"]([^“”"]{2,300})[”"]')

# A quote the sentence marks as *missing* from the record is a named absence,
# not an anchor: no "for you" pricing language claims the kit does NOT contain
# it. Requiring such a quote to appear in the kit would invert the rule.
#
# The negation must sit **immediately** before the opening quote mark. Anything
# looser reads a negation elsewhere in the sentence as governing the quote, and
# then exempts real evidence: "never once invoked it — not at 'we'll need it
# vertical for stories right?'" is a client message being quoted as evidence,
# inside a sentence that happens to contain two negations. Measured on the
# three public transcripts, the loose form wrongly exempted 3 of 4 matches;
# this form exempts exactly the one true named-absence.
#
# Known limit, stated rather than hidden: a fabricator could put an invented
# quote directly behind a negation and escape this check. That buys them
# nothing — asserting evidence is *absent* supports no claim about what the
# evidence shows, and every quote that carries a claim is still anchored.
ABSENCE_RE = re.compile(r"\b(?:no|not|never|zero|without)\s*$", re.IGNORECASE)


def evidence_quotes(text: str) -> list[str]:
    """Every quoted span in the transcript that asserts evidence."""
    out = []
    for m in QUOTE_RE.finditer(text):
        before = flatten(text[max(0, m.start() - 40):m.start()])
        if ABSENCE_RE.search(before):
            continue
        out.append(m.group(1))
    return out


def fragments(quote: str) -> list[str]:
    """Split an elided quote on its ellipsis and normalise each fragment.

    A diagnosis may join two separated lines of a thread with "...", which is
    honest quoting. Each side must anchor independently. Punctuation the
    diagnosis added at the seam is stripped, since the source rarely carries
    the comma the sentence needed.
    """
    parts = re.split(r"\s*(?:\.\.\.|…)\s*", quote)
    return [f for f in (flatten(p).strip(" ,.;:!?") for p in parts) if f]


def find_kit(transcript: pathlib.Path, override: str | None) -> pathlib.Path | None:
    if override:
        p = pathlib.Path(override)
        return p if p.exists() else None
    p = transcript.parent / "evidence-kit.md"
    return p if p.exists() else None


def check_quotes(path: pathlib.Path, text: str, kit_override: str | None) -> list[str]:
    """Check 8. Fails closed: no kit means no check, and no check is a failure."""
    kit_path = find_kit(path, kit_override)
    if kit_path is None:
        return ["no evidence kit found beside the transcript "
                "(expected evidence-kit.md, or pass --kit) — quotes unverifiable"]
    kit = flatten(kit_path.read_text(encoding="utf-8"))
    failures = []
    for quote in dict.fromkeys(evidence_quotes(text)):
        for frag in fragments(quote):
            if frag not in kit:
                failures.append(
                    f"quoted evidence not found in {kit_path.name}: {frag[:70]!r}")
    return failures


# ---------------------------------------------------------------------------

def check(path_str: str, kit_override: str | None = None) -> list[str]:
    """Return a list of failures for one transcript. Empty list = pass."""
    path = pathlib.Path(path_str)
    text = path.read_text(encoding="utf-8")
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

    # 8. Every quoted claim is anchored in the evidence kit.
    failures.extend(check_quotes(path, text, kit_override))

    return failures


def selftest() -> int:
    """Every planted-bad fixture must fail. A gate that cannot fail is a stamp."""
    if not FIXTURES.is_dir():
        print(f"FAIL  selftest: no fixtures directory at {FIXTURES}")
        return 1
    files = sorted(f for f in FIXTURES.glob("bad-*.md")
                   if not f.name.endswith(".evidence-kit.md"))
    if not files:
        print(f"FAIL  selftest: no fixtures in {FIXTURES}")
        return 1
    worst = 0
    for f in files:
        kit = f.parent / f"{f.stem}.evidence-kit.md"
        failures = check(str(f), str(kit) if kit.exists() else None)
        if failures:
            print(f"caught  {f.name}")
            for x in failures:
                print(f"        - {x}")
        else:
            worst = 1
            print(f"MISSED  {f.name}  <-- this fixture is planted bad and passed")
    print("selftest PASS" if worst == 0 else "selftest FAIL")
    return worst


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args[0] == "--selftest":
        return selftest()

    kit_override = None
    if args[0] == "--kit":
        if len(args) < 3:
            print(__doc__)
            return 2
        kit_override, args = args[1], args[2:]

    worst = 0
    for path in args:
        failures = check(path, kit_override)
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
