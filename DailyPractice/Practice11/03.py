# define a global variable x and local variable y inside a method of a class Example. Create a method show_variable() to display the value of both variable.

x = 20
class Example:
    def m1(self,x):
        print(x)        #local variable
        print(globals()['x'])           #Global variable

ob1 = Example()
ob1.m1(22)
