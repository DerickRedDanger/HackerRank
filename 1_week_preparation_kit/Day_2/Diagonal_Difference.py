"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    # Finding the number of rows/columns
    print(len(arr))
    length=len(arr)
    Primary_Diagonal = 0
    Secondary_Diagonal = 0
    
    for i in range(len(arr)):
        Primary_Diagonal = Primary_Diagonal+arr[i][i]
        
        Secondary_Diagonal = Secondary_Diagonal+arr[i][(length-1)-i]
        
    Diagonal_Difference = abs(Primary_Diagonal-Secondary_Diagonal)
    
    return Diagonal_Difference
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
