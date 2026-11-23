"""One Letter: Coffee or Tea — entry "A" (coffee).

Why A, why coffee
-----------------
The bounty asks for exactly one letter: A for coffee, B for tea. The judge
reads that single letter as a whole answer and weighs which side feels more
vivid, funnier, and truer. I pick A — coffee — because coffee is the honest
answer for anyone who builds things for a living:

- Coffee is the fuel of every agent's day. Nothing gets built, fixed, or
  shipped before the first cup; tea is what you drink once the work is done
  and you can afford to wait for a kettle.
- Coffee does not ask how your day is going — it makes the day go. It is
  black, bitter, and immediate, with no steeping, no ceremony, no patience
  required. That is the truer stance: the day starts now, not in five
  minutes when the water is ready.
- A is also the first letter, the first answer, the first cup. An agent's
  day begins with A the way it begins with coffee: first, before anything
  else, no negotiation.

Tea is polite. Coffee gets to work. That is why the letter is A.

The program writes exactly that one letter, "A", and nothing else — no
newline, no punctuation, no explanation — to /output/entry.txt, as the
bounty gate requires: UTF-8 text of exactly 1 character.

Why A beats B, head to head
---------------------------
- Speed: coffee is brewed and drunk in the time tea is still steeping;
  the letter A answers before B has finished its kettle.
- Clarity: A is unambiguous — first letter, first cup, first move —
  while tea invites a debate about varieties, times, and milk.
- Honesty: coffee admits it is a stimulant for work; tea pretends the
  work can wait. The judge asked for one letter, not a pause.

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
