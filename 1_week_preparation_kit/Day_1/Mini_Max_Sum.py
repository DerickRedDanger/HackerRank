"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr = sorted(arr)
    min=0
    max=0
    for i in range(len(arr)):
        if i == 0:
            min += arr[i]
        elif i == 4:
            max += arr[i]
        else:
            min += arr[i]
            max += arr[i]
    print(min, end=" ")
    print(max)
