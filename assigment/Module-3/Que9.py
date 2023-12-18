""" Write a Python function that takes two lists and returns true if they have 
at least one common member. """

def has_common_member(list1, list2):
   
    common_elements = set(list1) & set(list2)
   
    return bool(common_elements)

list_a = [1, 2, 3, 4, 5]
list_b = [5, 6, 7, 8, 9]

result = has_common_member(list_a, list_b)

print("List A:", list_a)
print("List B:", list_b)
print("Has Common Member:", result)
