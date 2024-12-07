# Create a class student with instance variables name and grade. Add a method display_info() to print the students name and grade. Create two objects with different data and call the method for both


class Student:
    def display_info(self):
        print(f"The name is {self.name} and the grade is {self.grade}")

ob1 = Student()
ob1.name = "Rahul"
ob1.grade = 89

ob2 = Student()
ob2.name = "Sohit"
ob2.grade = 50

ob1.display_info()
ob2.display_info()



