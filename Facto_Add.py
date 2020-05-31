''''Write a program which accept one number form user and return addition of its factors. '''

import math

def divSum(n):

    result = 0

    for i in range(2, (int)(math.sqrt(n)) + 1):

        if (n % i == 0):
            if (i == (n / i)):
                result = result + i
            else:
                result = result + (i + n // i)

    return (result + n + 1)


n = int(input ("Enter the number: "))
print(divSum(n))

