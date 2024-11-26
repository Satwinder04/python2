# n=int(input("enter value of n "))
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end= " " )
#     print()


# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# f=0
# s=1
# temp=0
# n=int(input("enter value of n "))
# for i in range(0,n-1):
#     temp = f+s
#     f=s
#     s=temp
# print(temp,end=" ")
#
#
import random
gnum=random.randint(1,100)
steps=0
while True:
    n=int(input("Enter the number "))
    steps+=1
    if n==gnum:
        print(f"Number is found in {steps} steps")
        break
    elif n<gnum:
        print("Please enter the higher ")
    else:
        print("Please enter the lower number")








