def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # py2 needs to convert either the numerator or denominator float
    # in order to produce the correct result from divisions
    y *= 1.0
    if y == 0:
        return "Sorry, cannot divide by zero!"
    return x / y