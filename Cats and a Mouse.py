#___________________________________________ @AbhijeetK1N6 ______________________________________________

#!/bin/python3

import math
import os
import random
import re
import sys
#___________________________________________________________________________________________________________
# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    x_z=x-z
    y_z=y-z
    
    for i in range(q):
        if abs(x_z) > abs(y_z):    #abs() gives absolute values
            return "Cat B"         #i.e. it removes -ve sign from the number
        elif abs(y_z) > abs(x_z):   
            return "Cat A"
        elif abs(x_z) == abs(y_z):
            return "Mouse C"
        
#_____________________________________________________________________________________________________________
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
#_______________________________________________________________________________________________________________________________
