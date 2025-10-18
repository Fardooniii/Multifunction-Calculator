import sys

# 4 functions for each operation
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    # Make sure you can't divide by zero
    if b == 0:
        print("Error: Cannot divide by zero!")
        sys.exit(1)
    return a / b

def main():
    print("Welcome to the Python Calculator!")
    print("You can perform addition, subtraction, multiplication, or division.")
    print("Type 'quit' anytime to exit.")

# A dictionary for the symbols
    operation_symbols = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/"
    }

    while True:
        operation = input("Choose an operation (addition, subtraction, multiplication, division): ").lower()

        if operation == "quit":
            print("Thank you for using the calculator. Goodbye!")
            break

        if operation not in operation_symbols:
            print("Invalid operation. Please choose: addition, subtraction, multiplication, or division.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid number entered. Please enter numeric values only.")
            continue

        if operation == "addition":
            result = addition(num1, num2)
        elif operation == "subtraction":
            result = subtraction(num1, num2)
        elif operation == "multiplication":
            result = multiplication(num1, num2)
        elif operation == "division":
            result = division(num1, num2)

        # Find the symbol from the dictionary
        symbol = operation_symbols[operation]
        print(f"{num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    main()
