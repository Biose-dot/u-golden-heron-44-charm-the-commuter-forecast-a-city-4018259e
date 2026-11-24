#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

The forecast moves to Nowhereville, where the weather itself is absurd: umbrellas fall from the sky, gossip blows at 45 mph, and déjà vu is almost guaranteed.
"""
import os

ENTRY = 'Today in Nowhereville: heavy rain of missing umbrellas, gossip winds at 45 mph, and a 90% chance of déjà vu.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
