#!/bin/python3

"""
Link: 
https://www.hackerrank.com/challenges/30-binary-numbers/problem
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    rev_bin = ""
    one_arr = []
    max_one = 0

    while n > 0:
        remainder = n%2
        n = n // 2
        rev_bin += str(remainder)

    one_arr = rev_bin.split('0')

    for i in one_arr:
        if max_one < len(i):
            max_one = len(i)

    print(max_one)
