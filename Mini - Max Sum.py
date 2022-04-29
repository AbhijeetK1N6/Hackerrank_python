#-------------------@AbhijeetK1N6---------------------

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
#___________________________________________________________
def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    a,b=0,0
    for i in range(0,len(arr)-1):
        temp1=arr[i]
        a+=temp1
#Coded by @AbhijeetK1N6
    for j in range(1,len(arr)):
        temp2=arr[j]
        b+=temp2
    print(a,b)
 #_____________________________________________________________       

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    

