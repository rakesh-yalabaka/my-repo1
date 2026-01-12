from student import Student

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")

    student = Student(student_id, name, age)
    students.append(student)
    print("✅ Student added successfully!")

def view_students():
    if not students:
        print("⚠️ No students available")
        return

    print("\n📋 Student List:")
    for student in students:
        print(student)

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    global students
    students = [s for s in students if s.student_id != student_id]
    print("🗑️ Student deleted (if existed)")

def main():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting program")
            break
        else:
            print("❌ Invalid choice, try again")

if __name__ == "__main__":
    main()
