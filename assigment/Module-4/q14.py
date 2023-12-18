# How many except statements can a try-except block have? Name Some built-in exception classes:

def vell(x, y): 
    try: 
        result = x // y 
        print("Yeah ! Your answer is :", result) 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ")

vell(20,30)