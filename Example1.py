import os

def substract(x, y):
    result = int(x) - int(y)
    return result

def add(x, y):
    result = int(x) + int(y)
    return result

def multiply(x, y):
    result = int(x) * int(y)
    return result

def split(x, y):
    result = int(x) / int(y)
    return result

def enterNumber(label):
    res = False
    number = 0

    while (res == False):
        number = input(label)
        res = number.isnumeric()
        print("Incorrect format, try again...")

    return number

print("Hello world...")
number1 = enterNumber("Enter number 1:")
number2 = enterNumber("Enter number 2:")
print("\nAdd result is ", add(number1, number2))
print("Substract result is ", substract(number1, number2))
print("Multiply result is ", multiply(number1, number2))
print("Split result is ", split(number1, number2))
