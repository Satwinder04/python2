# create a class car with instance variables brand and model than initiate three objects for different cars and print their details using a method car_info()

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def car_info(self):
        print(f"The car brand is {self.brand} and the model is {self.model}")

ob1 = Car("Toyota", "Fortuner")
ob2 = Car("Hundai", "Creta")
ob3 = Car("Maruti Suzuki", "Swift")

ob1.car_info()
ob2.car_info()
ob3.car_info()
