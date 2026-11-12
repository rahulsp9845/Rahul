import re
import csv
import os

FILE = "CAIAS_Students.csv"

# Create database if it does not already exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Class", "Email", "Roll Number", "Phone"])


def register_student():
    print("\n======================================")
    print("       CAIAS STUDENT REGISTRATION")
    print("======================================")

    name = input("Enter Student Name: ").strip()
    student_class = input("Enter Class (BCA/BBA/BCOM): ").strip().upper()
    email = input("Enter College Email: ").strip().lower()
    roll = input("Enter College Roll Number: ").strip().upper()
    phone = input("Enter Phone Number: ").strip()

    # Input validation
    if not name:
        print("Error: Name cannot be empty!")
        return

    if student_class not in ["BCA", "BBA", "BCOM"]:
        print("Error: Invalid class!")
        return

    if not re.fullmatch(r"[a-zA-Z0-9._%+-]+@bca\.caias\.in", email):
        print("Error: Enter a valid CAIAS college email!")
        return

    if not re.fullmatch(r"\d{2}[A-Z]{3}\d{3}", roll):
        print("Error: Invalid roll number! Example: 26BCA126")
        return

    if not re.fullmatch(r"[6-9]\d{9}", phone):
        print("Error: Enter a valid 10-digit phone number!")
        return

    # Check for duplicate roll numbers
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        students = list(csv.DictReader(f))

    for student in students:
        if student["Roll Number"] == roll:
            print("Error: Student already registered!")
            return

    # Save student details
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, student_class, email, roll, phone])

    # Display registration result
    print("\n======================================")
    print("       REGISTRATION SUCCESSFUL!")
    print("======================================")
    print("Student Name :", name)
    print("Class        :", student_class)
    print("Email        :", email)
    print("Roll Number  :", roll)
    print("Phone Number :", phone)
    print("======================================")
    print("       STUDENT REGISTERED!")
    print("======================================")
    print("             Made by Rahul")
    print("======================================")


def view_students():
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        students = list(csv.DictReader(f))

    print("\n========== REGISTERED STUDENTS ==========")

    if not students:
        print("No students registered yet.")

    for student in students:
        print("\nName:", student["Name"])
        print("Class:", student["Class"])
        print("Email:", student["Email"])
        print("Roll Number:", student["Roll Number"])
        print("Phone:", student["Phone"])

    print("\nTotal Students:", len(students))


def main():
    while True:
        print("\n1. Register Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("\nThank you!")
            print("Project developed by Rahul.")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
