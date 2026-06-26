students = {}
def add_student():
    roll = int(input("Enter Roll Number: "))
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = list(map(int, input("Enter 3 Marks: ").split()))
    students[roll] = {
        "name": name,
        "branch": branch,
        "marks": marks
    }
    print("Student Added Successfully!")
def display_students():
    if len(students) == 0:
        print("No students found.")
        return
    for roll, details in students.items():
        avg = sum(details["marks"]) / len(details["marks"])
        print("\n-----------------------")
        print("Roll Number :", roll)
        print("Name        :", details["name"])
        print("Branch      :", details["branch"])
        print("Marks       :", details["marks"])
        print("Average     :", avg)
def search_student():
    roll = int(input("Enter Roll Number: "))
    if roll in students:
        s = students[roll]
        print("\nStudent Found")
        print("Name    :", s["name"])
        print("Branch  :", s["branch"])
        print("Marks   :", s["marks"])
        print("Average :", sum(s["marks"]) / len(s["marks"]))
        print("Highest :", max(s["marks"]))
        print("Lowest  :", min(s["marks"]))
    else:
        print("Student Not Found!")
def update_marks():
    roll = int(input("Enter Roll Number: "))
    if roll in students:
        new_marks = list(map(int, input("Enter New 3 Marks: ").split()))
        students[roll]["marks"] = new_marks
        print("Marks Updated Successfully!")
    else:
        print("Student Not Found!")
def delete_student():
    roll = int(input("Enter Roll Number: "))
    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")
def class_report():
    if len(students) == 0:
        print("No students available.")
        return
    total_students = len(students)
    class_average = 0
    highest_avg = -1
    lowest_avg = 101
    topper = ""
    lowest_student = ""
    for roll, details in students.items():
        avg = sum(details["marks"]) / len(details["marks"])
        class_average += avg
        if avg > highest_avg:
            highest_avg = avg
            topper = details["name"]
        if avg < lowest_avg:
            lowest_avg = avg
            lowest_student = details["name"]
    class_average /= total_students
    print("\n======= CLASS REPORT =======")
    print("Total Students       :", total_students)
    print("Class Average        :", round(class_average,2))
    print("Highest Average      :", highest_avg)
    print("Lowest Average       :", lowest_avg)
    print("Topper               :", topper)
    print("Lowest Performer     :", lowest_student)
while True:
    print("\n========= STUDENT MANAGEMENT SYSTEM =========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Class Report")
    print("7. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        class_report()
    elif choice == 7:
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")
