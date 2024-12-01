# def greet(*args):
#     print("hello ", args)
# greet("satwinder","manpreet","samar",)



# def student(**kwargs):
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# student(name="Satwinder",rollno=120)
#
# def greet(name,*args):
#     print("hello ", args,name)
# greet("satwinder","manpreet","samar",)
# #
# def greet(name,*args,**kwargs):
#     print(name)
#     for i in args:
#         print(i)
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
#
# greet("satwinder","manpreet","samar",n="aman",marks="2134")


# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(4))