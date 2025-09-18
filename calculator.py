import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by 0."
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot take the square root of a negative number."
    return math.sqrt(x)


def calculator():
    print("Calculator")
    print("Please choose one of the following functions (1-6):")
    print("1 : Add")
    print("2 : Subtract")
    print("3 : Multiply")
    print("4 : Divide")
    print("5 : Power")
    print("6 : Square Root")

    choice = input("Option : ")

    if choice == '6':
        x = float(input("Enter the number: "))
        print(square_root(x))

    elif choice in ['1', '2', '3', '4', '5']:
        x = float(input("Enter your first number: "))
        y = float(input("Enter your second number: "))

        if choice == '1':
            print(add(x, y))

        elif choice == '2':
            print(subtract(x, y))

        elif choice == '3':
            print(multiply(x, y))

        elif choice == '4':
            print(divide(x, y))

        elif choice == '5':
            print(power(x, y))

    else:
        print("Invalid choice. Please pick 1-6.")


calculator()