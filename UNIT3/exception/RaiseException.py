# RaiseException.py

x, y = 100, 2

try:
    z = x / y
    if z > 10:
        raise ValueError(f"Value too large: {z}")
    print("Result:", z)

except ValueError as e:
    print("Custom Exception Caught:", e)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

finally:
    print("Execution completed")