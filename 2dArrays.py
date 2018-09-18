#!/bin/python3

import math
import os
import random
import re
import sys


def hgSum(center_row, center_col, matrix):
    sum = 0
    sum = (matrix[center_row - 1][center_col - 1]
         + matrix[center_row - 1][center_col]
         + matrix[center_row - 1][center_col + 1]
         + matrix[center_row][center_col]
         + matrix[center_row + 1][center_col - 1]
         + matrix[center_row + 1][center_col]
         + matrix[center_row + 1][center_col + 1]
         )

    return sum


if __name__ == '__main__':
    arr = []
    max_sum = -63
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(1, 5):
        for j in range(1, 5):
            hourGlassSum = hgSum(i, j, arr)
            if max_sum < hourGlassSum:
                max_sum = hourGlassSum

    print (max_sum)
