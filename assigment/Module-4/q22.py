# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class 

# define the class is class keyword
class f_cla:
    # the self is defoult argument in function
    def sum(Self ,a ,b):
        sum = a + b
        print(sum)
        
    # the self is defoult argument in function
    def sub(Self ,a ,b):
        sub = a - b
        print(sub)

fo = f_cla()
fo.sum(30,50)
fo.sub(50,60)