# How can you pick a random item from a list or tuple?

""" 1. Use the import keyword to import the random module(used to generate random integers. ...
2. Create a tuple and add some dummy data to it.
3. Generate a random item from the tuple using random. ...
4. Print the generated random tuple item."""

# importing random module
import random
# input tuple
inputTuple = (30, 10, "TutorialsPoint", 20, "python", "code")
# printing the given input tuple
print("The given input tuple: ", inputTuple)
# generating a random item from the tuple using random.choice() method
randomItem = random.choice(inputTuple)
print("The generated random tuple item = ", randomItem)