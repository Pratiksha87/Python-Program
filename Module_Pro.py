'''.Create on module named as Module_Pro which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for
 multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on
 python program which call all the functions from Arithmetic module by accepting the parameters from user. '''

def Add(Num1,Num2):
    print('Addition: ')
    print(Num1+Num2)

def Sub(Num1,Num2):
        print('Subtraction: ')
        print(Num1-Num2)

def Mult(Num1,Num2):
    print('Multiplication: ')
    print(Num1*Num2)

def Div(Num1,Num2):
    if Num2<=0:
        print('Division: ')
        print('Divide by zero error')
    else:
        print('Division: ')
        print(Num1//Num2)

