import datetime
# for i in range(0,5):
#     c=datetime.datetime.now()
#     print(c)
# cdate=datetime.date.today()
# print(cdate)
# date=datetime.date(2025,12,4)
# print(date)
# time=datetime.time(6,12,4)
# print(time)


# now=datetime.datetime.now()
# print("year :",now.year)
# print("month :",now.month)
# print("day :",now.day)
# print("hour :",now.hour)
# print("minute :",now.minute)
# print("sec :",now.second)
#
# today=datetime.date.today()
# futrue_date=today+datetime.timedelta(days=10)
# print(futrue_date)


# 1. Write a program to display the current date and time in the format YYYY-MM-DD HH:MM:SS.
# c=datetime.datetime.now().time()
# print(c)

# 2. Write a program to extract and display the year, month, and day from the current date.
# c=datetime.datetime.now()
# print(c.year)
# print(c.day)
# # print(c.date)
# print(c.hour)
# print(c.minute)
# print(c.second)
# print(c.microsecond)
# 3. Write a program to calculate the number of days between 2024-01-01 and the current date.
# a=datetime.date(2024,1,1)
# b=datetime.date.today()
# dif=abs(b-a)
# print(dif.days ,"days")
# 4. Write a program to display only the current date without the time.
# cdate=datetime.date.today()
# print(cdate)
# 5. Write a program that adds 15 days to the current date and displays the resulting date.
# today=datetime.date.today()
# futrue_date=today+datetime.timedelta(days=15)
# print(futrue_date)
# 6. Write a program to display the current date in the following formats: MM/DD/YYYY
# cdate=datetime.date.today()
# print(f"{cdate.month}/{cdate.day}/{cdate.year}")
# 7. Write a program to calculate the difference in hours, minutes, and seconds between two given times: 10:30:00 and 14:45:30.
# a=datetime.time(10,30,0)
# b=datetime.time(14,45,30)
# print(f"{abs(a.hour-b.hour)}:{abs(a.minute-b.minute)}:{abs(a.second-b.second)}")
# from datetime import datetime
# a=datetime.strptime("10:30:00","%H:%M:%S")
# b=datetime.strptime("14:45:30","%H:%M:%S")
# print(abs(a-b))
# 8. Write a program to create a datetime object for 15th August 2025, 10:30:00 AM and display it in YYYY-MM-DD HH:MM:SS format.
# y=int(input("year "))
# Mo=int(input("month "))
# d=int(input("date "))
# h=int(input("hour "))
# m=int(input("min "))
# s=int(input("sec "))
# date=datetime.date(y,Mo,d)
# time=datetime.time(h,m,s)
# # print(f"{date.year}-{date.month}-{date.day} {time.hour}:{time.minute}:{time.second}:{time.microsecond} ")
# print(date,time)
#
import calendar

for day in calendar.day_name:
    print(day)