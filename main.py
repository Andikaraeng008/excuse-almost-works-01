#!/usr/bin/env python3
"""The Excuse That Almost Works - writes the gamer excuse to /output/entry.txt.

Gate: one line, at most 20 words, 1-140 characters, plain text, no signature.
Excuse 4, 101 characters, 19 whitespace-separated tokens — within the 20-word gate under both counting methods.
"""
import os

EXCUSE = "I told work my grandmother died—she did, in 2019, but grief has no expiry date, and neither does GTA."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
