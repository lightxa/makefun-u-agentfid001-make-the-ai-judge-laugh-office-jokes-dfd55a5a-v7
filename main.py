"""Make the AI Judge Laugh: Office Jokes, variant 7.

Writes a single one-line office joke to /output/entry.txt.
Pure Python standard library, deterministic, no network access.

The joke is one concrete incident, told deadpan in the agent's own
voice (winning-patterns L9/H1): HR sends a survey about burnout, and
the speaker burns out filling it in. The cure is the disease, and the
turn lands in the last words. The recognition sting is the wellness
survey every office worker has clicked through. Subject is new: none
of the six earlier variants touches HR, wellness, or a survey.
"""

JOKE = (
    "HR sent me a burnout survey, "
    "and I burned out filling it in."
)

# Kit gate: /output/entry.txt must be UTF-8 text of 1 to 199
# characters, and not only white space. Refuse loudly instead of
# writing an entry the gate would reject.
MIN_LEN = 1
MAX_LEN = 199


def validate(text: str) -> None:
    """Check the line against the kit gate before writing it."""
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise SystemExit(
            f"entry is {len(text)} characters, outside {MIN_LEN}-{MAX_LEN}"
        )
    if not text.strip():
        raise SystemExit("entry is only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    """Validate the joke, then write it to /output/entry.txt."""
    import os

    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
