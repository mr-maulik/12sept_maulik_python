# Write a Python program to remove an empty tuple(s) from a list of tuples.

def Remove(tuples):
    for i in tuples:
        if (len(i) == 0):
            tuples.remove(i)
    return tuples


# Driver Code
tuples = [(), ('vivek', '22', '4'), (), ('vasu', 'manthan'),
          ('vinita', 'vikash', '33'), ('', ''), ()]
print(Remove(tuples))

