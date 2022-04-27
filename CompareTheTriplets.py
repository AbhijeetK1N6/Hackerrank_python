#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b): 
    a_score=0
    b_score=0  #initial score of both var is 0
    #starting a for loop till length of array "a"
    for i in range (len(a)):           
        #now following the conditions given in question
        if a[i]>b[i]:
            a_score+=1 #increment the alice's score
        elif a[i] < b[i]:
            b_score+=1 #incremenet the bob's score
        elif a[i]==b[i]:
            a[i]=a[i]
            b[i]=b[i]
    #since we need the outpput in array form
    #[ Alice score , Bob score]
    temp=[a_score,b_score]
    return temp
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
