# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if(i%3==0 and i%5==0):
#             print("FizzBuzz")
#         elif(i%3==0):
#             print("Fizz")
#         elif(i%5==0):
#             print("Buzz")
#         else:
#             print(i)
#
# s=int(input())
# fizz_buzz(s)
#
# from imaplib import Flags
# from itertools import count
# from multiprocessing.reduction import duplicate

# def sum(a,b):
#     return a+b
#
# a=int(input("enter value of a "))
# b=int(input("enter value of b "))
# print(sum(a,b))
#


# # 1. Remove Duplicates
# def r_d(l):
#     s, r = set(), []
#     for i in l:
#         if i not in s:
#             r.append(i)
#             s.add(i)
#     return r
#
# print(r_d([1, 2, 2, 3, 4, 4, 5]))
#
# # 2. Minimum and Maximum Tuple
# def m_m(t):
#     return (min(t), max(t))
#
# print(m_m((4, 1, 8, 3, 9)))  # (1, 9)
#
# # 3. Prime Numbers in a Range
# def p_n(s, e):
#     def i_p(n):
#         if n < 2:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     return [n for n in range(s, e + 1) if i_p(n)]
#
# print(p_n(10, 20))  # [11, 13, 17, 19]
#
# # 4. Second Largest Number
# def s_l(l):
#     u = sorted(set(l), reverse=True)
#     return u[1] if len(u) > 1 else None
#
# print(s_l([10, 20, 4, 45, 99, 99]))  # 45
#
# # 5. Convert to Title Case



# list = list(input("Enter the List : "))
# list1 =[]
# for i in list:
#     duplicate=False
#     for j in list1:
#         if i==j:
#             duplicate=True
#             break
#     if not duplicate:
#         list1.append(i)
# print(list1)
#
# list=list(map(int, input("Enter list ").split(" ")))
#
#
# i=0
# while(i<len(list)):
#     j=i+1
#     while(j<len(list)):
#         if list[i]==list[j]:
#             list.pop(j)
#         else:
#             j=j+1
#     i=i+1
# print(list)

# t=(1,2,3,4,5,7)
# def mm():
#     return (min(t),max(t))
# print(mm())

# n=tuple(map(int,input("enter tuple ").split(" ")))
# # mn=n[0]
# # mx=n[0]
# def mm():
#     mn= mx = n[0]
#     for i in n:
#         if i<mn:
#             mn=i
#         if i>mx:
#             mx=i
#     return(mn,mx)
# print(mm())

# n = int(input("enter value of n "))
# start = int(input("enter Start value "))
# end = int(input("enter end value "))
# list =[]
# count = 0
# for j in range(start,end+1):
#     if j>1:
#         is_prime=True
#         for i in range(2, j):
#             if j%i == 0:
#                 is_prime=False
#                 break
#         if is_prime:
#             list.append(j)
#             count+=1
# print(f"prime no. {list} and end {count}")



    # if start%i==0:
    #     is_prime = True
    #     break

# if is_prime:
#     list.append(i)
#     print(list)
# else:
#     print("not Prime")
# s=input("enter String ")
# def tc(s):
#     return s.title()
#
# print(tc(s))







#
#
# # Prime Numbers Function
# def prime_numbers(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if num > 1:
#             for i in range(2, int(num**0.5) + 1):
#                 if num % i == 0:
#                     break
#             else:
#                 primes.append(num)
#     return primes
#
# print(prime_numbers(10, 20))


# list=[3,4,5,6,7]
# list2=list.sort()
# secondlargest=(len(list2)-2)
# print(secondlargest)

# print(list[secondlargest])