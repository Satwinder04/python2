class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        self.__name=new_name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age>18:
            self.__age=new_age
        else:
            print("below 18")

obj=Student("Satwinder",24)
print(obj.name)
print(obj.age)
