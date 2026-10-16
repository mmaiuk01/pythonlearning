# Get input from the user
name = input("Enter student name: ")
exam1 = int(input("Enter Exam 1 score: "))
exam2 = int(input("Enter Exam 2 score: "))
exam3 = int(input("Enter Exam 3 score: "))

# Step 1: Calculate the average of the three scores
average = (exam1 + exam2 + exam3) / 3

# Step 2: Determine the letter grade using the CS 1300 scale.

if average >= 90:
    grade = "A"
elif average >= 87:
    grade = "A-"
elif average >= 83:
    grade = "B+"
elif average >= 80:
    grade = "B"
elif average >= 77:
    grade = "B-"
elif average >= 73:
    grade = "C+"
elif average >= 70:
    grade = "C"
elif average >= 67:
    grade = "C-"
elif average >= 63:
    grade = "D+"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Step 3: Determine the student's standing
if average >= 90:
    status = "Dean's List"
elif average >= 70:
    status = "Good Standing"
elif average >= 60:
    status = "Academic Probation"
else:
    status = "Academic Suspension Warning"

# Step 4: Print the formatted grade report
print()
print("=" * 28)
print("STUDENT GRADE REPORT".center(28))
print("=" * 28)
print(f"Student: {name}")
print(f"Exam 1:  {exam1}")
print(f"Exam 2:  {exam2}")
print(f"Exam 3:  {exam3}")
print("-" * 28)
print(f"Average: {average:.2f}")
print(f"Grade:   {grade}")
print(f"Status:  {status}")
print("=" * 28)
