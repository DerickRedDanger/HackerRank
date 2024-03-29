"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    n=len(s)
    brackets = {"(": ")", "{": "}", "[": "]"}
    test=[]
    
    # If lenght is odd, then the list isn't paired
    if n %2 !=0:
        return "NO"
        
    for i in s:
        # if a opening bracket, append to the test list and increase the N by 1
        if i in brackets:
            test.append(i)
            
        # if a closing one
        elif i in brackets.values():
            
            # check if the list isn't empty and if the last element is a opening bracket of the same kind,
            if test and i == brackets[test[-1]]:
                
                # if it's pop it and reduce N
                test.pop()
                
            # Else, it's not paired.
            else:
                return "NO"
                
    if test:  # Check if the test list is now empty. If it isn't, it's not paired
        return "NO"

    else:
        return "YES"