# Create a class calculator with an instance method add(self, a,b) to add two numbers,
# now add a static method info() to print "This is a calculator class". Call both methods appropriately.

class Calculator:
    def add(self,a,b):
        print(a+b)
    @staticmethod
    def info():
        print("This is a Calculaotr class")
ob1 = Calculator()
ob1.add(5,10)
Calculator.info()
