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
    # Write your code here
    w = list(w) 
    for i in range(len(w)-2, -1, -1):
        min_char = None
        min_index = None
        for j in range(i+1 , len(w)):
            if w[i] < w[j]:
                if not min_char or w[j] < min_char:
                    min_char = w[j]
                    min_index = j
        if min_char:
            w[i], w[min_index] = w[min_index], w[i]
            w = w[:i+1] + sorted(w[i+1:])
            return ''.join(w) 
    return 'no answer'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
