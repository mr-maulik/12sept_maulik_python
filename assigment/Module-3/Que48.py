# Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))

