# Filename: divide.py

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Usage Example
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error: Cannot divide by zero
