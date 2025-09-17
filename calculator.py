def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    print("Calculator")
    print("Please choose one of the following functions (1-4):")
    print("1 : Add")
    print("2 : Subtract")
    print("3 : Multiply")
    print("4 : Divide")

    choice = input("Option : ")

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

    else:
        print("Invalid choice. Please pick 1-4.")


calculator()