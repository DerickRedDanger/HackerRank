"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem
"""

#!/bin/python3
import time
import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    
    # frequency array with 100 elements (from 0 to 99)
    length = 100
    Counting_Sort=[0] * length

    for i in arr:
        Counting_Sort[i] += 1

    return Counting_Sort