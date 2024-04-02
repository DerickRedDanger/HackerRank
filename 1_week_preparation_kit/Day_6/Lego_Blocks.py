"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    
    layouts = [0, 1, 2, 4, 8]  # total number of possible layouts for 1xm up to m=4 (notice that Layouts[0] is to a layout of 1x0)
    
    total_layouts = [0, 1] + [0] * (m-1)  # Total number of layouts for nxm
    
    module = 10**9+7
    
    solid = [0, 1]+[0]*(m-1)  # solid layouts for nxm
    
    # Edge cases:
    if m == 1:
        return 1  # since a block of 1 doesn't have any a vertical break
        
    if n == 1:  # if only 1 row
        if m < 5:
            return 1  # since below 5, the only way to make a wall without break is using a single block
        else:
            return 0  # since any combination would have a straight vertical break
            
    # normal cases:
    if m >= 5:
        layouts += [0]*(m-4)  # total number of possible layouts(good and bad) to form a 1xm
    
    # finding the total number of layouts
    for i in range(2, m+1):
        
        # The total number of layouts for a width I is the same as the sum of the N layouts that came before it. In this case, since we are using 4 different blocks, that N = 4.
        if i >= 5:
            layouts[i] = layouts[i-1] + layouts[i-2] + layouts[i-3] + layouts[i-4]
        
        # the total number of layouts is the number of possible layouts for a 1xm to the power of n. We are using module in the power and not in the end to ensure we won't get a overflow in the middle of the operation.
        total_layouts[i] = pow(layouts[i], n, module)

        
    # Finding the number of solid layout
    for i in range(2, m+1):
        # To find the number of solid wall, we need to first find the number of non solid ones
        non_solid = 0
        
        # To do that we will use our knowledge of solid and total layouts.
        # Imagine a layout with a width I, a non solid one would, at least, one straight line from top to bottom. If we fix that line on the first block, and slowly moves it toward the last, we'd have solid layout to the left on the width J(since the straight line is after the solid layout, not in it), then we'd have all possible layour of width I-J to the right (considering all the solid and non Solid layout).
        # By moving that line to the right and summing all non solid layouts, we will get the total number of non solid layouts for a width I.
        for j in range(1, i):
            non_solid += solid[j] * total_layouts[i-j]
        
        # Then, to find the number of solid ones, we just have to reduce the non solid from the total number of layouts
        solid[i] = (total_layouts[i]-non_solid) % module

    
    return solid[m]