"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[8] == 'A':
        # if 12:00Am, becomes 00:00
        if s[:2] == '12':
            conversion ='00' + s[2:8]
        # else, just remove the Am
        else:
            conversion = s[:8]
        
    else:
        # if 12:00PM, becomes 00:00
        if s[:2] == '12':
            conversion = s[:8]
        # else, just increase hour by 12 and removes Pm
        else:
            time = int(s[:2]) + 12
            conversion = str(time) + s[2:8]

    return conversion

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()