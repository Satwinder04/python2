# class car:
#     def cars(self,b,m):
#         self.brand= b
#         self.model= m
#
# ob= car()
# ob.cars("toyota","corolla")
# print(ob.brand)
# print(ob.model)


class car:
    def __init__(self,b,m):
        self.brand= b
        self.model= m
    def __str__(self):
        return f"model : {self.model}, brand : {self.brand}"
    # def __init__(self,b,m):
    #   self.brand= b
    #   self.model= m

ob= car("toyota","corolla")
# print(ob.brand)
# print(ob.model)\
print(ob)

