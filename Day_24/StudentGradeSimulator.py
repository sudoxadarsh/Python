"""
Problem statement
Ek Python program banao jo student ke 5 subjects ke marks input le,
total aur percentage calculate kare, aur final grade display kare.
Requirements
1. Student ka naam input lo.
2. 5 subjects ke marks input lo — har subject 100 marks ka hai.
3. Marks sirf 0–100 ke beech accept karo.
4. Agar user abc, -5, ya 110 enter kare, toh error message dikhao aur 
   us subject ke marks dobara maango.
5. Total marks aur percentage calculate karo.
6. Percentage ke basis par grade decide karo.
7. Student ka result print karo.


Grade criteria
Percentage	Grade
90–100%	A+
80–89.99%	A
70–79.99%	B
60–69.99%	C
40–59.99%	D
Below 40%	Fail


example output:

Enter student name: Rahul

Enter marks for Subject 1: 85
Enter marks for Subject 2: 92
Enter marks for Subject 3: 78
Enter marks for Subject 4: 66
Enter marks for Subject 5: 89

===== STUDENT RESULT =====
Name: Rahul
Total Marks: 410 / 500
Percentage: 82.0%
Grade: A
Result: Pass


Rules for your solution
- while loop use karna.
- if-elif-else use karna.
- try-except ValueError se invalid numeric input handle karna.
- Abhi functions, classes, lists, aur external libraries use mat karna.
  Har subject ke marks ke liye separate variables use karo.
- AI se code generate mat karwana. Khud logic likho; error aaye toh 
  error message aur apna code bhejna.

"""
subject_marks = []
marks_sum = 0
# Student Grade Simulator


print("Enter student name: ", end="")

while True:
    try:
        student_name = input()
        break
    except ValueError:
        print("enter valid student name: ", end="")
        continue

for i in range(5):
    print("Enter marks for subject", end="")
    while True:
        try:

            subject_mark = int(input(f" {i + 1}: "))
            
            if 0 <= subject_mark <= 100:
                subject_marks.append(subject_mark)
                marks_sum += subject_mark
                break

            print("Enter correct marks for subject in range of 0 <= subject_mark <= 100", end="")

            continue

        except ValueError:
            print("Enter marks correctly!", end="")
            continue

print("\n\n\n===== STUDENT RESULT =====")
print(f"Name: {student_name}")
print(f"Total marks: {marks_sum} / 500")



for i in subject_marks:
    if i < 33:
        count += 1

if count >=2:
    Remark = "F"
    grade = "Fail"



percentage = (marks_sum / 500) * 100

grade = ""
remark = ""
count = 0


print(f"Percentage: {(percentage)}%")

if percentage >= 90:
    grade = "A+"
    remark = "Pass"
elif percentage >= 80:
    grade = "A"
    remark = "Pass"
elif percentage >= 70:
    grade = "B"
    remark = "Pass"
elif percentage >= 60:
    grade = "C"
    remark = "Pass"
elif percentage >= 40:
    grade = "D"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"

print(f"Grade: {grade}")
print(f"Result: {remark}")