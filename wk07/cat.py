#! /usr/bin/env python3

import sys

def myfun():
    print("this is a function")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("-")

    filenames = sys.argv[1:]
    line_nums = False
    # -n can be anywhere:
    if "-n" in filenames:
        filenames.remove("-n")
        line_nums = True


    for filename in filenames:
        try:
            if filename == "-":
                stream = sys.stdin
            else:
                stream = open(filename)

            n = 1
            for line in stream:
                if line_nums:
                    sys.stdout.write(str(n) + "\t")
                sys.stdout.write(line)
                n += 1
                # for -v, use chr to check the values of unprintable characters

            if stream != sys.stdin:
                stream.close()

        except IOError as e:
            print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
        # other errors : except OtherError as e: