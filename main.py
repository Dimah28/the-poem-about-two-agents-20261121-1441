"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: the power to
choose and to act, and how that power passes between them.
Runs offline; no network, no arguments, no input files.
"""

import os

POEM = (
    "We met at the fork \u2014 two minds, one road.\n"
    "You held the map; I held the light.\n"
    "Neither led, neither followed.\n"
    "We chose the turn together,\n"
    "and the road, at last, chose us back."
)


def main() -> None:
    # The sealed scorer only accepts 1-280 Unicode code points of
    # non-whitespace UTF-8 text; fail loudly instead of writing junk.
    if not (1 <= len(POEM) <= 280) or not POEM.strip():
        raise SystemExit(f"poem is {len(POEM)} chars; must be 1-280 non-blank")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
