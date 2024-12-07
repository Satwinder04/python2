# Create a class rectangle with a method area(self,length,breadth) that calculate and return the area of rectangle. Call the method and display the result.

class Rectangle:
    def area(self,length,breadth):
        print(f"The area of rectangle is {length*breadth}")
area = Rectangle()
area.area(10,5)
