#! /usr/bin/env python3
# e.g. /usr/bin/python3

import sys

# TODO: write an implementation of head
# name = input("Enter name: ")
# print("Hi there", name +"!")

# number of lines to be printed
# in shell: $1
n_lines = 10

if len(sys.argv) > 1:
    files = sys.argv[2:]
    if sys.argv[1][0] == "-":
        # string slicing to get everything after the "-"
        n_lines = int(sys.argv[1][1:])
    else:
        # slice to get every filename
        files = sys.argv[1:]

for file in files:
    print("\n===", file, "===")
    # this doesn't do error handling currently
    with open(file) as f:
        # outside of this indentation level, the file is automatically closed
        i = 0
        for line in f:
            print(line.strip())
            i += 1
            # break works the same in python
            if i == n_lines:
                break

print("\n=== STDIN ===")
i = 0

# sys.stdin is an iterator (standard input)
for line in sys.stdin:
    print(line.strip())
    i += 1
    # break works the same in python
    if i == n_lines:
        break

