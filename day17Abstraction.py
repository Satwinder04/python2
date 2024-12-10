from abc import ABC,abstractmethod
from time import sleep


# class A(ABC):
#     def d(self):
#         None
#     def d(self):
#         print("hoooo")
# class B(A):
#     def d(self):
#         print("ba")
#
#
#
# class Animal(ABC):
#     @abstractmethod
#     def eat(self):
#         pass
# class Tiger(Animal):
#     def eat(self):
#         print("non-veg")
# class Cow(Tiger):
#     def eat(self):
#         print("veg")
#         super().eat()
# o=Cow()
# o.eat()

#
# class Shape(ABC):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def area(self):
#         print(f"area of R is {self.l*self.b}")
#
#
# # lst=[(1,2),
# #      (2,3),
# #      (7,2),
# #      (9,4),
# #      (2,4),
# #      ]
# # for i in lst:
# #     o=Rectangle()
# #     o.area()


# Access_specifiers
# Scope -variable,class,method
# __ => private
# _ => Protected

class Private:
    __privatVar=12
    _protected=13
    def __privateM(self):
        print("private methode")
        print(self.__privatVar)
    def _protectedM(self):
        print("protected methode")
        print(self._protected)

o=Private()
# o._protectedM()
o._Private__privateM()