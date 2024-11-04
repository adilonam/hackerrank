#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def generate_magic_squares():
    all_magic_squares = [
        [
            [8, 1, 6],
            [3, 5, 7],
            [4, 9, 2]
        ],
        [
            [6, 1, 8],
            [7, 5, 3],
            [2, 9, 4]
        ],
        [
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ],
        [
            [2, 9, 4],
            [7, 5, 3],
            [6, 1, 8]
        ],
        [
            [8, 3, 4],
            [1, 5, 9],
            [6, 7, 2]
        ],
        [
            [4, 3, 8],
            [9, 5, 1],
            [2, 7, 6]
        ],
        [
            [6, 7, 2],
            [1, 5, 9],
            [8, 3, 4]
        ],
        [
            [2, 7, 6],
            [9, 5, 1],
            [4, 3, 8]
        ]
       ]
    return all_magic_squares


def calculate_min_cost(matrix):
    def calculate_cost(m1, m2):
        return sum(abs(m1[i][j] - m2[i][j]) for i in range(3) for j in range(3))

    magic_squares = generate_magic_squares()
    min_cost = float('inf')

    for magic_square in magic_squares:
        cost = calculate_cost(matrix, magic_square)
        if cost < min_cost:
            min_cost = cost

    return min_cost


def formingMagicSquare(s):
    # Write your code here
    return calculate_min_cost(s)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))


    result = formingMagicSquare(s)
    
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
