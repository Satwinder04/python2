# 1. Write a program to divide two numbers. Handle the case where the divisor is
# zero using ZeroDivisionError.
# def div(a,b):
#     print(a/b)
# try:
#     a=int(input("enter a "))
#     b=int(input("enter b "))
#     div(a,b)
# except ZeroDivisionError as e:
#     print(e)

# 2. Create a program that accepts two integers from the user. Handle the case where the user
# enters a non-integer value using ValueError.
# def intt(a,b):
#     print(a,b)
# try:
#     a=int(input("enter a "))
#     b=int(input("enter b "))
#     intt(a,b)
# # except ValueError as e:
# #     print(e)
# except ValueError:
#     print("invalid")

# 3. Write a program that accepts a list of integers from the user and retrieves an element by index.
# Handle the case where the index is out of range using Index Error.
# lst=list(map(int,input("enter lst").split(" ")))
# def lst(l1):
#     print(l1)
# try:
#     # l1 = list([int(e) for e in input("Enter List: ").split(",")])
#     l1=list(map(int,input("enter lst").split(" ")))
#     lst(l1)
#     indx=int(input("enter indx"))
#     print(l1[indx])
# except IndexError as a:
#     print(a)
# 4. Create a program with a dictionary of fruits and their prices. Allow the user to input a
# fruit name and display its price. Handle the case where the fruit does not exist using
# KeyError.
# dc={
#     "m":12,
#     "a":13,
#     "b":15
# }
# n=input("enter fruit ")
# print(dc["m"])

# 5. Write a program that accepts a number from the user and calculates its square root. Raise a ValueError if the input is negative, and handle it gracefully.
# 6. Write a program that combines multiple operations, such as dividing two numbers and retrieving an element from a list. Use nested try-except blocks to handle specific exceptions like ZeroDivisionError and IndexError
# 7. Create a custom exception class called InvalidAgeException. Write a program that raises this exception if the user inputs an age less than 18.
# 8. Define a custom exception class called InsufficientBalance Exception. Write a program where the user tries to withdraw an amount from their bank balance. Raise this exception if the withdrawal amount exceeds the balance.
# 9. Write a program that accepts two inputs: a number and its divisor. Handle multiple exceptions, such as ZeroDivisionError (if the divisor is zero) and ValueError (if non-numeric inputs are provided).
# 10. Write a program that performs division and uses the finally block to print a cleanup message, such as "Execution completed, exiting program," regardless of whether an exception occurs.
