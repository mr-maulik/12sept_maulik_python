# Write a Python program to map two lists into a dictionary

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# to convert lists to dictionary
res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))