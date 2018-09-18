#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    test = list()
    set_ = set()
    count = 0
    for num in arr:
        if abs(k-num) in set_:
            test.append((k-num,num))
            count += 1
        if abs(k+num) in set_:
            test.append((k+num,num))
            count += 1
        set_.add(num)
    #return count
    return len(set(arr) & set([item + k for item in set(arr)]))


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print(str(result) + '\n')
