# patterns

# n=5
# n=int(input("enter value of n"))
# for i in range(n):
#     for j in range(n):
#         print("*",end= " " )
#     print()
#
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *



# def p():
#     for i in range(n):
#         for j in range(i+1):
#             print("*",end= " " )
#         print()
# n=int(input("enter value of n "))
# p()


# *
# * *
# * * *
# * * * *
# * * * * *



# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(n-i):
#         print("* ",end= " " )
#     print()

# *  *  *  *  *  *
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *


# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print(" x",end= "" )
#     print()
#         x
#       x x
#     x x x
#   x x x x
# x x x x x



# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end= " " )
#     for j in range(n-i):
#         print(" x",end="")
#     print()
#
#  x x x x
#    x x x
#      x x
#        x



# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print(" x ",end= " " )
#     print()

#         x
#       x   x
#     x   x   x
#   x   x   x   x
# x   x   x   x   x



# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print("x",end= " " )
#     for j in range(i):
#         print("x",end= " " )
#     print()
  #       x
  #     x x x
  #   x x x x x
  # x x x x x x x



# n=int(input("enter value of n "))
#
# n=int(input("enter value of n "))
# for i in range(n-1):
#     for j in range(n-i-1):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print("x",end= " " )
#     for j in range(i):
#         print("x",end= " " )
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end= " " )
#     for j in range(n-i):
#         print("x",end=" ")
#     for j in range(n - i-1):
#         print("x",end= " " )
#     print()
#
#         x
#       x x x
#     x x x x x
#   x x x x x x x
# x x x x x x x x x
#   x x x x x x x
#     x x x x x
#       x x x
#         x


# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end= " " )
#     print()