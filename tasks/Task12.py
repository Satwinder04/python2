# Task:12
# Write a program that takes a student's marks as input and determines the grade based on the following criteria:
# 	A: Marks greater than or equal to 90
# 	B: Marks between 80 and 89
# 	C: Marks between 70 and 79
# 	D: Marks between 60 and 69
# 	F: Marks below 60

StudentMarks=int(input("Enter Marks of the student 0-100 "))
if StudentMarks>=90:
    print("A: Marks greater than or equal to 90 ",StudentMarks)
if 80<StudentMarks<89:
    print("B: Marks between 80 and 89",StudentMarks)
if 70<StudentMarks<79:
    print("C: Marks between 70 and 79 ",StudentMarks)
if 60<StudentMarks<69:
    print("D: Marks between 60 and 69 ",StudentMarks)
if StudentMarks<60:
    print("F: Marks below 60 ",StudentMarks)
