# Write a Python program to find the repeated items of a tuple.

x=0
tup=(1,3,4,32,1,1,1)
for i in tup:
    if tup.count(i) > 1:
        x = x+1


print(x)