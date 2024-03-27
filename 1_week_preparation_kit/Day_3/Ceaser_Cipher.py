"""
Original Problem at: https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here

    # Getting the alphabet
    alpha="abcdefghijklmnopqrstuvwxyz"
    
    # The shift can take us past the end of the alphabet, to handle that, we will concatenate it to itself.
    cipher = alpha + alpha
    
    # K can vary between 0 and 100.
    # To keep it between 0 and 26, we will divide it by 26 and use it's remainder
    k = k % 26
    
    # Strings are immutable, so when we concatenate two strings, we actually are creating a third and discarding the first.
    # To avoid creating strings time and time again, we'll append the characters to a list, and only turn it into a single string at the end
    encrypting=[]
    
    for i in s:
        
        # if i is alphabets
        if i.isalpha():
            
            if i.isupper():
                position = alpha.index(i.lower())
                letter = cipher[k + position]
                encrypting.append(letter.upper())
                
            else:
                position = alpha.index(i)
                letter = cipher[k + position]
                encrypting.append(letter)
        else:
            encrypting.append(i)
            
    # turning the list of characters in a single string
    encrypted= "".join(encrypting)
                
    return encrypted
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
