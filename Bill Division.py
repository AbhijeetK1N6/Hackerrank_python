
"""
Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume.
Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2,4,6] . Anna declines to eat item k=bill[2] which costs 6.
If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of bill[2], he will calculate (2+4+6)/2=6.
In the second case, he should refund 3 to Anna.


Input Format

The first line contains two space-separated integers n and k, the number of items ordered and the 0-based index of the item that Anna did not eat.
The second line contains n space-separated integers bill[i] where 0<=i<n.
The third line contains an integer, b, the amount of money that Brian charged Anna for her share of the bill.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    bill.remove(bill[k])
    temp=0
    for i in range(n-1):
        temp=temp+bill[i]
        i+=1
    d=temp/2
    
    if d==b:
        print("Bon Appetit")
    else:
        s=d-b
        print(abs(int(s)))
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
