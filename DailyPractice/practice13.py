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
# class Animals:
#     def ani(self,n):
#         self.name=n
# ob=Animals()
# ob.ani("elephant")
# print(ob.name)
# ob.ani("loin")
# print(ob.name)
# ob.ani("cat")
# print(ob.name)
# ob.ani("bat")
# print(ob.name)
# ob.ani("rat")
# print(ob.name)
# 6. Create a class Shape with a default constructor that initializes type to "Generic"
# class Shape:
#     def __init__(self):
#         print("Gneric")
# Shape()

# 7. Create a class Rectangle with a method to calculate and return the area.
# class Rectangle:
#     def cal(self,l,b):
#         return l*b
# ob=Rectangle()
#
# print(ob.cal(10,20))
# 8. Create a class Employee that overrides str to format the details.
# class Emp:
#     def __init__(self,n,s):
#         self.name=n
#         self.salary=s
#     def __str__(self):
#         return f"name : {self.name}, salary : {self.salary}"
# ob=Emp("Satwidner",12)
# print(ob)
# 9. Create a class BankAccount with methods to deposit, withdraw, and check balance
# class BankAccount:
#     def __init__(self, bal=0):
#         self.bal = bal
#     def dep(self, amt):
#         self.bal += amt
#     def wth(self, amt):
#         if amt > self.bal:
#             print("Insufficient balance")
#         else:
#             self.bal -= amt
#     def bal_chk(self):
#         return self.bal
# bal=int(input("enter the balance "))
# acct = BankAccount(bal)
# dep=int(input("enter the amount to be deposit "))
# acct.dep(dep)
# wth=int(input("enter the amount to be withdrawal "))
# acct.wth(wth)
# print(acct.bal_chk())

# 10. Create a class ShoppingCart to add, remove, and display items.
class ShoppingCart:
    def __init__(self):
        self.items = [1,2,3,4,6,7,8]
    def add(self, item):
        self.items.append(item)
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
    def display(self):
        return self.items
cart = ShoppingCart()
cart.add(5)
cart.add(9)
cart.remove(2)
cart.remove(4)
print(cart.display())

# # 11. Create a class Library to add, borrow, and display books.
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add(self, book):
#         self.books.append(book)
#
#     def borrow(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             return book
#         return None
#
#     def display(self):
#         return self.books
#
# lib = Library()
# lib.add("Python Basics")
# lib.add("Data Structures")
# lib.borrow("Python Basics")
# print(lib.display())
#
# # 12. Create a class Circle with methods to calculate area and circumference.
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def area(self):
#         return 3.14159 * self.r * self.r
#
#     def circ(self):
#         return 2 * 3.14159 * self.r
#
# circle = Circle(5)
# print(circle.area())
# print(circle.circ())

