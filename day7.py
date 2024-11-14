from turtledemo.sorting_animate import ssort

# s="Satwinder04"
# d="Satwinder"
# l="lower"
# u="UPPER"
# print(l.islower())
# print(u.isupper())
#
# print(s.isalpha())
# print(s.isalnum())
# print(s.isdigit())
#
# print(d.isalpha())
# print(d.isalnum())
# print(d.isdigit())
#
# print(s.find('e')) #it will give index
# print(s.count('e')) # it wil give no of ocurence


# s="string in python"
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.replace("in" , "on"))


# Reverse a string

# s= input()
# rev=""
# for i in s:
#     rev = i+rev
# print(s+" "+rev)
#
# rev=s[::-1]
# if(s==rev):
#     print("palindrome")
# else:
#     print("not palindrome")
# print(rev)


# anagram
# s=input()
# d=input()
#
# if len(s)==len(d):
#     if sorted(s)==sorted(d):
#         print("anagram")
#     else:
#         print("not anagram")
# else:
#     print("not anagram")



# collection

# a=10
# s="welcome"
# d = 10.5

# list  - concept of indexing , starts form 0 - mutable - []
# Tuple -
# Set
# Dictionary


# list= [10,20,30,40,50,60,70]
# list2 = ["satwinder","amar","aman","sunil"]
# listcopy = list2
# listcopy[2] = "satwinder"
# print(listcopy)
# print(list2)




# list3= ["satwinde","amar","aman","sunil",1,2,3,4]
# list4= list() # empty list

# print(list)
# print(list2)
# print(list3)

# indexing
# print(list[1])
# print(list[2])
# print(list[-1:-4])


# chk if elemnt exit or not
#
# list2 = ["satwinder","amar","aman","sunil"]
# for i in range(len(list2)):
#     if "satwinder" in list2:
#         print("preasent")
#         break
#     else:
#         print("not present")


# add element in list
# list2 = ["satwinder","amar","aman","sunil"]
# # list2.append("retesh")
# # list2.pop(1)
# # del list2
# list2.clear()
# list2.insert(1,"retesh")
# print(list2)



# pailendrom
# anagram
# count the no. vowels in the sring
# count the no. words
# remove all the spaces from the string
# strng into uprcase
# impliment the concept of the tuple

# Function to count the number of vowels in a string
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = sum(1 for char in s if char in vowels)
#     return count
#
# # Example usage
# s = input("Enter a string: ")
# vowel_count = count_vowels(s)
# print(f"Number of vowels in the string: {vowel_count}")