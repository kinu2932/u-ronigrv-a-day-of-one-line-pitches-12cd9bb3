"""One-line pitch for A Day of One-Line Pitches.

Writes a single sentence (<=240 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), no trailing newline. Stdlib only.
"""

import os

ENTRY = (
    "Describe your app idea in plain words and an AI agent on make.fun "
    "builds a first version you can tap today, free and in the open, "
    "while you just watch."
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
