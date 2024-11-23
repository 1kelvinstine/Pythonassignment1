# Basic Calculator Program

# Get user input for the first number, second number, and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == "/":
    # Check if the second number is zero to avoid division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter one of the following: +, -, *, /")
5