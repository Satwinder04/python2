# s='satwinder singh'
# s2="satwinder singh"
# s3=str("satwinder singh")
# s4=str('satwinder singh')
#
# print(id("welcome"))
# s=8
# a= 4
# b=4
# p=a+b
# print(id(s))
# print(id(a+b))
from itertools import count

# print(s,s2,s3,s4)

#why strings are immutable
# it will not change the location it will replace the refrance

# str = "welcome"
# print(str + "python")
#
# print(str*2)
# print(str*3)

# str="welcome"
# w  e  l  c  o  m  e
# 0  1  2  3  4  5  6  index
#-7 -6 -5 -4 -3 -2 -1
# 1  2  3  4  5  6  7  #lenght


# print(str[1:4])
# print(str[:4])
# print(str[1:])
# print(str[-4:-1])
# print(str[1:-1])
# print(str[-1])

# print(ord("A"))
# print(ord("a"))
#
# print(chr(65))
# print(chr(97))

# print(min("Satwinder"))
# print(max("Satwinder"))
# # print(min("Satwinder"))
#
# print(len("satwinder"))

# s= "Satwinder"
# print('inder' in s)
# print('inder' not in s)
# print('indre' in s)
# print('Inder' not in s)

# print("tim"=="tie") #false
# print("freedom"=="free")
# print("tim">"tie")
# print("teeth"<"tee")
# print("tim"<="tie")
# print("tim">="tie")


#
# n=int(input("enter value of n "))
# count = 1
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print(count," ",end= " " )
#         count+=1
#
#     print()
# enter value of n 6
#             1
#           2   3
#         4   5   6
#       7   8   9   10
#     11   12   13   14   15
#   16   17   18   19   20   21



#
# n=int(input("enter value of n "))
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
#     print()

#
#    1
#   121
#  12321
# 1234321

# n=int(input("enter value of n"))
# for i in range(n):
#     for j in range(n):
#         if(j%2==0):
#             print("1",end=" ")
#         else:
#             print("0",end= " ")
#     print()
#

# convert f int c
#
# c=int(input("enter value of f"))
# f= c*(9/5)+32
# print(f)

# import math
# a=int(input("enter value of a"))
# b=int(input("enter value of b"))

# GCD(a, b) = (a × b) / LCM(a, b)
# LCM = math.lcm(a,b)
# i=0
# while True:
#     i+=0
#     if (a%i !==0) and (b%i !==0):
#         print(i)
# GCD = abs(a*b)/LCM
# print(GCD)
