#list of keywords in python
# import keyword
# print(keyword.kwlist)


#Dynamic type - python will automatically assign data type
# a=10
# b=90.2
# c="asf"
# print(type(a),type(b),type(c))

# a=10
# b=2.4
# c="wellcome"
# print(a,b,c)
#--------------------------------------------------------------------------
# example1
# a=100
# b=100
# c=100
# a=b=c = 100
# print(a,b,c)

#--------------------------------------------------------------------------
# Swapping
# x=10
# y=20
#
# print("before Swapping","x = ",x, "y = ",y)
# x,y=y,x
# print("After Swapping","x = ",x, "y = ",y)
#--------------------------------------------------------------------------
# deleting var
# a=10
# b=20
#
# print(a)
# print(b)
#
# del a
# print(a)
# print(b)
#--------------------------------------------------------------------------
# oPratores
# Assignment oprators
# a=6
# b=2
# print(a+b)
# print(a-b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b) # power
# print(a*b)

# a=43
# a+=3 # it will increment the value by 3 and assign to the "a" variable
# a-=3 # it will increment the value by 3 and assign to the "a" variable
# print(a)

#--------------------------------------------------------------------------
# Simple interst
# SI = P × R × T / 100

# P=2
# R=34
# T=3
# SI= P*R*T/100
# print(SI)

# Area of circle
# R=3
# ar= 3.14 * R**2
# print(ar)

# With math function
# import math
# radius = float( input("enter radius = "))
# ar = math.pi * radius**2
# print(ar)
#--------------------------------------------------------------------------
# relational opreators
# a=5
# b=6
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)
# print(a<=b)
# print(a>=b)
#--------------------------------------------------------------------------
#Logical Opreatoer
# a= True
# b=False
# print(a and b)
# print(a or b)
# print(not b)
#--------------------------------------------------------------------------
# Lists
# x=[1,2,3,4,5]
# y=x #it uses reference
# z=[1,2,3,4,5] # it is a separate list
# print(x is y) # "is" operator will compare references
# print(x is z)
# print(x is not y)
# print(x is not z)
#--------------------------------------------------------------------------
#Diffrent ways to printting

# name,age,sal = "aman",25,100000
# print("Name is " ,name)
# print("age is " , age)
# print("sal is " , sal)
#
# print("Name is : %s , Age is : %d , sal is : %f" %(name,age,sal))
# print("Name is {} , Age is : {}, sal is : {}".format(name,age,sal))
# print(f"Name is : {name}, Age is {age} , Salary is :{sal}")


# a= int(input("Enter the value of a : "))
# b= int(input("Enter the value of b : "))
# c = a+b
# print("Sum of a and b is :",c)
#
# a= int(input("Enter the value of a : "))
# b= int(input("Enter the value of b : "))
# c = a%b
# print("remander of a and b is :",c)

#WAP no. greater then b or not
#
# a= int(input("enter value of a "))
# b= int(input("enter value of b "))
#
# # c=int(a>b)
# c=str(a>b)
# # c=a>b
# print("A is greater then b" ,type(c),c)

#WAP av no. of user
# a= int(input("first No."))
# b= int(input("2nd No."))
# c= int(input("3rd No."))
# av= (a+b+c)/3

# a= input("first No.")
# b= input("2nd No.")
# c= input("3rd No.")
#
# av =(int(a)+int(b)+int(c))/3
# print(av)

