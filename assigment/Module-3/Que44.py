# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}


import itertools

# Create a dictionary 'd' with keys '1' and '2', and associated lists of characters as values.
d = {'1': ['a', 'b'], '2': ['c', 'd']}

# Iterate through combinations of values from the dictionary 'd' using 'itertools.product'.
# The values are sorted based on their keys to ensure a specific order.
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    # Print the combinations as strings by joining the characters in each combination.
    print(''.join(combo))