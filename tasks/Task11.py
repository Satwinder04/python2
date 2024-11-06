# Task:11
#  Create a program that demonstrates the usage of bitwise operators.
# 1.	Define two integers, a and b, with values of your choice.
# 2.	Perform the following bitwise operations and print the results:
# •	AND (&)
# •	OR (|)
# •	XOR (^)
# •	NOT (~)
# •	Left Shift (<<)
# •	Right Shift (>>)

a=int(input("Enter value of a "))
b=int(input("Enter value of b "))


print(a&b)
print(a|b)
print(a^b)
print(~b)
print(a>>b)
print(a<<b)