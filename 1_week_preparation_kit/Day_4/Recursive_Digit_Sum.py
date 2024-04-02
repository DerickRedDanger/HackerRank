"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    
    sum=0

    # summing before multiplaying to avoid dealing with large numbers
    for number in n:
        sum+=int(number)
        
    n=sum
    n=n*k
    n=str(n)
    lenght=len(n)

    # while n's Length is > 1
    while lenght > 1:
        sum=0
        for i in n:
            sum+=int(i)
            
        n=sum
        n=str(n)
        lenght=len(n)
    
    return n
