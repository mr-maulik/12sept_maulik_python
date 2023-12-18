# Write a Python program to write a list to a file.

l = ['rachit','chaman','maulik']

# open file
with open('name.txt', 'w+') as f:

    # write elements of list
    for items in l:
        f.write('%s\n' %items)
    
    print("File written successfully")


# close the file
f.close()