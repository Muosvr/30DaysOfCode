#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalSwaps = 0
for i in range(n):
    innerSwaps = 0
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            innerSwaps += 1
            totalSwaps += 1
    if innerSwaps == 0:
        break
print("Array is sorted in {} swaps.".format(totalSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
