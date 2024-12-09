# Assignment-7

#
# # 1.Calculate the difference in days between two dates: 15th August 2025 and 1st January 2025.
# import datetime
# d1=datetime.date(2025,8,15)
# d2=datetime.date(2025,1,1)
# print(abs(d1-d2).days)

# 2.Write a Counter class with a class variable count to keep track of how many objects have been created.
# Test this by creating multiple objects and printing the count.
# class Counter:
#     count=0
#     def c(self):
#         self.count+=1
#         print(self.count)
# ob=Counter()
# ob.c()
# ob.c()
# ob.c()
# ob.c()
# 3.Write a program to print the current date and time in the format YYYY-MM-DD HH:MM:SS. Create a datetime object for 1st January 2025,
# 12:00 PM and print it in the format Day Month, Year at HH:MM.
# import datetime
# c=datetime.datetime.now()
# print(c)

# 4.Write a Product class with instance attributes for name and price. Add a class method set_discount(cls, discount) to apply a
# discount to all products. Use this class method to change the price of all created products.
class Product:
    name=""
    price=0

# 5.Create a class Car with:
# •	An instance variable brand
# •	A class variable wheels initialized to 4
# •	Add a method show() to print both variables.
# 6.Write a program to add 30 days to the current date and print the result.
# 7.Extend the Car class to include a method delete_attribute(attr_name) that checks if the attribute exists before deleting it.
# Print an appropriate message if the attribute does not exist.
# 8.Create a class Book with a constructor that initializes the title. Override the del method to print a message when the object is deleted.
# Create and delete a Book object to demonstrate this.
# 9.Create a class Product with:
# •	A constructor that takes name and price.
# •	A class method from_discounted_price(name, discounted_price, discount_percentage) that initializes a product based on the discounted price.
# •	Demonstrate the use of both constructors.







#
#
# from datetime import datetime, timedelta
#
# # 1. Calculate the difference in days between two dates: 15th August 2025 and 1st January 2025
# d1 = datetime(2025, 8, 15)
# d2 = datetime(2025, 1, 1)
# print("Days:", (d1 - d2).days)
#
# # 2. Write a Counter class with a class variable cnt to keep track of how many objects have been created.
# #    Test this by creating multiple objects and printing the total count.
# class C:
#     cnt = 0
#
#     def __init__(self):
#         C.cnt += 1
#
# o1 = C()
# o2 = C()
# o3 = C()
# print("Count:", C.cnt)
#
# # 3. Print the current date and time in the format YYYY-MM-DD HH:MM:SS.
# #    Create a datetime object for 1st January 2025, 12:00 PM, and print it in the format Day Month, Year at HH:MM.
# now = datetime.now()
# print("Now:", now.strftime("%Y-%m-%d %H:%M:%S"))
# dt = datetime(2025, 1, 1, 12, 0)
# print("Specific:", dt.strftime("%A %B, %Y at %H:%M"))
#
# # 4. Write a Product class with:
# #    - Instance attributes for n (name) and p (price).
# #    - A class method set_d(cls, d) to set a discount for all products.
# #    - A method to calculate the final price after applying the discount.
# class P:
#     d = 0
#
#     def __init__(self, n, p):
#         self.n = n
#         self.p = p
#
#     @classmethod
#     def set_d(cls, d):
#         cls.d = d
#
#     def fp(self):
#         return self.p - (self.p * P.d / 100)
#
# p1 = P("P1", 100)
# p2 = P("P2", 200)
# P.set_d(10)
# print("Price1:", p1.fp())
# print("Price2:", p2.fp())
#
# # 5. Create a Car class with:
# #    - An instance variable b (brand).
# #    - A class variable w (wheels) initialized to 4.
# #    - A method show() to print both b and w.
# class Car:
#     w = 4
#
#     def __init__(self, b):
#         self.b = b
#
#     def show(self):
#         print("Brand:", self.b, "Wheels:", Car.w)
#
# c = Car("Tesla")
# c.show()
#
# # 6. Write a program to add 30 days to the current date and print the result in the format YYYY-MM-DD.
# print("Add 30 days:", (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"))
#
# # 7. Extend the Car class to include a method del_attr(a) that:
# #    - Deletes the attribute a if it exists.
# #    - Prints an appropriate message if the attribute doesn’t exist.
# class CarEx(Car):
#     def del_attr(self, a):
#         if hasattr(self, a):
#             delattr(self, a)
#             print("Deleted:", a)
#         else:
#             print("Not found:", a)
#
# ce = CarEx("BMW")
# ce.del_attr("b")
# ce.del_attr("color")
#
# # 8. Create a Book class with:
# #    - A constructor to initialize t (title).
# #    - An overridden __del__ method to print a message when the object is deleted.
# #    - Demonstrate the deletion of a Book object.
# class B:
#     def __init__(self, t):
#         self.t = t
#
#     def __del__(self):
#         print("Deleted:", self.t)
#
# b = B("Python")
# del b
#
# # 9. Create a Product class with:
# #    - A constructor to take n (name) and p (price).
# #    - A class method from_dp(cls, n, dp, d) that initializes a product using the discounted price (dp) and discount percentage (d).
# #    - Demonstrate both constructors.
# class P2:
#     def __init__(self, n, p):
#         self.n = n
#         self.p = p
#
#     @classmethod
#     def from_dp(cls, n, dp, d):
#         op = dp / (1 - d / 100)
#         return cls(n, op)
#
# p3 = P2("Gadget", 500)
# p4 = P2.from_dp("Discounted", 450, 10)
# print("P3:", p3.n, "Price:", p3.p)
# print("P4:", p4.n, "Price:", round(p4.p, 2))
