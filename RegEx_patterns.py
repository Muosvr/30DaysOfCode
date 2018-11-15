#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    list = []

    pattern = r'@gmail.com$';

    for N_itr in range(N):
        firstNameEmailID = input().split(" ")

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search(pattern, emailID, re.M):
            # print("Found email!")
            index = 0
            for name in list:
                if ord(name[0]) < ord(firstName[0]):
                    # print(ord(name[0]), ord(firstName[0]))
                    index += 1
            list.insert(index,firstName)

    # for name in list:
    #     print(name)
    for name in list:
        print(name)
