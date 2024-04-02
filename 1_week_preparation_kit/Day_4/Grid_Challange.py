"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    
    N_row=len(grid)

    # keeping track of which row we are sorting
    n=0
    
    for row in grid:
        sorting=[]
        
        for element in row:
            sorting.append(element)
            
        sorting.sort()
        N_columns = len(sorting)
        grid[n] = "".join(sorting)
        n+=1
    
    is_sorted=1
    # Since we are comparing the present row to the next, we have to stop at the one before last,
    # or we'd get an out of range error
    for row in range(N_row-1):
        for column in range(N_columns):
            if grid[row][column]>grid[row+1][column]:
                is_sorted=0
                
    if is_sorted==0:
        return "NO"
        
    else:
        return "YES"