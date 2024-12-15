#errors
#types
'''
syntax
logic
runtime
'''
# print("Starting")
# print("Starting")
# print(0/0)
# print("ending")
# print("ending")
"""

To avoid termination, we need to handle the exception..........
To handle the exception we have try, except, else, finally
try: code that might cause the exception
except: / expect someExceptionName as e: code to handle the exception
else: code to execute if no exception occured
finally: code that will run no matter what
"""
# ___________________________________
# print("start")
# print("start")
# print("start")
# try:
#     print(0/0)
# except :
#     print(0)
# print("ending")
# print("ending")
# print("ending")
# ________________________________________
# print("start")
# print("start")
# print("start")
# try:
#     print(0/0)
# except Exception as e :
#     print(e)
# print("ending")
# print("ending")
# print("ending")
# ________________________________________
# print("start")
# print("start")
# print("start")
# try:
#     print(0/0)
# except ZeroDivisionError as e :
#     print(e)
# print("ending")
# print("ending")
# print("ending")
# -------------------------------------------------------------
# n1,n2=10,0
# try:
#     result=n1/n2
#     print(result)
# except ZeroDivisionError:
#     print("num can not divisible by 0")
# except SyntaxError:
#     print("Syntex")
# except Exception as e:
#     print(e)
# else:
#     print("no exection")
# finally:
#     print("always execute")

# -----------------------------------------------------------------------

# def enterage(age):
#     if age<0:
#         raise ValueError("-ve")
#     if age%2==0:
#         print("even")
#     else:
#         print("odd")
#
#
# # age=-1
# try:
#     n=int(input("enter the age "))
#     enterage(n)
# except ValueError:
#     print("-veee")
#

# _____________________________________________________________________
# class customError(Exception):
#     pass

# ________________________________________________________________________
# class NegetiveNumberError(Exception):
#     def __init__(self,msg="-ve value not allowed"):
#         self.msg=msg
#         super().__init__(self.msg)
# def chkPositive(n):
#     if n<0:
#         raise NegetiveNumberError()
#     else:
#         print("+ve")
#
# try:
#     num=int(input("enter n "))
#     chkPositive(num)
# except NegetiveNumberError as e:
#     print(e)
# except Exception as a:
#     print(a)
#




