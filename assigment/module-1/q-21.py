# Write a Python function to reverses a string if its length is a multiple of 4

str1 = input("Enter a string: ")

if len(str1) % 4 == 0:
    reversed_str = ''.join(reversed(str1))
    print("Reversed string:", reversed_str)
else:
    print("String length is not a multiple of 4. The original string is:", str1)
