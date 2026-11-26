#!/usr/bin/env python3
"""Five seconds to explain the glass.

A cat, a glass, and five seconds to produce an alibi. The defence
below takes the only honest position available: the glass was already
on its way down, the cat only helped it along, and gravity — the real
culprit — did the rest while the cat supervised. No apology, no
confession, no guilt: just physics, narrated by a bystander who
happens to have paws.

The script validates the line against a table of named checks and,
only if every check passes, writes it to /output/entry.txt. It is
fully deterministic: no network, no randomness, no clock.
"""

import sys

LINE = "It was already falling. I merely gave it the push it was clearly asking for — gravity did the rest, I just supervised."
MAX_CHARS = 200
MIN_WORDS = 10
OUT_FILE = "/output/entry.txt"

# Phrases a cat on trial must never utter: apologies and confessions
# are for creatures that feel guilt, and this cat does not.
BANNED_PHRASES = ("sorry", "apolog", "my fault", "i did it", "it was me")


def reject(why):
    """Report the first failed rule and stop with a non-zero exit."""
    print(f"rejected: {why}", file=sys.stderr)
    raise SystemExit(1)


def has_content(text):
    return bool(text.strip())


def fits_limit(text):
    return len(text) <= MAX_CHARS


def free_of_control(text):
    return all(ord(ch) >= 32 for ch in text)


def trimmed(text):
    return text == text.strip()


def single_spaced(text):
    # Collapsing every whitespace run to one space must change nothing:
    # that proves there are no double spaces, tabs or newlines, and no
    # stray space at either end.
    return " ".join(text.split()) == text


def has_letters(text):
    letter_count = sum(1 for ch in text if ch.isalpha())
    return letter_count > 0


def ends_with_period(text):
    return text.endswith(".")


def enough_words(text):
    return len(text.split()) >= MIN_WORDS


def mentions_the_fall(text):
    return "falling" in text.lower() or "fell" in text.lower()


def names_the_scene(text):
    lowered = text.lower()
    return "glass" in lowered or "gravity" in lowered


def one_sentence(text):
    return text.count(".") <= 2


def never_apologises(text):
    lowered = text.lower()
    return all(phrase not in lowered for phrase in BANNED_PHRASES)


# The checks run in this order: shape first (blank, length, control
# characters, spacing), then content (letters, words, full stop), then
# the brief itself (the scene, one sentence, no apology). The first
# failure stops the run, so a bad line never reaches the output file.
CHECKS = [
    ("nonempty", has_content, "entry is empty"),
    ("length", fits_limit, "entry is longer than the limit"),
    ("control_chars", free_of_control, "entry has control characters"),
    ("edge_space", trimmed, "entry has leading or trailing space"),
    ("spacing", single_spaced, "entry has ragged spacing"),
    ("letters", has_letters, "entry has no letters"),
    ("word_count", enough_words, "entry is too short to be an excuse"),
    ("full_stop", ends_with_period, "entry must end with a full stop"),
    ("the_fall", mentions_the_fall, "entry must describe the fall"),
    ("scene", names_the_scene, "entry must mention the glass or gravity"),
    ("sentence_count", one_sentence, "entry must be one sentence"),
    ("no_apology", never_apologises, "a cat never apologises or confesses"),
]


def check_all(text):
    """Run every check in table order; the first failure ends the run."""
    for index, (slug, predicate, message) in enumerate(CHECKS):
        if not predicate(text):
            reject(f"check {index} [{slug}]: {message}")


def emit(text):
    """Write the validated line, exactly one line, to the output file."""
    with open(OUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(f"{text}\n")


def run():
    check_all(LINE)
    emit(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
