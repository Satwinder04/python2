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
#
#
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
#
#
#
# mydict10= {
#     "name":"satwinder",
#     "age":23,
#     "city":"patiala"
# }
# keys=set(mydict10.keys())
# print(keys)
#
# mydict10= {
#     "name":"satwinder",
#     "age":23,
#     "city":"patiala"
# }
# dc= {
#     "name":"satwinder"
# }
# z = set(dc).issubset(set(mydict10))
# print(z)
# # for i in mydict10:
# #     if i in dc:
# #
# #     else:
# # print(dc)
# from DailyPractice.practice7 import list2
#
# #write a program to update the dictionary
# dict1= {
#     'john':45,
#     'ritesh':80,
#     'amar':78
# }
# dict2={
#     'amar':60
# }
# dict1.update(dict2)
# print(dict1)
#
# dict1={
#     '1':1,
#     '2':1,
#     '3':1,
#     '4':1,
#     '5':1,
# }
# print(sum(dict1.values()))

# tuple1=(1,2,3,4,5)
# list1=list(tuple1)
# n=int(input())
# list1.append(n)
# tuple2 = tuple(list1)
# print(tuple2)
#
# set1={10,20,30,56,40}
# list1=list(set1)
# mx,mn=list1[0],list1[0]
# for i in set1:
#     if i>mx:
#         mx=i
#     elif i<mn:
#         mn=i
# set2=set(list1)
# set2.remove(mx)
# set2.remove(mn)
# print(set2)

#
# set1={1,2,3,6,8,9}
# list1=list(set1)
# mx,mn=float('-inf'),float('inf')
# for i in set1:
#     if i>mx:
#         mx=i
#     if i<mn:
#         mn=i
# set2=set(list1)
# print(mx,mn)
# set1.remove(mx)
# set1.remove(mn)
# print(set1)
#
# set1= set(map(int,input("enter set1 : ").split(" ")))
# set2= set(map(int,input("enter set2 : ").split(" ")))
#
# print(set1^set2)

#Write a python function that finds and returns the index of all
# occurrences of a specified element ina list using the index method() 
# If the element is not found returns none.
# def find_all_indexes(lst, element):
#     indexes = []
#     start = 0
#     while True:
#         try:
#             index = lst.index(element, start)
#             indexes.append(index)
#             start = index + 1
#         except ValueError:
#             break
#     if indexes:
#         return indexes
#     else:
#         return None
#
#
#
# lst = [1, 2, 3, 2, 4, 2, 5]
# element = 2
# print(find_all_indexes(lst, element))
#
# element = 6
# print(find_all_indexes(lst, element))
#








# Write a python function that finds and returns the index of all
# occurrences of a specified element in a list using the index method()
# If the element is not found returns none.

# list1=[1,3,2,5,2,5]
# ind=[]
# c=int(input("enter value "))
# for i in range(len(list1)):
#     if list1[i]==c:
#         # n=list1[i]
#         ind.append(i)
#
# print("index",ind,"value",c)

# write a python code that find keys in a dict that have specific value
v=int(input("enter value "))
dict1={
    'a':1,
    'b':3,
    'c':1,
    'd':4,
    'e':5
}
for key,value in dict1.items():
    if value == v:
          print(key)
