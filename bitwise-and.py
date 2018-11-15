#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        s = [i for i in range(1, n+1)]
        result = 0
        for A in s:
            for B in s:
                if A != B and A&B < k and A&B > result:
                    result = A&B
        print(result)
