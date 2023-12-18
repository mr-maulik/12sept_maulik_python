# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Recag:
    
    def area(self, w, l):
        area = w * l
        print(area)

width = int(input("Enter the width :"))
lenght = int(input("Enter the lenght :"))

re = Recag()
re.area(width, lenght)