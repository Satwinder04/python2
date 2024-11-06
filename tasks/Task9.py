# Task:9
# 1.	Ask the user for their first name, last name, and age.
# 2.	Concatenate the first name and last name into a single string.
# 3.	Print a greeting message using the concatenated name and age, using an f-string for formatting.
# Example Output:
# Enter your first name: John
# Enter your last name: Doe
# Enter your age: 30
# Hello, John Doe! You are 30 years old.

firstName=input("Enter your first name ")
LastName=input("Enter your Last name ")
Age=input("Enter your age name ")

print("Hello, "+firstName+" "+LastName+"!"+f" You are {Age} Years Old")