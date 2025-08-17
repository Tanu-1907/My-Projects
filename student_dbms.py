import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change to your MySQL username
    password="phoenix",  # change to your MySQL password
    database="student_db"
)
cursor = conn.cursor()

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    marks = int(input("Enter Marks: "))

    query = "INSERT INTO students (name, age, department, marks) VALUES (%s, %s, %s, %s)"
    values = (name, age, dept, marks)
    cursor.execute(query, values)
    conn.commit()
    print("✅ Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n--- Student Records ---")
    for row in rows:
        print(row)

def search_by_department():
    dept = input("Enter Department to search: ")
    query = "SELECT * FROM students WHERE department = %s"
    cursor.execute(query, (dept,))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("⚠️ No students found in this department")

def update_marks():
    student_id = int(input("Enter Student ID to update marks: "))
    new_marks = int(input("Enter New Marks: "))
    query = "UPDATE students SET marks = %s WHERE id = %s"
    cursor.execute(query, (new_marks, student_id))
    conn.commit()
    print("✅ Marks updated successfully!")

def delete_student():
    student_id = int(input("Enter Student ID to delete: "))
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("✅ Student deleted successfully!")

def menu():
    while True:
        print("\n====== Student Database Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search by Department")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_by_department()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice, try again!")

# Run menu
menu()

# Close connection
cursor.close()
conn.close()
