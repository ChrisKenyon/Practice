#!/bin/python3

import math
import os
import random
import re
import sys

def nC3(n):
    if n < 3:
        return 0
    return n * (n-1) * (n-2) // 6

from collections import Counter
# Complete the countTriplets function below.
def countTriplets(arr, r):
    if len(arr) < 3:
        return 0
    counter = Counter(arr)
    trips = 0
    if r > 1:
        for elem in arr:
            trips += counter[elem*r] * counter[elem*r*r]
    else:
        for elem in counter:
            count = counter[elem]
            trips += nC3(count)

    return trips

if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(str(ans) + '\n')
