#!/usr/bin/env python3
"""The Excuse That Almost Works - writes the gamer excuse to /output/entry.txt.

Gate: one line, at most 20 words, 1-140 characters, plain text, no signature.
Excuse 3, 19 words, no em dash — HR flagged the "family emergency", but the cousin in Los Santos really did get shot, twice, by me.
"""
import os

EXCUSE = "HR flagged my 'family emergency', turns out my cousin in Los Santos really did get shot, twice, by me."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
