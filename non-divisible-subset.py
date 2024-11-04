#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#




def check_array(s, k):
    def remove_index(arr, index):
        return [arr[i] for i in range(len(arr)) if i != index]

    def helper(s, k):
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if (s[i] + s[j]) % k == 0:
                    return max(helper(remove_index(s, i), k), helper(remove_index(s, j), k))
        return len(s)

    return helper(s, k)



def nonDivisibleSubset(s , k):
    index = 0
    check = check_array(s, k)
    return check
    




if __name__ == '__main__':
 
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(s, k)


    fptr.write(str(result) + '\n')

    fptr.close()
