#--------------------------@AbhijeetK1N6----------------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#------------------------------------------
def diagonalDifference(arr):
    # Write your code here
    ss=0
    for i in range(n):
        temp_sum=arr[i][i]
        ss=ss+temp_sum
        i+=1
#__Coded_by___@AbhijeetK1N6_______
    tt=0
    for i in range(n):
        temp=arr[i][-1-i]
        tt=tt+temp
        i+=1
    pp=ss-tt
    return abs(pp)
#--------------------------------------------            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
