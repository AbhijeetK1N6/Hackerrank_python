"""
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25.
There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

Input Format:-
The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
The second line contains a single word consisting of lowercase English alphabetic letters.

Returns:-
int: the size of the highlighted area
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#
####################################################
def designerPdfViewer(h, word):
    # Write your code here
    a1=list(word)    #string to word
    a2=[]            #Taken an Empty List
    for i in range(0,len(a1)):
        ck=ord(a1[i])-97    #((ASCII Code of Char) - 97) will result the index count from 0 to 1
        a2.append(h[ck])    #Taking and appending the value of found index from given index into created array a2[]
        i+=1
#-----@AbhijeetK1N6--------        
    a2.sort()          #sorted a2[]
    a2.reverse()       #Taken Tallest Height(Largest Number) in 0th index
    multa=a2[0]*len(word)   #Area Calculation 
    return multa
    ######################################################
        
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
