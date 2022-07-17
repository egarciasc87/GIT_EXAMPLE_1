import os

def substract(x, y):
    result = int(x) - int(y)
    return result

def add(x, y):
    result = int(x) + int(y)
    return result

print("Kello world...")
number1 = input("Enter number 1:")
number2 = input("Enter number 2:")
print("Add result is ", add(number1, number2))
print("Substract result is ", substract(number1, number2))
