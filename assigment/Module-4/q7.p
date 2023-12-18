# Write a Python program to read a file line by line store it into a variable.

f = open("my_file.txt","r")
str=""

for i in range(0,100):
    str=str + f.read(i)

print(str)