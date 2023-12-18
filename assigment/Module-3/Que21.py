# Write a Python program to convert a tuple to a string.


def convertTuple(tup):
    
    str = ''
    for item in tup:
        str = str + item
    return str


# Driver code
tuple = ('p', 'a', 'r', 't', 'h')
str = convertTuple(tuple)
print(str)