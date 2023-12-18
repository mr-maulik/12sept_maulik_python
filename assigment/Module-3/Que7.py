# Write a Python program to remove duplicates from a list.



l=[]
n = int(input("Enter the number of element of list: "))
for i in range(n):
    i1=int(input("Enter the element: "))
    l.append(i1)
print(set(l))