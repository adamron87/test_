def add(x, y):
    return x + y
    """Add Function"""

def subtract(x, y):
    return x - y
    """Subtract Function"""

def multiply(x, y):
    return x * y
    """Multiply function"""

def divide(x, y):
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y

print(add(10, 5))
print(subtract(10, 5))