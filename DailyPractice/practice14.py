# 1. Implement a Car class with attributes like make, model, and year. Include a method start_engine() that prints a message indicating the engine is starting. Create multiple objects to represent different cars.
# class Car():
#     def start_engine(self,make,model,year):
#         print("engine is start",make,model,year)
#
# ob = Car()
# ob.start_engine("abc","xyz",2019)
# ob.start_engine("asd","xyz",2018)
# ob.start_engine("fasf","xyz",2015)
# ob.start_engine("dadfa","xyz",2013)
from itertools import count
from time import sleep


# 2. Implement a Company class with a class attribute company name. Add instance attributes for employee_name and designation. Create multiple employees and display their details along with the company name.

#
# class Company:
#
#     company_name="bebo"
#     # def __init__(self,emp,ds):
#     #     self.emp_name=emp
#     #     self.designation=ds
#
#     def display(self,emp,ds):
#         print(f"company name ={self.company_name}")
#         print(f"employee name ={emp}")
#         print(f"designation name ={ds}")
#
# ob = Company()
# ob.display("satwinder","QE")
# ob.display("satwinder","QE")
# ob.display("satwinder","QE")
# ob.display("satwinder","QE")

# 3. Write a Counter class with a class variable count to keep track of how many objects have been created. Test this by creating multiple objects and printing the count.
# class Counter:
#     count=0
#     def countt(self):
#         self.count+=1
#         print(self.count)
# ob=Counter()
# ob.countt()
# ob.countt()
# ob.countt()

# 4. Create a Person class with a constructor that accepts name and age as parameters. Add a method to display this information. Test the constructor by creating objects with different values.

# class Person:
#     def __init__(self,n,a):
#         self.name= n
#         self.age= a
#     def display(self):
#         print(f"name is {self.name} age is {self.age}")
# ob=Person("satwinder",23)
# ob.display()
# ob=Person("satwinder",23)
# ob.display()
# ob=Person("satwinder",23)
# ob.display()
# ob=Person("satwinder",23)
# ob.display()
#

# 5. Develop a Laptop class with attributes like brand and model. Use a constructor to initialize these attributes. Include a method specifications) to print the details.
# class Laptop:
#     def __init__(self,b,m):
#         self.brand= b
#         self.model= m
#     def display(self):
#         print(f"brand is {self.brand} model is {self.model}")
# ob=Laptop("HP","pavilion")
# ob.display()
# ob=Laptop("HP","victus")
# ob.display()

# 6. Create a Point class to represent a point in 2D space with attributes x and y. Use a constructor to initialize
# these values and a method to calculate the distance between two points.
# Formula distance (x2-x1)2+(y2-y1)2
# import math
# class Point:
#     def __init__(self, a, b,c,d):
#         self.x1 = a
#         self.y1 = b
#         self.x2 = c
#         self.y2 = d
#     def distance(self):
#         dis= ((self.x2-self.x1)**2 +(self.y2-self.y1)**2)
#         print(math.sqrt(dis))
# ob=Point(3,4,7,1)
# ob.distance()
# 7. Write a Python program to implement an Employee class with a constructor that initializes id, name, and salary.
# Add a method give raise(percent) to increase the salary by a given percentage.

# class Company:
#     def __init__(self,emp,salary):
#         self.emp=emp
#         self.salary=salary
#     def display(self,percent):
#         print(f"employee name ={self.emp}")
#         print(f"designation name ={self.salary}")
#         print((self.salary*percent)/100+self.salary)
# ob = Company("satwinder",1200)
# ob.display(10)


# 8. Write a Product class with instance attributes for name and price.
# Add a class method set_discount(cls, discount) to apply a discount to all products.
# Use this class method to change the price of all created products.

class Product():
    ProductList=dict({'phone':100,'tv':120,'watch':80})
    def set_discount(self,dis):
        # self.dis=dis
        for key,value in Product.ProductList.items():
            temp=(value-(value * dis)/100)
            Product.ProductList[key]=temp
    def display(self):
        for i,j in Product.ProductList.items():
            print(i,j,end=" ")
ob=Product()
ob.set_discount(10)
ob.display()

# 9. Create a module math_operations.py with functions add, subtract, multiply, and divide. Write a script to import and use these functions.



# 10. Develop a package shapes with modules circle py and rectangle.py. Include methods to calculate the area and perimeter of a circle and rectangle. Test the package in a separate script.
# 11. Create a package utilities with modules string_util.py (with functions like reverse_string and is_palindrome) and number_util.py (with functions like is even and is_prime). Use these utilities in a Python script.
# 12. Create a package inventory with a module product.py. Define a Product class with attributes like name, price, and quantity. Add methods to update the quantity and calculate the total value. Import and use this package in another script.

