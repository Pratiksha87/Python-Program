'''Write a program which accept one number from user and return its factorial.'''

def Fun():
    Num=int(input("Enter number: "))
    if Num < 0:
        return 0
    elif Num == 0 or Num == 1:
        return 1
    else:
        fact = 1
        while (Num > 1):
            fact *= Num
            Num -= 1
        return fact

ret=Fun()
print("Factorial: ",ret)

