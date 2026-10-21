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

print("Operations using a = 10 and b = 5")
print(f"Result of Addition: {add(10, 5)}")
print(f"Result of Subtraction: {subtract(10, 5)}")
print(f"Result of Multiplication: {multiply(10, 5)}")
print(f"Result of Division: {divide(10, 5)}")