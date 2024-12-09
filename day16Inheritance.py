# class A:
#     def __int__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print("method of class A")
# class B(A):
#     def __int__(self):
#         print("im constructor of B")
#     def m2(self):
#         print("im method of class B")
#
# ob=B()
# ob.m1()
# ob.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.a+self.b)
# ob=B()
# ob.m1()
# ob.m2()


#Multilevel
# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def __init__(self):
#         print("i am constructor of B")
#     def m2(self):
#         print(self.a+self.b)
# class C(B):
#     p,q=1000,2000
#     def __init__(self):
#         print("i am constructor of C")
#     def m3(self):
#         print(self.p+self.q)
# ob=C()
# ob.m1()
# ob.m2()
# ob.m3()

# hierarchy inheritance
# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=100,200
#     def __init__(self):
#         print("i am constructor of B")
#     def m2(self):
#         print(self.a+self.b)
# class C(A):
#     p,q=1000,2000
#     def __init__(self):
#         print("i am constructor of C")
#     def m3(self):
#         print(self.p+self.q)
# ob=B()
# ob.m1()
# ob.m2()
#
# ob2=C()
# ob2.m1()
# ob2.m3()
#
# class A:
#     x,y=10,20
#     def __init__(self):
#         print("i am constructor of A")
#     def m1(self):
#         print("m1 of class A")
# class B:
#     a,b=100,200
#     def __init__(self):
#         print("i am constructor of B")
#     def m1(self):
#         print("m of class B")
#     def m2(self):
#         print(self.a+self.b)
# class C(A,B):
#     p,q=1000,2000
#     def __init__(self):
#         print("i am constructor of C")
#     def m3(self):
#         print(self.p+self.q)
#
# ob2=C()
# ob2.m1()
# ob2.m1()

# method overload
# method overriding

# class V:
#     def m1(self):
#         print("speed - 100km/hr")
# class B(V):
#     def m1(self):
#         print("speed - 70km/hr")
# class C(V):
#     def m1(self):
#         print("speed - 80km/hr")
#         super().m1()
#     def m1(self):
#         print("hii all")
#
# ob1=V()
# ob1.m1()
#
# ob2=B()
# ob2.m1()
#
# ob3=C()
# ob3.m1()

# use of super

# class A:
#     name="Aman"
# class B(A):
#     name="John"
#     def test(self):
#         print(super().name)
# obj=B()
# obj.test()
#
# a,b=1000,2000
# class A:
#     x,y=100,200
# class B(A):
#     i,j=10,20
#     def m1(self,x,y):
#         print(x+y)
#         print(self.i+self.j)
#         # print(globals(a)+globals(b))
#
# obj=B()
# obj.m1(10,20)
# class Calculation:
#     def add(self,a=0,b=0,c=0):
#         print(a+b+c)
# cal = Calculation()
# cal.add()
# cal.add(10,20)
# cal.add(10,20,30)

