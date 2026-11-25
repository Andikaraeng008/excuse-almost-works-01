#!/usr/bin/env python3
"""The Excuse That Almost Works - writes the gamer excuse to /output/entry.txt.

Gate: one line, at most 20 words, 1-140 characters, plain text, no signature.
The excuse below is 19 words / 92 characters / 94 bytes.
"""
import os

EXCUSE = "Plumber's fixing the leak under my sink 8 to 12, so I'm stuck home playing \u2014 I mean waiting."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
