def calculator():
    print("Welcome to Basic Calculator")
    print("Type 'AC' to clear, or 'exit' to quit\n")

    while True:
        first = input("Enter first number: ")
        if first.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
        elif first.upper() == 'AC':
            continue
        elif not first.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a number.")
            continue

        operator = input("Enter operator (+, -, *, /): ")
        if operator not in ['+', '-', '*', '/']:
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

            print("Result:", result)
        except ZeroDivisionError:
            print("Error: Division by zero not allowed.")

# Run the calculator
calculator()
