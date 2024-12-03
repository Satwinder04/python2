# 1. Create a class Person with a constructor that initializes name and age. Print the details of an object.

# class person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
# ob=person("satwinder",23)
# print(ob.name,ob.age)
# 2. Create a class Book that overrides the str method to display book details.
# class book:
#     def __str__(self,bn):
#         self.book_name=bn
# ob=book("harry")
# print(ob.book_name)
#

# 3. Create a class Car and print a message when an object is deleted.
# class car:
#     def __init__(self,b,m):
#         self.brand= b
#         self.model= m
#     def __str__(self):
#         return f"model : {self.model}, brand : {self.brand}"
#
# ob= car("toyota","corolla")
# del ob
# print(ob)
# print(" ob is deleted")
# 4. Create a class Student with properties name and marks.
# Modify and print the updated values.
# class Student:
#     def __init__(self,n,a):
#         self.name=n
#         self.marks=a
#     def modify(self):
#         self.name = "ayushi"
#         self.marks = 12
# ob=Student("satwinder",23)
#
# print(ob.name,ob.marks)
# ob.modify()
# print(ob.name,ob.marks)
#
# # 5. Create a class Animal and instantiate multiple objects to represent different animals.
class Animals:
    def ani(self,n):
        self.name=n
ob=Animals()
ob.ani("elephant")
print(ob.name)
ob.ani("loin")
print(ob.name)
ob.ani("cat")
print(ob.name)
ob.ani("bat")
print(ob.name)
ob.ani("rat")
print(ob.name)
# 6. Create a class Shape with a default constructor that initializes type to "Generic"

# 7. Create a class Rectangle with a method to calculate and return the area.
# 8. Create a class Employee that overrides
# str to format the details.
# 9. Create a class BankAccount with methods to deposit, withdraw, and check balance 10. Create a class ShoppingCart to add, remove, and display items.
# 11. Create a class Library to add, borrow, and display books.
# 12. Create a class Circle with methods to calculate area and circumference.

