# Author: Hikmet Tenis
# Date: 07/28/2024
# Description: Calculating Grades

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade,
# and a message stating whether the student is passing.

# Average   Grade
# 90+   A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59  F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

# Taking input for the three exam grades and converting them to integers
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

# Creating a list of grades
grades = [exam_one, exam_two, exam_three]

# Calculating the sum of grades
total = sum(grades)

# Calculating the average of grades
avg = total / len(grades)
avg = round(avg)
# Determining the letter grade based on the average
if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:
    letter_grade = "B"
elif 70 <= avg < 80:
    letter_grade = "C"
elif 60 <= avg < 70:
    letter_grade = "D"
else:
    letter_grade = "F"

# Printing the grades, average, and letter grade
print("Exams: " + str(exam_one) +", "+ str(exam_two) +", "+ str(exam_three))

print("Average: " + str(avg))
print("Grade: " + letter_grade)

# Printing if the student is passing or failing
if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
