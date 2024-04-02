"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    
    heapq.heapify(A)
    operations = 0
    
    # while the least sweet cookie is less sweet then K and we have two or more cookies
    while A[0] <= k and len(A) >= 2:
        combined_cookie = heapq.heappop(A) + 2 * heapq.heappop(A)  # Heappop will pop the smallest value, then the second smallest
        
        heapq.heappush(A, combined_cookie)
        operations+=1
        
    if A[0] >= k:
        return operations
    else:
        return -1