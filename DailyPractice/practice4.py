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

# simple calculator

# a=int(input("enter value of a :"))
# op=input("enter value of opretor :")
# b=int(input("enter value of b : "))
#
# if op=="+":
#     print("addition of a and b is ",a+b)
# elif op=="-":
#     print(a-b)
# elif op=="*":
#     print(a*b)
# elif op=="/":
#     print(a/b)
# elif op=="**":
#     print(a**b)
# elif op=="%":
#     print(a%b)
# elif op=="//":
#     print(a//b)
# else:
#     print("invalid input")


# n = int(input("Enter value of n: "))
# print(f"Prime factors of {n} are:")

# for i in range(2, n + 1):
#     if n % i == 0:
#         isPrime = 1
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 isPrime = 0
#                 break
#         if isPrime == 1:
#             print(i)

#
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# if num2 > num1:
#     num1, num2 = num2, num1
#
# while num2 != 0:
#     remainder = num1 % num2      #15%12=3         12%3=4
#     num1 = num2     #num1=12      num1=3
#     num2 = remainder  #num2 = 3       num2=4
#
# print("The GCD of the numbers is:",num1)







# a=b*r+a/b

# a= int(input("enter the value of a : "))
# b= int(input("enter the value of b : "))
#
# if a>b:
#     a,b=b,a
#
# while b!=0:
#     rem = a%b
#     a = b
#     b= rem
# print("GCD of a and b is : ",a)
