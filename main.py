import math

def get_number(prompt):
    # to make sure they enter a number, not letters
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

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

    choice = get_number("Option : ")

    if choice == '6':
        x = get_number("Enter the number: ")
        print(square_root(x))

    elif choice in ['1', '2', '3', '4', '5']:    
        x = get_number("Enter the first number: ")
        y = get_number("Enter the second number: ")

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


if __name__ == "__main__":
    calculator()