# 1. Write a Python script to create a file called example.txt, write the text
# "Python programming is interesting" into it, and close the file.
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\example.txt",'w')
# file.write("Python programming is interesting")
# file.close()
# print("done")
#
# 2. Write a program to read and display the contents of a file named example.txt.
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\example.txt",'r')
# d=file.read()
# file.close()
# print(d)
# print("done")
# 3. Modify a file named log.txt by appending the current date and time at the end of the file.
# import datetime
# dt=str(datetime.datetime.now())
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\log.txt",'a')
# file.write(dt)
# file.close()
# print("done")
# 4. Write a Python program to count the number of words in a file called document.txt.
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\example.txt",'r')
# strr=file.read()
# print(len(strr.split(" ")))
# print(len(strr))
# file.close()
# print("done")
# 5. Read a CSV file named data.csv and print its contents line by line.
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\data.csv",'r')
# d=file.read()
# file.close()
# print(d)
# print("done")
# 6. Write a program to copy the contents of a file source,txt to another file destination.txt.
# file = open(r"D:\BEBO-tech\python\DailyPractice\practice19\source.txt",'r')
# f2 = open(r"D:\BEBO-tech\python\DailyPractice\practice19\copy.txt",'a')
#
# strr=file.read()
# f2.write(strr)
# f2.close()
# file.close()
# print("done")
# 7. Write a script that takes a file name as input and prints the number of
# lines, words, and characters in the file.
fileName=input("enter file name ")
f1=open(fr"D:\BEBO-tech\python\DailyPractice\practice19\{fileName}.txt",'a')
w=input("enter data ")
f1.write(w)
f1.close()
f2=open(fr"D:\BEBO-tech\python\DailyPractice\practice19\{fileName}.txt",'r')
f3=open(fr"D:\BEBO-tech\python\DailyPractice\practice19\{fileName}.txt",'r')
strr=f2.read()
lst=f3.readlines()

print(len(lst))
print(len(strr.split(" ")))
print(len(strr))
print(strr)
print(lst)
print("done")
# 8. Write a program to merge the contents of two files, filel.txt and file2.txt, into a new file called merged.txt.
# f1=open(r"D:\BEBO-tech\python\DailyPractice\practice19\file1.txt",'r')
# f2=open(r"D:\BEBO-tech\python\DailyPractice\practice19\file2.txt",'r')
# strr1=f1.read()
# strr2=f2.read()
# mrge=strr1+" "+strr2
#
# f1.close()
# f2.close()
# f3=open(r"D:\BEBO-tech\python\DailyPractice\practice19\merge.txt",'a')
# f3.write(mrge)
# f3.close()
# print("done")
