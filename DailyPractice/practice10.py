# # 4.	Write a function to calculate the area of a rectangle, given its length and breadth.
#
#
# def area(l,b):
#     a = l*b
#     return a
# l = int(input("Enter the length of rectangle:"))
# b = int(input("Enter the breadth of rectangle:"))
# print(area(l,b))
#
# # 5.	Create a function that prints a pattern of stars in increasing order up to a given number of rows
#
#
# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* ",end="")
#         print()
# n = int(input("Enter the number: "))
# pattern(n)
#
#
# # 6.	Write a function that takes three parameters and demonstrates the use of default values for some of them.
#
#
# def func(a,b,c=30):
#     return a,b,c
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print(func(a,b))
#
#
# # 7.	Create a function to check whether a given string is a palindrome.
#
# def is_palindrome(num):
#     rev = ""
#     for i in num:
#         rev=i+rev
#     if num!=rev:
#         print("Not Palindrome")
#     else:
#         print("Palindrome")
#
# num = input("Enter the String: ")
# is_palindrome(num)
#
#
#
# # 8.	Write a recursive function to find the nth Fibonacci number
#
# n = int(input("Enter the number:"))
# first = 0
# second = 1
# for i in range(n+1):
#     temp = first%second
#     first=second
#     second=temp
# print(first)
#
#
# # 9.	Implement a recursive function to calculate the sum of the digits of a given number.
#
# def sum(num):
#     for i in range(num+1):
#         return num+num+1
# num = int(input("Enter the number: "))
# print(sum(num))
#
# # 10.	Use a lambda function to create a one-liner that calculates the square of a number.
#
# n = int(input("Enter the number: "))
# x = lambda z:z**2
# print(x(n))
#
#
#
# # 11.	Use a lambda function with filter to extract even numbers from a list of integers.
#
# my_list = list(map(int,input("Enter the list of numbers: ").split(",")))
#
# x = list(filter(lambda z:z%2==0,my_list))
# print(x)
#
#
# # 12.	Write a lambda function with map to double the elements of a list.
#
# my_list = list(map(int,input("Enter the list of numbers: ").split(",")))
#
# x = list(map(lambda z:z*2,my_list))
# print(x)
#
#
# # 13.	Create a function that accepts another function and two numbers as arguments and applies the passed function to the numbers.
#
# def func_1(a,b):
#     return a+b
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
#
# a1 = func_1(a,b)
#
# def func_2(a1,c,d):
#     return a1,c,d
# c=int(input("Enter the first number:"))
# d=int(input("Enter the second number:"))
# print(func_2(a1,c,d))
#
#
# # 14.	Implement a nested function that demonstrates how inner functions can access variables from the outer function.
#
# def outer_func(outer_var):
#     print("Outer function",outer_var)
#
#     def inner_func(inner_var):
#         print("Inner function",inner_var)
#
#         print("Calling outer inside inner:",outer_var)
#     inner_func(4)
# outer_func(45)
#
#
#
# # 15.	Create a lambda function that generates a multiplier function for a given number.
#
# n = int(input("Enter the number: "))
# x = lambda z:z**2
# print(x(n))
#
#
#
# # 16.	Write a function that takes a list of numbers and returns both the maximum and minimum numbers.
#
# def max_min(my_list):
#     # return max(my_list),min(my_list)
#     max_value=my_list[0]
#     min_value=my_list[0]
#     for i in my_list:
#         if max_value>i:
#             max_value=i
#         if min_value<i:
#             min_value=i
#     return max_value,min_value
# my_list = list(map(int,input("Enter the list of numbers: ").split(",")))
# print(max_min(my_list))
#
#
# # 17.	Implement a function to calculate the grade of a student based on marks in five subjects.
#
# def calculate_grade(marks):
#     if marks>=90:
#         print("The grade is: A")
#     elif marks>=80:
#         print("The grade is: B")
#     elif marks>=50:
#         print("The grade is: C")
#     elif marks>=30:
#         print("The grade is: D")
#     else:
#         print("Congrats, you are Fail")
#
# marks = int(input("Enter the marks: "))
# calculate_grade(marks)
#
#
# # 18.	Write a function that takes a string and returns a dictionary with the frequency of each word in the string.
#
#
#
# def freq(s1):
#     d = {}
#     for i in s1:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i] = 1
#     print(d)
# s1 = input("Enter the String: ")
# freq(s1)
#
#
#
# # 19.	Create a function to generate a random password with a given length, ensuring a mix of uppercase, lowercase, digits, and special characters.
#
#
# import random
# import string
#
# def generate_password(length):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choice(characters) for _ in range(length))
#
# length = int(input("Enter the password length: "))
# print("Generated password:", generate_password(length))
#
# # 20.	Create a function that takes a list of numbers and removes all duplicates, returning a new list.
#
#
# def remove_dup(user_list):
#     dup_list = []
#     for items in user_list:
#         if items not in dup_list:
#             dup_list.append(items)
#     print(dup_list)
# user_list = list(map(int,(input("Enter the elements of list separated by (,): ").split(","))))
# remove_dup(user_list)
#

