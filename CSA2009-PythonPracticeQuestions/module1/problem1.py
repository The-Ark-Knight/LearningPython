"""
A simple program to do a bunch of things:

calculator program
"""

def input():
    num1 = int(input("Enter the first number :: "))
    num2 = int(input("Enter the second number :: "))
    return num1, num2

def addition(num1 = 0, num2 = 0):
    return num1 + num2

def subtraction(num1 = 0, num2 = 0):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def main():
    num1, num2=input()
    print(f"Addition of {num1} and {num2} is {addition(num1, num2)}")


main()