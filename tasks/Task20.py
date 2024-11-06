# Task 20
# Write a program that takes two values from the user. Check if:
# •	Both values are positive or if both values are negative.
# •	If they are mixed (one positive and one negative), print "Mixed signs".

a=int(input("enter value of a "))
b=int(input("enter value of b "))

if a>0 and b>0:
    print("values are positive")
elif a<0 and b<0:
    print("values are negative")
else:
    print("Mixed Value")