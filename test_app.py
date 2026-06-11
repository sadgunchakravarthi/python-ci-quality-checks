"""Unit tests for the calculator application."""

import pytest, os

# import os ---> to test how ruff check . work
from app import add, divide, multiply, subtract, validate_number


def test_add_two_numbers():
    """Test adding two numbers."""
    assert add(2, 3) == 5


def test_subtract_two_numbers():
    """Test subtracting two numbers."""
    assert subtract(10, 4) == 6


def test_multiply_two_numbers():
    """Test multiplying two numbers."""
    assert multiply(3, 5) == 15


def test_divide_two_numbers():
    """Test dividing two numbers."""
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    """Test that division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


def test_validate_number_accepts_int_and_float():
    """Test that valid numeric input is accepted."""
    assert validate_number(10) == 10
    assert validate_number(3.5) == 3.5


def test_validate_number_rejects_string():
    """Test that string input raises a TypeError."""
    with pytest.raises(TypeError, match="Value must be an int or float"):
        validate_number("10")
