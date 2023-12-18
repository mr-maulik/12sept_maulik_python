# Write a Python program to replace last value of tuples in a list.

l = [(10, 20, 40)]
print([t[:-1] + (55,) for t in l])
