"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-no-prefix-set/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    checked_words=set()
    prefix=set()
    
    for word in words:
        if word in prefix:
            print("BAD SET")
            print(word)
            return
        for i in range(1, len(word)+1):
            prefix.add(word[:i])
            if word[:i] in checked_words:
                print("BAD SET")
                print(word)
                return
        checked_words.add(word)
    print("GOOD SET")
    return