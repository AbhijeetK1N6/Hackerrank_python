#--------------------------@AbhijeetK1N6---------------

if __name__ == '__main__':
    s = input()
    alphanum=False
    alpha=False
    digit=False
    lrcase=False
    upcase=False
    for each in s:
 #________Coded by @AbhijeetK1N6___________
        if each.isalnum():
            alphanum=True
        if each.isalpha():
            alpha=True
        if each.isdigit():
            digit=True
        if each.islower():
            lrcase=True
        if each.isupper():
            upcase=True
print(alphanum,alpha,digit,lrcase,upcase, sep='\n' )
