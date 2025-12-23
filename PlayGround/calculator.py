def operation_logger(func):
    def wrapper(a, b, operator):
        print(f"Performing operation: {a} {operator} {b}")
        result = func(a, b, operator)
        print(f"Result of operation: {result}")
        return result
    return wrapper

@operation_logger
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator!"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, op)
print("Result:", result)