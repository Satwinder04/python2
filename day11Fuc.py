# def myfuc():
#     print("hello")
#
# myfuc() # calling function
# from time import process_time


# def myfuc1(name):
#     print("hello",name)
# n=input()
# myfuc1(n)

# def cal(a,b):
#     return a+b
#
# print(cal(10 ,10))

# def func():
#     return
# print(func())

# def adding(a,b,c,d,e,f,g):
#     return a+b+c+d+e+f+g
# print(adding(10,10,10,10,10,10,10))

# def fact(n):
#     factt =1
#     # for i in range(1,n+1):
#     #     factt*=i
#     # return factt
#     i=1
#     while i<=n:
#         factt*=i
#         i+=1
#     return factt
#
# n=int(input("enter no."))
# print(fact(n))

# globale = 20
# def func():
#     locale =10
#     return locale
# # print(locale)
# print(func())
# print(globale)

# xy = 20
# def func():
#     xy =10
#     return xy
# # print(locale)
# print(func())
# print(xy)
#
# xy = 20
# def func():
#     global xy
#     xy =10
#     return xy
# # print(locale)
# print(func())
# print(xy)
#
# x=100
#
# def cool():
#     global x
#     x=500
#     print(x)
# # cool()
# print(x)


#
# def cal(a,b):
#     global c
#     c=a+b
#
# cal(10 ,10)
# print(c)

# def s(a,b):
#     return a+b
# print(s(10,10))
# print(s(a=10,b=20))
# print(s(b=10,a=20))

# def s(a,b=30): #default argument
#     return a+b
# print(s(10))
# print(s(a=10,b=20))
# print(s(b=10,a=20))

# def greet(name,greetmsg): #default argument
#     print(greetmsg+ " "+name)
# greet("hello","satwinder")
# greet(name="hello",greetmsg="satwinder")
# greet(greetmsg="satwinder",name="hello")

# def s(a,b,c):
#     print(a,b,c)

# def g(a,b):
#     if a>b:
#         print("a is grater")
#     else:
#         print("b is greater")
#
# a=int(input("enter value of a "))
# b=int(input("enter value of b "))
# g(a,b)

# def ar(a,b=10):
#     arr=a*b
#     return arr
# print(ar(20))

# name=input("enter name ")
# classs=input("enter calss ")
# address=input("enter adderss ")
#
# def det(name,classs,address):
#     print("name "+name + " class " + classs +" address " + address)
# det(name=name,classs=classs,address=address)

# x=lambda a:a+10
# print(x(5))

# x=lambda a,b:a+10+b
# print(x(5,10))

#
# x=lambda a,b,c:a+10+b+c
# print(x(5,10,10))
# lst=[1,2,3,4,5,6,7,8,9,6,3]
# def ev(x):
#     return x%2
#
# for i in list:
#     print(ev(list[i]))

# ev=list(filter(lambda x:x%2==0,lst))
# print(ev)
#
# city=["patiala","rajpura","ambrsr","patna"]
# def leng(city):
#     return len(city)
# sort= sorted(city,key=leng)
# print(sort)

# sort =sorted(city,key= lambda x:len(x))
# print(sort)

# no=[1,2,3,4]
# sq= list(map(lambda x:x**2,no))
# print(sq)

# from functools import reduce
# z=reduce(lambda x,y:x+y,[1,2,3,4])
# # z=reduce(lambda x,y:x+y,[1,2,3,4,5,6,7,8,9])
# print(z)

# a=[10,20,30,40]
# b=[50,60,70,80]
# z= zip(a,b)
# print(list(z))

a=["java","python","js","c++"]
b=[50,60,70,80]
z= zip(a,b)
print(list(z))