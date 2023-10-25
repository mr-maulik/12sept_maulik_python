"""Write a Python function that takes a list of words and returns the length
of the longest one."""

def count_word_length(my_list):
    counter = 0
    for item in my_list:
        if len(item) >= counter:
            counter = len(item)
    return counter

word_list = input("Enter a list of words separated by spaces: ").split()
result = count_word_length(word_list)
print("The length of the longest word is:", result)
