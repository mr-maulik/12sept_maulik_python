# Write a Python program to read last n lines of a file. 


s=74 
n=5
def readfile(x):
    print("The total number of lines in the file is",s)
    startline=(s-n)
    print("The last",n,"lines of the file are")
    with open(x,'r') as d:
        for i, l in enumerate(d):
            if (i>=startline):
                print(i)
                print(d.readline())
