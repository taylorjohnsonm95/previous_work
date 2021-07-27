#!/usr/bin/env python3

import sys

def hamming(string_1, string_2):
    """returns hamming distance between two strings"""
    diffs = 0
    for x1, y1 in zip(string_1, string_2):
        if x1 != y1:
            diffs += 1
    return diffs

if __name__ == "__main__":
    #check for two arguments"
    arg_count = len(sys.argv) - 1
    if arg_count < 2:
        raise Exception("This requires 2 arguments.")
    else:
        string_1 = sys.argv[1]
        string_2 = sys.argv[2]
        result = hamming(string_1, string_2)
        print("{}\t{}\t{}".format(string_1, string_2, result))
