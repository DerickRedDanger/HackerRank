"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    min_bribe = 0
    for I in range(len(q)):

        # Check if the person I is ahead of it's original position by more than 2
        # The person in I was originally in the position I+1 (since it started at 1, not 0)
        if q[I] - (I + 1) > 2:
            print("Too chaotic")
            return
        
        # check how many numbers larger than Q[I] are ahead of Q[I]
        for j in range(max(0, q[I] - 2), I):
            if q[j] > q[I]:
                min_bribe += 1
    
    print(min_bribe)
    