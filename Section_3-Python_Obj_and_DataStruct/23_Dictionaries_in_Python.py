
### Dictionaries in Python

price_lookup = {
    'apple': 2.99, 
    'oranges': 1.99,
    'mile': 5.80,
    }

item = 'apple'  # Variable holding the item being searched

d = {'k1':123, 'k2':[0,1,'c'], 'k3':{'insidekey':100}}

d['k2'][1] = 'one' # reassign a new value to an index, for list inside a dictionary

print(item, price_lookup[item])                 # Looking up an item by it's key
print("Nested List:", d['k2'])                  # prints the list from the dictionary
print("Index of Nested List:", d['k2'][2])      # prints value at index of dict nested list
print("Nested key pair:", d['k3']['insidekey']) # prints value of the nested key pair
print("Index of Nested List to Upper:", d['k2'][2].upper())
print("D:", d.keys())                           # prints all of the dictionary keys
print("D:", d.values())                         # prints all of the dictionary values
print("D:", d.items())                          # prints all of the pairs as tuples
                                            ## Is there a way to target index with .items() ?