# How can you pick a random item from a range?

# importing random module
import random
print('Random Numbers from 1 to 50 are:')

# getting a random number from 1 to 50
x=random.randrange(1,50)
print(x)

# getting an alternative(odd number) random number from 1 to 50
y=random.randrange(1,50,2)
print(y)