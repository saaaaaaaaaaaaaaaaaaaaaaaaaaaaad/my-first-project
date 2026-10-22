
students = {}


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = []

    for subject in ["Python", "Database", "Mathematics"]:
        while True:
            try:
                mark = float(input(f"Enter {subject} marks (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")

    students[name] = dict(zip(
        ["Python", "Database", "Mathematics"], marks
    ))
    print("Student added successfully!")


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def view_students():
    if not students:
        print("No student records found.")
        return

    for name, marks in students.items():
        average = sum(marks.values()) / len(marks)
        print(f"\n{name}: {marks}")
        print(f"Average: {average:.2f}")
        print(f"Grade: {calculate_grade(average)}")


def search_student():
    name = input("Enter student name: ").strip()

    if name in students:
        print(name, students[name])
    else:
        print("Student not found.")


def main():
    while True:
        print("\n--- STUDENT GRADEBOOK ---")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
