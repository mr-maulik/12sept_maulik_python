# Write a Python program to append text to a file and display the text.

with open("first_file.txt", "a") as fl:
    fl.write("Hello \n")
    fl.write("buddys \n")
    fl.write("how are yo!!!")