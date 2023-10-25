# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, returninstead of the empty string.
inputString = input("Enter a string: ")

count = 0

for _ in inputString:
    count += 1

newString = inputString[0:2] + inputString[count - 2:count]

print("Input string = " + inputString)
print("New String = " + newString)
