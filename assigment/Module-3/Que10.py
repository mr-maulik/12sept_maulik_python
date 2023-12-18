""" Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30."""


def printValue():
    list=[]
    for i in range(1,30):
        x = i**2
        list.append(x)

    print(list)

printValue()
