#! /usr/bin/env python3

def main():
    to_upper_dict = {}
    for i in range(26):
        to_upper_dict[chr(ord('a') + i)] = chr(ord('A') + i)
    
    print_dict(to_upper_dict)

    # print(to_upper_dict.values())


def print_dict(d):
    # default iterator is the keys
    # use d.values() to get values (as an object)
    # "" d.keys()
    print(f"[key] => value")
    for key in d:
        print(f"[{key}] => {d[key]}")


if __name__ == "__main__":
    main()