# Filename: arithmetic_operations.py

def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Usage Example
print(arithmetic_operation(10, 5, '+'))  # Output: 15
print(arithmetic_operation(10, 5, '/'))  # Output: 2.0
print(arithmetic_operation(10, 0, '/'))  # Output: Error: Division by zero
