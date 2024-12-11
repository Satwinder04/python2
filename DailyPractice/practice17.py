# 1. Create a program to demonstrate how the issubclass() function works with inheritance.
# class A:
#     pass
# class B(A):
#     pass
# d=issubclass(A,B)
# e=issubclass(B,A)
# print(d)
# print(e)
from time import sleep


# 2. Write a Python program to demonstrate single inheritance using a Person class and a derived class Employee.
# class Person:
#     def m1(self):
#         print("Employee")
# class Employee(Person):
#     def m1(self):
#         print("s")
#         super().m1()
# obj=Employee()
# obj.m1()


# 3. Create a base class Shape with a method area. Derive classes Rectangle and Circle from Shape and implement the area method for each.
# import math
# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print(f"area of Rect is {self.l*self.b}")
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         print(f"area of Rect is {math.pi*self.r**2}")
#
# r=Rectangle(2,3)
# r.area()
# c=Circle(7)
# c.area()

# 4. Implement a class Product with private attributes price and stock.
# Use getter and setter methods to ensure the price and stock values
# cannot be negative.
#
# class Product:
#     def __init__(self,price,stock):
#         self.__price=price
#         self.__stock=stock
#
#     @property
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self,new_price):
#         if new_price>0:
#             self.__price=new_price
#         else:
#             print("invalid")
#     @property
#     def stock(self):
#         return self.__stock
#
#     @stock.setter
#     def stock(self,new_stock):
#         if new_stock>0:
#             self.__stock=new_stock
#         else:
#             print("invalid")
#
# o=Product(124,123)
# print(o.price)
# print(o.stock)
#
# o.price=2
# o.stock=3
# print(o.price)
# print(o.stock)
# 5. Write a Python program to demonstrate how super() can be used to call a parent class
# constructor.
# class Person:
#     def __init__(self,a):
#         self.a=a
#         print(self.a)
#     # def m1(self):
# class Employee(Person):
#     def __init__(self):
#         print("s")
#         super().__init__()
#     def m1(self):
#         print("ugu")
# obj=Employee(89)
# obj.m1()

# 6. Write a Python program to demonstrate the use of public, protected, and private access specifiers.

# class Private:
#     __privatVar=12
#     _protected=13
#     public=14
#     def __privateM(self):
#         print("private methode")
#         print(self.__privatVar)
#     def _protectedM(self):
#         print("protected methode")
#         print(self._protected)
#     def publicM(self):
#         print("public methode")
#         print(self.public)
# o=Private()
# o._protectedM()
# o._Private__privateM()
# o.publicM()
# 7. Create a program to show hierarchical inheritance with a base class Vehicle and derived classes Car and Bike.
# class Vehical:
#     def m1(self):
#         print("this is vehical")
# class Car(Vehical):
#     def m1(self):
#         print("this is car")
#         super().m1()
# class Bike(Vehical):
#     def m1(self):
#         print("this is bike")
#         super().m1()
# obj=Car()
# obj.m1()
# ob=Bike()
# ob.m1()


# 8. Write a program to show how the is instance() function can be used with inheritance.
# class A:
#     def instance(self):
#         print("A")
# class B(A):
#     def instance(self):
#         print("B")
#         super().instance()
# o=B()
# o.instance()
# 9. Create a class BankAccount that demonstrates encapsulation by
# having private attributes account_number and balance. Provide
# methods to deposit and withdraw money.
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
# bal=int(input("balance "))
# acct = BankAccount(bal)
# dep=int(input("deposit "))
# acct.dep(dep)
# wth=int(input("withdrawal "))
# acct.wth(wth)
# print(acct.bal_chk())

# 10. Implement a program to show how to prevent instantiation of an
# abstract class.
