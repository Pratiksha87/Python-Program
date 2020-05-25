'''.Create on module named as Module_Pro which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for
 multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on
  python program which call all the functions from Arithmetic module by accepting the parameters from user. '''

import Module_Pro

Num1=int(input('Enter first number: '))
Num2=int(input('Enter second number: '))
Module_Pro.Add(Num1,Num2)
Module_Pro.Sub(Num1,Num2)
Module_Pro.Mult(Num1,Num2)
Module_Pro.Div(Num1,Num2)