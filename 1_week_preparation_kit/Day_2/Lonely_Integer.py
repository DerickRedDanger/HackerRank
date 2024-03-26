"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    lonely=""
    
    for i in range(len(a)):
        duo=False
        
        for j in range(len(a)):
            
            if i != j and a[i] == a[j]:
                duo=True
                break
                
        if duo is True:
            duo=False
        
        else:
            lonely = a[i]
            break
            
    return lonely
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
