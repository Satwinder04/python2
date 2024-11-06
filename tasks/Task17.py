# Task 17
#
# Write a program that checks if a student is eligible for admission to a specific course. The criteria for eligibility are:
# •	The student must have scored at least 80% in math and 70% in science.
# •	Or they must have a total average score of at least 75%.

mathMarks=int(input("Enter math Marks "))
ScienceMarks=int(input("Enter math Science "))

av = (mathMarks+ScienceMarks)/2

if mathMarks>=80 and ScienceMarks>=70 and av>70:
    print("Student is eligble")
else:
    print("Student is not Eligible")