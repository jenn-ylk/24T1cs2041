#! /usr/bin/env python3

import sys

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <rows> <cols> <width>")
    exit()

(rows, cols, width) = sys.argv[1:]

for row in range(1, int(rows)+1):
    for col in range(1, int(cols)+1):
        print(f"{str(row * col): >{int(width)}}", end="")
    print("")