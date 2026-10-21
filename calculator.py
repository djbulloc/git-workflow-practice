
# Practice program for Git 

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

def power(a, b):
    return a ** b

print(f"Result of Addition: 10 + 5 = {add(10, 5)}")
print(f"Result of Subtraction: 10 - 5 = {subtract(10, 5)}")
print(f"Result of Multiplication: 10 * 5 = {multiply(10, 5)}")
print(f"Result of Division: 10 / 5 = {divide(10, 5)}")