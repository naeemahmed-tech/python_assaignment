# Student Grade Calculator

# Take student name as input
student_name = input("Enter student name: ")

# Take marks for three subjects
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate total and average marks
total_marks = mark1 + mark2 + mark3
average_marks = total_marks / 3

# Determine grade
if average_marks >= 80:
    grade = "A+"
elif average_marks >= 70:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
elif average_marks >= 50:
    grade = "C"
else:
    grade = "F"

# Display student result
print("\n----- Student Result -----")
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks:g}")
print(f"Average: {average_marks:.2f}")
print(f"Grade: {grade}")
