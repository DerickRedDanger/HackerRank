"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    towers =[m]*n
    
    minimun_amount_move=0
    """
    Both players always move optimally, so we can consider that P2 will always match to P1's movement. 
    Which means that, in the end, what matters is not how tall the towers are, but how many of them there are. 
    This will be the deciding factor for who will run out of moves first.
    """
    
    for i in towers:  # Checking for the minimal amount of moves (decreasing to 1) that can be done
        if i > 1:
            minimun_amount_move += 1
    if minimun_amount_move == 0:  # edge case where all towers are of height 1, meaning P1 wouldn't be able to make a move
        return 2
    # Since P2 will always match P1, if the number of moves is even, P1 will always run out of moves frist
    elif minimun_amount_move %2 == 0:
        return 2
    # But if they are odd, P2 will be the one out of moves
    elif minimun_amount_move %2 != 0: 
        return 1
