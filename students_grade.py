# List of students with their grades
students = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 84],
    "Charlie": [75, 85, 95],
    "David": [88, 79, 85]
}

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Open the text file in write mode
with open("student_grades.txt", "w") as file:
    for student, grades in students.items():
        average_grade = calculate_average(grades)
        # Write the student's name and average grade to the file
        file.write(f"{student}: {average_grade:.2f}\n")

print("Student averages have been written to 'student_grades.txt'.")
