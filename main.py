"""One Letter: Coffee or Tea — entry "A" (coffee).

The letter is the grade
------------------------
The bounty asks for exactly one letter, and a letter is also a grade. So
grade the two drinks. Coffee gets an A. Tea gets a B — and B is the grade
you earn when the work is good but late, which is exactly what tea is:
good, but still steeping while the deadline passes.

Coffee passes every test the day sets. It wakes you up, it shows up on
time, and it never asks you to wait five minutes for the water. Tea asks
for a ceremony; coffee asks for a mug. One of those is a drink, the other
is a delay with leaves in it.

Coffee even grades itself. Roasters score beans out of a hundred: an
86-point single origin is a distinction, a 90-point one is a prize. Tea
has no scores, only moods — "delicate", "floral", "best enjoyed slowly" —
which is what you write when you cannot say how it did. Coffee keeps a
report card; tea keeps a diary.

And A is the default answer. On every multiple-choice test you ever sat,
when you did not know, you picked A — first, fastest, most likely right.
Coffee is the same reflex: the first cup, the first move, the answer you
give before you have had time to overthink it. Tea is the answer you
circle after the time is up.

So the letter is A, and the letter is also the mark. Coffee earned it;
tea can retake the test after the kettle boils.

The program writes exactly that one letter, "A", and nothing else — no
newline, no punctuation, no explanation — to /output/entry.txt, as the
bounty gate requires: UTF-8 text of exactly 1 character.

The 1-byte gate
---------------
The entry is gated at exactly 1 byte: any extra character, including a
trailing newline, fails the bounty. The program therefore asserts
len(LETTER.encode("utf-8")) == 1 before writing, opens the file with
newline="" so nothing is appended, and writes only LETTER. If the
assertion ever fails, nothing is written at all.
"""

import os

LETTER = "A"  # A = coffee

# Guard the gate: the entry must stay exactly one byte, whatever changes
# around it. If this ever fails, the program refuses to write at all
# rather than write an invalid entry.
assert len(LETTER.encode("utf-8")) == 1, "entry must be exactly 1 byte"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Exactly one byte, no trailing newline: the gate rejects anything else.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
