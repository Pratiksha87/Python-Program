''' Write a program which accept number from user and print that number of “*” on screen'''

def Fun():
    Num = int(input("Enter the number: "))
    for i in range(Num):
        print('*', end=' ')

Fun()