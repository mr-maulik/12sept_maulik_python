# How Do You Handle Exceptions With Try/Except/Finally In Python? 
 

try:
    k = 7/0 
    print(k)

# handles zerodivision exception    
except ZeroDivisionError:   
    print("Can't divide by zero")
    
finally:
    print('This is always executed') 