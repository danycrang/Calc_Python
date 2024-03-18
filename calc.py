# simple calculator made in python
# added a while loop to better simulate a traditional calculator

on = True
def add():
    a = float(input("Enter a number:"))
    b = float(input("Enter a second number:"))
    print("Result is: {}".format(a+b))


def subtraction():
    a = float(input("Enter a number:"))
    b = float(input("Enter a second number:"))
    print("Result is: {}".format(a-b))


def multiply():
    a = float(input("Enter a number:"))
    b = float(input("Enter a second number:"))
    print("Result is {}".format(a*b))


def divide():
    a = float(input("Enter a number:"))
    b = float(input("Enter a second number:"))
    print("Result is {}".format(a/b))

while on:
    print("Calculator:")
    operation = input("Choose the operation: + , - , * , / , q")
    if operation == "+":
        add()
    elif operation == "-":
        subtraction()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "q":
        print("Calculator app has been stopped.")
        on = False
    else: print("This is not available.")
