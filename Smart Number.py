#----------------------------@AbhijeetK1N6-------------------------

"""
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

A number is called a smart number if it has an odd number of factors. Given some numbers, find whether they are smart numbers or not.

Debug the given function is_smart_number to correctly check if a given number is a smart number.

Note: You can modify only one line in the given code and you cannot add or remove any new lines.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The first line of the input contains , the number of test cases.
The next  lines contain one integer each.

The output should consist of  lines. In the  line print YES if the  integer has an odd number of factors, else print NO.
"""

import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val**2 == 1:   #<<--------------
        return True
    return False
#----------Debigged-by-@AbhijeetK1N6-----
for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
