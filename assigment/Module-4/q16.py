# Can one block of except statements handle multiple exception?


try:
    k = 7//0 
    print(k)

    
except ZeroDivisionError:   
    print("Can't divide by zero")