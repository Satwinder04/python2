# Sum of Numbers in a List
# Write a Python program that takes a list of numbers as input and uses a
# for loop to calculate and print the sum of the numbers.
#
# a=[1,2,3,4]
# sum = 0
# for i in range(0, len(a)):
#     sum+=a[i]
# print(sum)
#--------------------------------------------------------------------
#
# Check Even or Odd Numbers in a Range
#
# Write a Python program that uses a for loop to print
# whether each number in a given range is even or odd.

# n=int(input("enter value of n "))
# for i in range(0,n+1):
#     if i%2==0:
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

#--------------------------------------------------------------------
# Find the Largest of a List of Numbers
# Write a Python program that takes a list of numbers as input and uses a for loop to find the largest number in the list

# a=[1,2,3,4]
#
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if a[i] > a[j+1] and a[i] > a[j+2]:
#             largest = a[i]


#------------------------------------------------------------------
# Print Each Character in a String
# Write a Python program that uses a for loop to print each character of a user-provided string on a new line.

# a =input("write String ")
#
# for i in range(0,len(a)):
#     print(a[i])
#

#-----------------------------------------------------------------------
# Print Elements of a List
# Write a Python program that uses a for loop to print each element of a list.

# a= [1,2,3,3,5]
# for i in range(0,len(a)):
#     print(a[i])

# Print Squares of Numbers
# Write a Python program that uses a for loop to print the squares of numbers from 1 to 10.
#
# for i in range(0,11):
#     print(f"Square of {i} is" , i**2)



#
# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end= " " )
#     for j in range(i+1):
#         print(j,end= " " )
#     for j in range(i):
#         print("x",end= " " )
#     print()
#
#   #       x
#   #     x x x
#   #   x x x x x
#   # x x x x x x x