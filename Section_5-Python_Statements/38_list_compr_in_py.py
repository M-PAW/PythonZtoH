
'''
    List Comprehensions in Python:

        A unique way of quickly creating a list in python.

        If you find yourself using a for loop combined with .append(),
        it might be better to use a Comprehension instead.


'''
import timeit

# Method 1
mystring = "hello"
mylist = []

start = timeit.default_timer()
for letter in mystring:
    mylist.append(letter)
stop = timeit.default_timer()

print(mylist)
print('Time:', stop - start)

# Method 2
mystring = "hello"
start = timeit.default_timer()
mylist = [letter for letter in mystring]    # Flattened out for loop
stop = timeit.default_timer()

print(mylist)
print('Time:', stop - start)


### Generate a list of numbers
mylist = [num for num in range(0,11)]             ## Generates a list of nums in range
print(mylist)

mylist = [num**2 for num in range(0,11)]          ## Operations can be performed on the first num
print(mylist)

mylist = [num**2 for num in range(0,11) if num%2==0] ## Can add a condition to the end
print(mylist)

celcius = [0,10,20,34.5]

fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

print(fahrenheit)

"""
    If else statements in a list comprehension
    Looks like garbage but functions
"""

result = [ 'EVEN' if x%2==0 else 'ODD' for x in range(0,11)]    # Confusing by its appearance
print(result)


'''
    Nested loop in list comprehensions
'''

mylist = [x * y for x in [2,4,6] for y in [1,10,1000]] 

print(mylist)


mylist = []
for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)

print(mylist)

