#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    input_num = n
    rev_bin = []
    binary = []
    pre_one = False
    consecutive_one = 0
    cons_array = []
    while n > 0:
        remainder = n%2
        n = n // 2
        rev_bin.append(remainder)
    for i in rev_bin:
        if pre_one == True:
            consecutive_one += 1
        if i == 1:
            pre_one = True
        else:
            pre_one = False
            cons_array.append(consecutive_one)
            consecutive_one = 0

    max_cons_one = max(cons_array)
    print(max_cons_one)
    
