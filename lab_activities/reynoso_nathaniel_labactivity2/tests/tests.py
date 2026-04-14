# -----------------------------------------------------------------------------------
# File: tests.py
# This file tests whether the main python code can really create, update and display.
# -----------------------------------------------------------------------------------

import main

def run_tests():
    print("\n--- Running Lab 2 Automated Tests ---")
    main.display_all()
    # Test 1: Create
    main.add_student("2022103327", "Nathaniel", "njcreynoso@mymail.mapua.edu.ph", "911")
    assert "2022103327" in main.student_db, "Test 1 Failed"
    main.display_all()
    print("[TEST 1] Student Creation: Passed")

    # Test 2: Update
    main.update_grades("2022103327", "90")
    student = main.student_db["2022103327"]
    assert "90" in student["grades"], "Test 2 Failed"
    main.display_all()
    print("[TEST 2] Grade Updating: Passed")

    # Test 3: Display
    db = main.student_db
    assert len(db) == 1, "Test 3 Failed"
    main.display_all()
    print("[TEST 3] Dictionary Retrieval: Passed")

    print("\nSUCCESS: All tests completed! OK")

if __name__ == '__main__':
    run_tests()