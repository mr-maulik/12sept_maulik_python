# Write a Python program to get unique values from a list

list=[]

n = int(input("Enter the number of element :"))

for i in range(n):
    x = int(input("Enter the element : "))
    list.append(x)

print(set(list))