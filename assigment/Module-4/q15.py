# When will the else part of try-except-else be executed? 


def elt(x, y): 
    try: 
        result = x // y 
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print("Yeah ! Your answer is :", result) 


elt(4, 2) 
elt(2, 0)