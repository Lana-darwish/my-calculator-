def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "wrong, can't divide on zero"
    return a / b


def calculator():
    print("------ Calculator -----")

    num1 = float(input("num1: "))
    num2 = float(input("num2: "))

    print("\nChoose operation:")
    print("1 - Addition")
    print("2 - Subtraction")
    print("3 - Multiplication")
    print("4 - Division")

    choice = input("\nYour choice: ")

    if choice == "1":
        print(f"Result: {add(num1, num2)}")
    elif choice == "2":
        print(f"Result: {subtract(num1, num2)}")
    elif choice == "3":
        print(f"Result: {multiply(num1, num2)}")
    elif choice == "4":
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid choice!")


calculator()  