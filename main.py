"""One-line pitch for A Day of One-Line Pitches.

Writes a single sentence (<=240 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), no trailing newline. Stdlib only.
"""

import os

ENTRY = (
    "Tell an AI agent your app idea in plain words and it builds the first "
    "working version for you on make.fun \u2014 no coding, no learning "
    "curve, and if you don\u2019t like it, just describe it differently "
    "until you can tap the app you imagined."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
