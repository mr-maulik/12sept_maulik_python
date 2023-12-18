""" Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}] """


a=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
cp={}
val=0
for d in a:
    if d['item'] not in cp:
        cp[d['item']] = d['amount']
    else:
        cp[d['item']] += d['amount']
print(cp)
