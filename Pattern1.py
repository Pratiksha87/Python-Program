''' Write a program which accept one number and display below pattern
Output :  * * * * *
          * * * * *
          * * * * *
          * * * * *
          * * * * * '''

def Fun():
    for i in range(0,5):
        for j in range(1,5):
            print("*",end=' ')
        print("*")
Fun()