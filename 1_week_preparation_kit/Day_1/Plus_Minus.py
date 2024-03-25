"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    #----
    # My code 

    length=len(arr)
    positive=0
    negative=0
    zero=0

    for x in arr:

        if x < 0:
            negative=negative+(1/length)

        elif x > 0:
            positive=positive+(1/length)

        elif x == 0:
            zero=zero+(1/length)

    # :.6f is formating the print so it shows the variable with exctly 6 digits after the decimal point.
    print(f"{positive:.6f}")
    print(f"{negative:.6f}")
    print(f"{zero:.6f}")
        
    #----

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)