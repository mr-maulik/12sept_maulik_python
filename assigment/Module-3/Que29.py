# Write a Python program to unzip a list of tuples into individual lists.

l = [(1, 2), (3, 4), (8, 9)]


result = list(zip(*l))

# Print the result, which is a list of two tuples formed by zipping the original tuples.
print(result)
