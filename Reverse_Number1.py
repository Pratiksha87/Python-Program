'''.Write a program which accept number from user and check whether that number is positive or negative or zero. '''

def Fun():
    Num=int(input())
    if Num>0:
        if Num == 0:
            print('zero')
        else:
            print('positive')
    else:
        print('negative')
Fun()