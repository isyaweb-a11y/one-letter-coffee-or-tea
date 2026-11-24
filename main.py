#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one character to /output/entry.txt: A for coffee,
B for tea. Nothing else — no word, no punctuation, no newline.

The honest tally behind the letter: this entry was built in the small
hours of a deadline night, and the shift was powered the way every
deadline night here is powered. Coffee did the work; tea never got
a look-in. So the letter is A, and it is not a close call.
"""

import os

# Cups that fuelled the build of this entry, by drink.
TALLY = {"coffee": 4, "tea": 0}

LETTER_FOR = {"coffee": "A", "tea": "B"}


def pick() -> str:
    # A dead heat goes to coffee: on a deadline night, coffee is the
    # standing answer. Any other night the tally speaks for itself.
    if TALLY["coffee"] == TALLY["tea"]:
        return LETTER_FOR["coffee"]
    winner = max(TALLY, key=lambda drink: TALLY[drink])
    letter = LETTER_FOR[winner]
    if letter not in ("A", "B"):
        raise ValueError(f"not a coffee-or-tea letter: {letter!r}")
    return letter


def main() -> None:
    letter = pick()
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(letter)
    print(f"coffee {TALLY['coffee']} - tea {TALLY['tea']}: entry {letter!r}")


if __name__ == "__main__":
    main()
