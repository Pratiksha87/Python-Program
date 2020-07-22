'''Write a program which accept one number and display below pattern.
Input : 5
Output :
* * * * *
* * * *
* * *
* *
*'''

def Fun():
    Num=int(input("Enter the number: "));
    for i in range(0,Num):
        for j in range(1,Num):
            if( i<j ):
                print("*",end=' ')
        print("*")
Fun()