# 1. Create a parent class Vehicle with attributes like brand and model. Implement a subclass Car that adds an attribute
# num_doors. Write methods to display the details of both parent and child classes.
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def display(self):
#         print(self.brand)
#         print(self.model)
#
# class Car(Vehicle):
#     def __init__(self,num_doors,brand,model):
#         self.num_doors=num_doors
#         super().__init__(brand,model)
#     def display(self):
#         super().display()
#         print(self.num_doors)
# obj=Car(4,"tyota","crola")
# obj.display()
#
#
#
# 2. Define a class Shape with a method area that raises a NotimplementedError. Create subclasses Rectangle and Circle that implement the area() method.
# import math
# class Shape:
#     def area(self):
#         raise NotImplementedError("asdfgh")
#
# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
#     def area(self):
#         print(f"area of rectangle is {self.l*self.b}")
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         print(f"Area of cicle is {(22/7)*self.r**2}")
#         print(f"Area of cicle is {math.pi*self.r**2}")
#
# r=Rectangle(2,3)
# r.area()
# c=Circle(2)
# c.area()
#
# 3. Write a Python program where a class Animal has a method make_sound(). Create subclasses Dog, Cat, and Cow that override the make_sound method to print their respective sounds.
# class Animal:
#     def make_sound(self):
#         pass
#
# class Dog(Animal):
#     def make_sound(self):
#         print("Woof Woof")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow meow")
#
# class Cow(Animal):
#     def make_sound(self):
#         print("Moo mooo")
#
# obj1 = Dog()
# obj1.make_sound()
# obj2 = Cat()
# obj2.make_sound()
# obj3 = Cow()
# obj3.make_sound()
#
# 4. Create a class Person with attributes name and age. Derive a class Employee from Person that adds employee_id and salary Implement methods to display details for both classes.write code without comment
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name)
#         print(self.age)
# class Employee(Person):
#     def display(self,empID,salary):
#         print(empID,salary)
#
# obj1=Person("satwinder",23)
# obj1.display()
#
# obj2=Employee()
# obj2.display(123456,12379876)
#
#
# class Person:
#     def __init__(self,name,age):
#         self.age=age
#         self.name=name
#     def display(self):
#         print(self.name)
#         print(self.age)
#
# class Emp(Person):
#     def __init__(self,EmpID,salay,name,age):
#         self.EmpID=EmpID
#         self.salay=salay
#         super().__init__(name,age)
#     def display(self):
#         super().display()
#         print(self.EmpID)
#         print(self.salay)
# obj=Emp("johuhiasidj",12345,12345678,123456785678)
# obj.display()
#
# 5. Write a function play_sound(animal) that takes an object of any subclass of Animal and calls its sound() method. Create subclasses of Animal to demonstrate polymorphism.
# class Animal:
#     def play_sound(self):
#         raise NotImplementedError("not implement error")
# class Dog(Animal):
#     def play_sound(self):
#         print("bhaow bhaaow")
# class Pickachu(Animal):
#     def play_sound(self):
#         print("Pickachu")
# class Aman(Animal):
#     def play_sound(self):
#         print("Aman")
#
# d=Dog()
# d.play_sound()
# P=Pickachu()
# P.play_sound()
# a=Aman()
# a.play_sound()
#
# 6. Define a base class Appliance with a method turn_on(). Create subclasses Washing Machine,
# Refrigerator, and Microwave that override the tum_on() method. Write a program to demonstrate calling
# the method for different objects using a loop.
#
# class Appliance:
#     def turn_on(self):
#         print("All")
# class WashingMachine(Appliance):
#     def turn_on(self):
#         print("turning on Washing Machine")
# class Refrigerator(Appliance):
#     def turn_on(self):
#         print("turning on Refrigerator")
# class Microwave(Appliance):
#     def turn_on(self):
#         print("turning on Microwave")
# lst=[WashingMachine(),Refrigerator(),Microwave()]
# for i in lst:
#     i.turn_on()
#
# 7. Write a program with a base class Shape and subclasses Square, Triangle, and Circle. Implement a method draw in each subclass and demonstrate polymorphism using a loop to call draw on a list of shapes.
# class Shape:
#     def draw(self):
#         pass
# class Square(Shape):
#     def draw(self):
#         print("4 sides")
# class Circle(Shape):
#     def draw(self):
#         print("infinite sides")
# class Triangle(Shape):
#     def draw(self):
#         print("3 sides")
#
# lst=[Square(),Circle(),Triangle()]
# for i in lst:
#     obj=i
#     obj.draw()
#
#
# 8. Create a class hierarchy for Transport with subclasses Airplane, Ship, and Car. Each subclass should override a method move(). Write a program to demonstrate polymorphism.
# class Transport:
#     def move(self):
#         pass
#
# class Airplane(Transport):
#     def move(self):
#         print("Fly")
#
# class Ship(Transport):
#     def move(self):
#         print("Sail")
#
# class Car(Transport):
#     def move(self):
#         print("Drive")
#
# lst = [Airplane(), Ship(), Car()]
#
# for i in lst:
#     i.move()
