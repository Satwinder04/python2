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
    def __init__(self,b,m):
            self.brand= b
            self.model= m

ob= car("toyota","corolla")
ob2= car("toyotaaaaa","corollaaaa")
print(ob.brand)
print(ob.model)
print(ob2.brand)
print(ob2.model)
