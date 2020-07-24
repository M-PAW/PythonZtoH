
### For Loops in Python

my_iterable = [1,2,3]

for item in my_iterable:    # print each individual item
    print(item)


mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print("外国人!")


for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')


list_sum = 0

for num in mylist:
    list_sum += num

print(list_sum)

mystring = "Hello World"

for letter in mystring:
    print(letter)

tup = (1,2,3) # tuples, tuple unpacking

for item in tup:
    print(item)

'''
    List of tuples, common in python
'''
mylist = [ (1,2),(3,4),(5,6),(7,8) ]

print(f'Length: {len(mylist)}')

for item in mylist:
    print(item)


## Tuple Unpacking

for (a,b) in mylist:
    print(f'a: {a}')
    print(f'b: {b}')


mylist = [ (1,2,3),(5,6,7),(8,9,10)]

for a,b,c in mylist:
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

### Iterate through a Dictionary

d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:          # Only iterates through the keys
    print(item)

for item in d.values():
    print(item)         # Prints only the values

for item in d.items():  # Prints the key pairs
    print(item)

for key, value in d.items():
    print(value)


