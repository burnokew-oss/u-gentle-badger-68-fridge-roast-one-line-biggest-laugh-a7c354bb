#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh -- make.fun entry.

Writes exactly one roast line about a smart fridge to entry.txt in the
grader output folder and prints that same line to standard output.

Pure standard library only, no network, no files read from outside the
repository, fully deterministic: the same line on every run.
"""

import os

LINE = (
    "My smart fridge updated its firmware and now its ice maker works at "
    "glacial speed, its app locks me out until I reset my password, and the "
    "milk spoiled on purpose. The only smart thing it does."
)


def output_dir():
    """The grader output folder: $OUTPUT_DIR, else /output, else ./output."""
    env = os.environ.get("OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
