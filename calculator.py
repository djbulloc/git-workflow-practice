def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


print(f"Addition: 10 + 5 = {add(10, 5)}")
print(f"Subtraction: 10 - 5 = {subtract(10, 5)}")
print(f"Multiplication: 10 * 5 = {multiply(10, 5)}")
print(f"Division: 10 / 5 = {divide(10, 5)}")