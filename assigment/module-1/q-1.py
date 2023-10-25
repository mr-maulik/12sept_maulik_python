#q-1.Write a Python program to check if a number is positive, negative or zero.


how = int(input("enter how many time chek number:"))

for i in range(how):
    number = float(input("Enter the value:"))

    if number > 0:
        print('-number is positiv')

    elif number < 0:
        print("-number is nagativ")

    else:
        print("-number is nul")


 