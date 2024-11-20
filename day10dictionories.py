# # mydict={
# #     "name":"Satwinder",
# #     "class":"mca",
# #     "rollno":"2310987107"
# # }
#
# mydict1= dict([
#     ("name","bob"),
#     ("age",17)
# ])
# print(mydict1)
# print(mydict1.get("age"))
#
# mydict2= dict(
#     name="Satwinder",
#     age=23
# )
# print(mydict2)
#
# # adding
# mydict3= dict(
#     name="Satwinder",
#     age=23
# )
# mydict3["age"]=24
# print(mydict3)
#
# # adding pair
# mydict4= dict(
#     name="Satwinder",
#     age=23
# )
# mydict4["city"]="patiala"
# print(mydict4)
#
# # del
# mydict5= dict(
#     name="Satwinder",
#     age=23
# )
# del mydict5["age"]
# print(mydict5)
# # pop
# mydict6= dict(
#     name="Satwinder",
#     age=23
# )
# mydict6.pop("age")
# print(mydict6)
#
# # keys
# mydict7= dict(
#     name="Satwinder",
#     age=23
# )
# mydict7.pop("age")
# print(mydict7.keys())
# # value
# mydict8= dict(
#     name="Satwinder",
#     age=23
# )
# mydict8.pop("age")
# print(mydict8.values())
#
# # item
# mydict9= dict(
#     name="Satwinder",
#     age=23
# )
# mydict9.pop("age")
# print(mydict9.items())
#
#
# #update
# mydict10= dict(
#     name="Satwinder",
#     age=23
# )
# mydict11= dict(
#     city="patiala",
#     phn=81445678456
# )
# mydict10.update(mydict11)
# print(mydict10)
#
#
# #update
# mydict12= dict(
#     name="Satwinder",
#     age=23
# )
#
# mydict13=mydict12.copy()
# print(mydict13)
#
# #update
# keys=[1,2,3,4]
# mydict14=dict.fromkeys([1,2,3,4,5],"welcome")
# print(mydict14)
#
# # set default
# mydict15= dict(
#     name="Satwinder",
#
# )
#
# mydict15.setdefault("age",23)
# print(mydict15)
#
# # iterating
# mydict16= dict(
#     name="Satwinder",
#     agw="23"
# )
# for i in mydict16:
#     print(i)
# for i in mydict16.values():
#     print(i)
# for i in mydict16.items():
#     print(i)
#
#
# # square
# sq={x:x**2 for x in range(0,11)}
# print(sq)


# nested dic
# mydict17={
#     '01':{
#         "name":"satwinder",
#         "age":23,
#         "city":"patiala"
#     },
#     '02':{
#         "name":"sunil",
#         "age":22,
#         "city":"bhiwani"
#     },
#     '03':{
#         "name":"aman",
#         "age":15,
#         "city":"bhihar"
#     }
# }
# print(mydict17['01']["name"])
# print(mydict17['03']["city"])

#
# mydict10= {
#     "name":"satwinder",
#     "age":23,
#     "city":"patiala"
# }
# mydict11= {
#     "age":23,
#     "phn":8146254176
# }
# dictt= set(mydict10.values()) ^ set(mydict11.values())
# print(dictt)



#
# mydict10= {
#     "name":"satwinder",
#     "age":23,
#     "city":"patiala"
# }
# keys=set(mydict10.keys())
# print(keys)
#
mydict10= {
    "name":"satwinder",
    "age":23,
    "city":"patiala"
}
dc= {
    "name":"satwinder"
}
z = set(dc).issubset(set(mydict10))
print(z)
# for i in mydict10:
#     if i in dc:
#
#     else:
#
# print(dc)
#
