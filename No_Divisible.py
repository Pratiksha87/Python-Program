''' Write a program which contains one function that accept one number from user and returns true if number
is divisible by 5 otherwise return false. '''

def Fun():
    Num=int(input())
    if Num % 5 == 0:
        return True
    else:
        return False

ret=Fun()
print(ret)