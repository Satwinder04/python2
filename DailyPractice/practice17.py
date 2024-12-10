# 1. Create a program to demonstrate how the issubclass() function works with inheritance.
# class A:
#     pass
# class B(A):
#     pass
# d=issubclass(A,B)
# e=issubclass(B,A)
# print(d)
# print(e)

# 2. Write a Python program to demonstrate single inheritance using a Person class and a derived class Employee.
class Person:
    def m1(self):
        print("Employee")
class Employee(Person):
    def m1(self):
        print("s")
        super().m1()
obj=Employee()
obj.m1()


# 3. Create a base class Shape with a method area. Derive classes Rectangle and Circle from Shape and implement the area method for each.

# 4. Implement a class Product with private attributes price and stock. Use getter and setter methods to ensure the price and stock values cannot be negative.
# 5. Write a Python program to demonstrate how super() can be used to call a parent class
# constructor.
# 6. Write a Python program to demonstrate the use of public, protected, and private access specifiers.
# 7. Create a program to show hierarchical inheritance with a base class Vehicle and derived classes Car and Bike.
# 8. Write a program to show how the is instance() function can be used with inheritance.
# 9. Create a class BankAccount that demonstrates encapsulation by having private attributes account_number and balance. Provide methods to deposit and withdraw money.
# 10. Implement a program to show how to prevent instantiation of an abstract class.
