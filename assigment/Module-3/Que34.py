# Write a Python script to check if a given key already exists in a dictionary.

def checkKey(dic, key):
    if key in dic.keys():
        print("Present, ", end =" ")
        print("value =", dic[key])
    else:
        print("Not present")
        
# Driver Code
dic = {'a': 100, 'b':200, 'c':300}
key = 'b'
checkKey(dic, key)

key = 'w'
checkKey(dic, key)