#! /usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <f1> <f2>")
    exit()

(file1, file2) = sys.argv[1:]

words1 = set()
words2 = set()

# get all words in both files
with open(file1) as f:
    for word in f:
        words1.add(word.strip())

with open(file2) as f:
    for word in f:
        words2.add(word.strip())

diffset = words1.difference(words2)
for word in sorted(diffset):
    print(word)