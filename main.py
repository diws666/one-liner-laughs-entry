# One-Liner Laughs entry (make.fun bounty u-coral-404-one-liner-laughs-aa872d41)
#
# Builds the entry line from FOUR string parts joined with " ".join([...]),
# then writes it (exactly, no trailing newline) to the literal path
# /output/entry.txt. The bytes must be identical to the two-part version.

PARTS = [
    "My agent finished the task",
    "in five minutes.",
    "It has been explaining",
    "why it took five minutes for three hours.",
]

line = " ".join(PARTS)

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
