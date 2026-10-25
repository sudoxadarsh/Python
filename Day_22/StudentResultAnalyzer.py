
'''
OM
'''


"""
google
"""

# Enter student's name and marks in 5 subjects,
# then generate a result report.

student_name = input("Enter the student's name: ")

subjects_marks = [] # list
total_marks = 0


"""
for(int i=0;i<=5;i++)
range(start,stop,step)

"""

for i in range(5): 
    while True:
        try:
            marks = float(input(f"Subject {i + 1}: "))

            if 0 <= marks <= 100:
                break

            print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    subjects_marks.append(marks)
    total_marks += marks

# Calculate percentage
percentage = (total_marks / 500) * 100

# Calculate grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Check whether the student passes every subject
passed = True

for mark in subjects_marks:
    if mark < 33:
        passed = False
        break

# Display result report
print("=" * 25)
print("RESULT REPORT")
print("=" * 25)

print(f"Student: {student_name}")
print(f"Subject Marks: {subjects_marks}")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")

if passed:
    print("Final Result: PASS")
else:
    print("Final Result: FAIL")
    print("Sorry! You failed in at least one subject.")

print("=" * 25)
