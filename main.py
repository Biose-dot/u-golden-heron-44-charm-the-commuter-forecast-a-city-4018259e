#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't — make.fun entry.

A weather forecast for Cloudhaven, a city that does not exist: sunny, with a 90% chance of falling streetlamps.
"""
import os

ENTRY = 'Cloudhaven: sunny with a 90% chance of falling streetlamps, so carry an umbrella and a helmet, just in case.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
