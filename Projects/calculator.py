import math

def calculator():
    print("Welcome to Basic Calculator with Extra Features")
    print("Available operators: +, -, *, /, %, **")
    print("Type 'sqrt' to calculate square root")
    print("Type 'history' to view previous calculations")
    print("Type 'AC' to clear or 'exit' to quit\n")

    history = []

    while True:
        first = input("Enter first number (or 'sqrt', 'history', 'AC', 'exit'): ")

        if first.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        elif first.upper() == 'AC':
            continue
        elif first.lower() == 'history':
            if history:
                print("Calculation History:")
                for h in history:
                    print(h)
            else:
                print("No history yet.")
            continue
        elif first.lower() == 'sqrt':
            num = input("Enter number for square root: ")
            if not num.replace('.', '', 1).isdigit():
                print("Invalid input. Please enter a number.")
                continue
            result = math.sqrt(float(num))
            print("Result:", result)
            history.append(f"√{num} = {result}")
            continue
        elif not first.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a number.")
            continue

        operator = input("Enter operator (+, -, *, /, %, **): ")
        if operator not in ['+', '-', '*', '/', '%', '**']:
            print("Invalid operator. Try again.")
            continue

        second = input("Enter second number: ")
        if second.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        elif second.upper() == 'AC':
            continue
        elif not second.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a number.")
            continue

        a = float(first)
        b = float(second)

        try:
            if operator == '+':
                result = a + b
            elif operator == '-':
                result = a - b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                if b == 0:
                    raise ZeroDivisionError
                result = a / b
            elif operator == '%':
                result = a % b
            elif operator == '**':
                result = a ** b

            print("Result:", result)
            history.append(f"{a} {operator} {b} = {result}")

        except ZeroDivisionError:
            print("Error: Division by zero not allowed.")

# Run the calculator
calculator()
