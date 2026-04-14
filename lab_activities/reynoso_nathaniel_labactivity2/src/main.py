# ---------------------------------------------------------------------------------------
# File: main.py
# A menu Python program for students that uses strings, lists, tuples, and dictionaries.
# It also demonstrate the CRUD operations.
# ---------------------------------------------------------------------------------------

student_db = {}
# Dictionary: This acts as the database for all student information. 

# String: Example of these are name or ID.
def add_student(student_id, name, email, phone): 
    """CREATE: Adds a new student to the database."""
    contact_info = (email, phone) 
# Tuple: The contact details of students are in a form of tuple.

    grades = []
# List: The list of grades will be constantly updated. 
    
    student_db[student_id] = {
        "name": name,
        "contact": contact_info,
        "grades": grades
    }

def view_student(student_id):
    """READ: Display the info of the student with the give ID."""
    if student_id in student_db:
        student = student_db[student_id]
        print(f"\n[ID: {student_id}] Name: {student['name']}")
        print(f"Contact: {student['contact']}")
        print(f"Grades: {student['grades']}")
        return student
    print("Error: Student ID not found.")
    return None

def update_grades(student_id, new_grade):
    """UPDATE: This will update a specific student's grade."""
    if student_id in student_db:
        student_db[student_id]["grades"].append(new_grade)
        return True
    return False

def display_all():
    """DISPLAY: This will display all the student data from the database."""
    print("\n--- Current Students ---")
    for sid, info in student_db.items():
        print(f"ID: {sid} | Name: {info['name']} | Grades: {info['grades']}")

def main_menu():
    """The Interactive Menu Loop."""
    while True:
        print("\n=== STUDENT RECORD SYSTEM ===")
        print("1. Add Student")
        print("2. View Student")
        print("3. Add Grade")
        print("4. Display All")
        print("5. Exit Application")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            s_id = input("Enter ID: ")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            phone = input("Enter Phone: ")
            add_student(s_id, name, email, phone)
            print("Student added successfully!")
            
        elif choice == '2':
            s_id = input("Enter ID to search: ")
            view_student(s_id)
            
        elif choice == '3':
            s_id = input("Enter Student ID: ")
            grade = input("Enter Grade: ")
            if update_grades(s_id, grade):
                print("Grade updated!")
            else:
                print("Student not found.")
                
        elif choice == '4':
            display_all()
            
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# They will be able to choose what they want in OneCompiler: 
# either T for testing or M for the interactive menu.
if __name__ == "__main__":
    mode = input("Type 'T' for Tests or 'M' for Menu: ").upper()
    if mode == 'T':
# OneCompiler workaround
        import os
        os.system("python3 tests.py")
    else:
        main_menu()