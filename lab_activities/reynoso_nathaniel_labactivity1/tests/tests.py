# -----------------------------------------------------------------
# File in tests/tests.py
# Tests the function of the main file.
# -----------------------------------------------------------------

from src import main

def run_tests():
    print("--- Running Automated Tests ---")

    # TEST CASE 1: Addition
    result_add = main.add(10, 5)
    print(f"[TEST 1] Testing Addition: 10 + 5 = {result_add}")
    assert result_add == 15, "ERROR: Addition failed!"

    # TEST CASE 2: Subtraction
    result_sub = main.subtract(20, 8)
    print(f"[TEST 2] Testing Subtraction: 20 - 8 = {result_sub}")
    assert result_sub == 12, "ERROR: Subtraction failed!"

    # TEST CASE 3: Multiplication
    result_mult = main.multiply(7, 6)
    print(f"[TEST 3] Testing Multiplication: 7 * 6 = {result_mult}")
    assert result_mult == 42, "ERROR: Multiplication failed!"

    # When no error occurs, it prints out this string.
    print("\nSUCCESS: All 3 tests passed! OK")

# Run the tests.
if __name__ == '__main__':
    run_tests()
