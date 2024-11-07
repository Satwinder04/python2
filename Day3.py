# range


# print(list(range(6,10)))

# print(list(range(1,10,2))) #odd
# print(list(range(0,11,2))) #even
#
# print(list(range(10,0,-1)))#-ve
# -------------------------------------------------------------------------

# Loopes

# intilization
# condition
# inc/dec

# i=1
# while i<=10:
#     print(i)
#     i+=1 # i=i+1
# print("done")

# i=10
# while i>=1:
#     print(i)
#     i-=1 # i=i-1
# print("done")
#
# i=1
# while i<=100:
#     print(i)
#     i+=1 # i=i+1
# print("done")


# N=int(input("enter the value of N "))
# i=1
# sum=0
# while i<=N:
#     sum+=i
#     i+=1
# print(sum)

# n=int(input("enter the value of n "))
# i=1
# fact= 1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)

#Reverse

# n=int(input("enter the number "))
# i=1
# rev=0
# while n!=0:
#     rem= n%10
#     rev = rev*10 + rem
#     n= n//10
#     i+=1
# print(rev)

# #count
#
# n=int(input("enter the number "))
# i=1
# rev=0
# count=0
# while n!=0:
#     rem= n%10
#     count+=1
#     n= n//10
#     i+=1
# print(count)

# sum = 0
# for i in range(1,101):
#     sum +=i
# print(sum)

# n=  int(input("enter value of n "))
# sum = 0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

# n=  int(input("enter value of n "))
# for i in range(0,n+1,2):
#     print(i)
#
#factorial

# n=  int(input("enter value of n "))
# fact = 1
# for i in range(1,n+1):
#     fact *=i
# print(fact)

# multiple

# n=  int(input("enter value of n "))
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")


# n no. of prime no.
#
# n = int(input("enter value of n "))
# is_prime=True
# for i in range(2,n):
#     if n%i==0:
#         is_prime =False
#         break
#
# if is_prime:
#     print("prime")
# else:
#     print("not Prime")

# n = int(input("enter value of n "))
# is_prime=True
# for i in range(2,int(n/2)+1):
#     if n%i==0:
#         is_prime =False
#         break
# if is_prime:
#     print("prime")
# else:
#     print("not Prime")


