"""Simple calculator application for CI quality checks."""


def validate_number(value):
    """Validate that the provided value is an int or float."""
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be an int or float")
    return value


def add(a, b):
    """Return the sum of two numbers."""
    validate_number(a)
    validate_number(b)
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    validate_number(a)
    validate_number(b)
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    validate_number(a)
    validate_number(b)
    return a * b


def divide(a, b):
    """Return the result of dividing a by b."""
    validate_number(a)
    validate_number(b)

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


# """Simple calculator application for CI quality checks."""


# def validate_number(value, check_zero=False):
#     """Validate that the provided value is an int or float."""
#     if not isinstance(value, (int, float)):
#         raise TypeError("Value must be an int or float")

#     if check_zero and value == 0:
#         raise ValueError("Cannot divide by zero")

#     return value


# def add(a, b):
#     """Return the sum of two numbers."""
#     validate_number(a)
#     validate_number(b)
#     return a + b


# def subtract(a, b):
#     """Return the difference between two numbers."""
#     validate_number(a)
#     validate_number(b)
#     return a - b


# def multiply(a, b):
#     """Return the product of two numbers."""
#     validate_number(a)
#     validate_number(b)
#     return a * b


# def divide(a, b):
#     """Return the result of dividing a by b."""
#     validate_number(a)
#     validate_number(b, check_zero=True)
#     return a / b
