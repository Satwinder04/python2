# # common values between two dictionaries
# dict1={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40
# }
#
# dict2={
#     "a":20,
#     "b":30,
#     "c":40,
#     "d":50
# }
# set1=set(dict1.values())
# set2=set(dict2.values())
# print(set1 & set2)


# q2 create a dictionary and convert its values to set
# dict1={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40
# }
# set1 = set(dict1.keys())
# print(set1)

# q3 find a unique value in a dictionary using set
# dict1={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40,
#     "e":40
# }
# set1 = set(dict1.values())
# print(set1)

#q4 Check if a Set of Keys Exists in a Dictionary

# dict1={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40,
#     "e":40
# }
# set1={"a","b","c","d"}
#
#
# for key in dict1.keys():
#     if key in set1:
#         print("ture",key)
#     else:
#         print("false",key)

#q5 Remove Dictionary Keys That Are in a Set
#
# dict1={
#     "a":10,
#     "b":20,
#     "c":30,
#     "d":40,
#     "e":40
# }
# set1={"a","b","c","d"}
# for key in set1:
#     if key in dict1.keys():
#         dict1.pop(key)
# print(dict1)

# # q6 Convert a Set to a Dictionary with Default Values
#
# set1={"a","b","c","d"}
# defaultv = 3
# res ={}
# for i in set1:
#     res[i]= defaultv
# print(res)

# q7 Find Common Keys Between a Dictionary and a Set
#
# def common(dict1,set1):
#
#
#
#     set2=set()
#     for key in dict1.keys():
#         if key in set1:
#             set2.add(key)
#         else:
#             print("false",key)
#     print(set2)
# dict1={
#      "a":10,
#      "b":20,
#      "c":30,
#      "d":40,
#      "e":40
#     }
# set1={"a","b","c","d"}
# common(dict1,set1)
# 8. Count the Occurrence of Items in a List and Store in a Dictionary
# lst=["a","a","d","d","s","a","a","a","d","f","g","h","j","k"]
# dc={}
# for i in lst:
#     if i in dc:
#         dc[i]+=1
#     else:
#         dc[i]=1
# print(dc)

# 9.Merge Two Sets and Add Their Elements as Keys in a Dictionary
#
# set1={"a","b","c","d"}
# set2={"g","t","s","c"}
# set3 = set1.union(set2)
# res ={}

# for i in set3:
#     res[i]=None
# print(res)
# print(set3)
# print(type(res))
