# Write a Python function to check whether a number is in a given range


def count(list1, l, r):
    c = 0
    # traverse in the list1
    for x in list1:
        # condition check
        if x >= l and x <= r:
            c += 1
    return c


# driver code
list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
l = 40
r = 80
print(count(list1, l, r))
