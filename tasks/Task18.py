# Task 18
# Write a program to simulate a login system. It should check if:
# 	The entered username matches the stored username and
# 	The entered password matches the stored password.

StoredUser= "satwinder"
StoredPass= "satwinder"

username = input("Enter Username ")
password = input("Enter password ")

if username == StoredUser and password == StoredPass:
    print("user already exist")
else:
    print("logged in")