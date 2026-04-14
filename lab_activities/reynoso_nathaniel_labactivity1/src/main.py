# -----------------------------------------------------------------
# File in src/main.py
# Main file wherein three functions were made for three test cases.
# Add, Subtract, and Multiply function were used to test.
# -----------------------------------------------------------------


def add(a, b):
    return a + b
"""Adds two numbers"""

def subtract(a, b):
    return a - b
"""Subtracts two numbers"""

def multiply(a, b):
    return a * b
"""Multiplies two numbers"""

# Workaround for using onecompiler to run tests.py
if __name__ == '__main__':
    import os
    os.system("python3 tests.py")