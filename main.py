#!/usr/bin/env python3
"""The Excuse That Almost Works - writes the gamer excuse to /output/entry.txt.

Gate: one line, at most 20 words, 1-140 characters, plain text, no signature.
The excuse below is 20 words / 109 characters / 111 bytes.
"""
import os

EXCUSE = "They cut my street's power for repairs, so I'm guarding the fridge — its backup battery only runs my console."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
