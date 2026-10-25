import datetime as d
print("-" * 20)
name = input("Enter name of student: ")
admission_year = d.datetime.now().year
course = input("Enter course student enrolled: ")
gender = input("Enter geneder male/female/other: ")

studentID = course[0] + name[0] + name[-1] + str(admission_year)

print(f"Student ID    : {studentID}")
print(f"Student Name  : {name}")
print(f"Admission Year: {admission_year}")
print(f"Course        : {course}")
print(f"Gender        : {gender}")
