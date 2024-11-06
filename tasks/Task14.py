# Task 14
#
# Write a program that takes three numbers as input and prints the largest of the three.
from logging import lastResort

a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))

if a>b and a>c:
    largest = a
elif b>c and b>a:
    largest = b
else:
    largest = c

print("Greatest no. is ",largest)
