
import json
import os

students = {}
subjects = ["Python", "Database", "Mathematics"]
file_name = "students.json"


def load_data():
    global students
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            students = json.load(file)


def save_data():
    with open(file_name, "w") as file:
        json.dump(students, file, indent=4)


def grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"


def add_student():
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    marks = {}
    for subject in subjects:
        while True:
            try:
                mark = float(input(subject + " marks (0-100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")

    students[name] = marks
    save_data()
    print("Student saved successfully!")


def view_students():
    for name, marks in students.items():
        avg = sum(marks.values()) / len(subjects)
        print(f"\n{name}: {marks}")
        print(f"Average: {avg:.1f}% | Grade: {grade(avg)}")


def improvement_advisor():
    name = input("Student name: ").strip()

    if name not in students:
        print("Student not found.")
        return

    marks = students[name]
    print("\n--- IMPROVEMENT REPORT ---")

    for subject, mark in sorted(marks.items(), key=lambda x: x[1]):
        print(f"\n{subject}: {mark}/100")

        if mark < 40:
            print("Priority: High")
            print("Revise basics and practise 10 questions daily.")
        elif mark < 60:
            print("Priority: Medium")
            print("Study weak topics and solve practice questions.")
        elif mark < 75:
            print("Keep improving with weekly tests.")
        else:
            print("Good performance! Practise harder questions.")

    weakest = min(marks, key=marks.get)
    print(f"\nFocus most on: {weakest}")


def target_calculator():
    name = input("Student name: ").strip()

    if name not in students:
        print("Student not found.")
        return

    avg = sum(students[name].values()) / len(subjects)
    target = float(input("Enter target average (0-100): "))

    if not 0 <= target <= 100:
        print("Target must be between 0 and 100.")
    elif avg >= target:
        print("You have already reached your target!")
    else:
        print(f"You need to improve by {target - avg:.1f} percentage points.")


def main():
    load_data()

    while True:
        print("\n--- SMART STUDENT GRADEBOOK ---")
        print("1. Add or update student")
        print("2. View all students")
        print("3. Improvement advisor")
        print("4. Target calculator")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            improvement_advisor()
        elif choice == "4":
            target_calculator()
        elif choice == "5":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
        


