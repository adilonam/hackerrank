#!/bin/python3

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

def biggerIsGreater(w):
    w = list(w)
    n = len(w)
    for i in range(n-1, 0, -1):
        if w[i] > w[i-1]:
            break

if __name__ == '__main__':
    

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)


