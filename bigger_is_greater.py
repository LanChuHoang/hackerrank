#!/bin/python3
# https://www.hackerrank.com/challenges/bigger-is-greater/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def convert_word_to_base26(word):
    base26 = []
    for char in word:
        base26.append(ord(char))
    return base26


# print(convert_word_to_base26("mdmsy"))


def find_last_non_increasing_suffix_index(char_list: list):
    for i in range(len(char_list) - 1, 0, -1):
        if char_list[i] > char_list[i - 1]:
            return i


def find_next_largest_char_index(char_list: list, left_most_char: str):
    for i in range(len(char_list) - 1, 0, -1):
        if char_list[i] > left_most_char:
            return i


def biggerIsGreater(w):
    # Write your code here
    char_list = list(w)
    pivot = find_last_non_increasing_suffix_index(char_list)
    if not pivot:
        return "no answer"
    left_most_char = char_list[pivot - 1]
    next_largest_char_index = find_next_largest_char_index(char_list, left_most_char)
    temp = char_list[pivot - 1]
    char_list[pivot - 1] = char_list[next_largest_char_index]
    char_list[next_largest_char_index] = temp
    return "".join(char_list[:pivot] + sorted(char_list[pivot:]))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + "\n")

    fptr.close()
