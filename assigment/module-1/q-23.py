# Write a Python function to insert a string in the middle of a string
original_string = input("Enter the original string: ")
word_to_insert = input("Enter the word to insert in the middle: ")

if len(original_string) >= 2:
    result = original_string[:2] + word_to_insert + original_string[2:]
    print("Modified String:", result)
else:
    print("Original string should have at least 2 characters.")
