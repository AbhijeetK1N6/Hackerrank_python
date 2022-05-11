#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    a,b,c=0,0,0
    for i in range(len(arr)):
        if arr[i]>0:
            a+=1
        elif arr[i]<0:
            b+=1
        elif arr[i]==0:
            c+=1
    print(float(a/n))
    print(float(b/n))
    print(float(c/n))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
