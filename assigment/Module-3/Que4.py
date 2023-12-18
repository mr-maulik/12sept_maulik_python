# Write a Python function to get the largest number, smallest num and sum of all from a list.

list=[]

n = int(input("Enter the how many element in list: "))

for i in range(n):
    l1=int(input("Enter the element: "))
    list.append(l1)
print(list)

# create the function
def Max_list(l1):
    print("Maximum number of list is :",max(l1))    #use max function to find maximum number of the list
    print("Minimum number of list is :",min(l1))    #use min function to find minimum number of the list


Max_list(list)  #call the function
print(sum(list)) #print sum of list
