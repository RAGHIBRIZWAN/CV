students = {
    "K12": {
        "Name": "Raghib",
        "Major": "AI",
        "Grades": [85, 90, 88]
    },
    "K62": {
        "Name": "fahad",
        "Major": "AI",
        "Grades": [92, 87, 95]
    },
    "K23": {
        "Name": "Umar",
        "Major": "AI",
        "Grades": [78, 85, 80]
    },
    "K05": {
        "Name": "Shaheer",
        "Major": "CS",
        "Grades": [88, 91, 90]
    }
}


def highest_average(students):
    best_student = ""
    highest = 0

    for student_id in students:
        grades = students[student_id]["Grades"]
        average = sum(grades) / len(grades)

        if average > highest:
            highest = average
            best_student = students[student_id]["Name"]

    return best_student


def search_by_major(students, major):
    print("\nStudents in", major + ":")

    found = False

    for student_id in students:
        if students[student_id]["Major"].lower() == major.lower():
            print(students[student_id]["Name"])
            found = True

    if not found:
        print("No students found in this major.")


print("Student with the highest average:")
print(highest_average(students))

search_by_major(students, "CS")
search_by_major(students, "AI")
