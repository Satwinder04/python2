# Create a class employee with instance variable name and salary. Add a method update_salary()
# to modify the salary of the employee. Display the updated salary using another meethod.

class Employee:
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self,new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name}.")
    def display_salary(self):
        print(f"The name is {self.name} and the updated salary is {self.salary}")

emp = Employee("Aman", 50000)
emp.display_salary()  # Display initial salary
emp.update_salary(60000)  # Update salary
emp.display_salary()
emp.update_salary(45500)  # Update salary
emp.display_salary()

