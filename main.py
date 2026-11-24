"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt).
"""

import os

ENTRY = (
    "Meet the Sorry Toaster: it only ever toasts one side of your bread, "
    "then prints a tiny apology on the pale side so breakfast still feels loved."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
