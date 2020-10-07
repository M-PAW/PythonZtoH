
'''
    Lambda Expressions: Map and Filter
'''

## Test data 
test_data = [1,2,3,4,5]

## Map, a built in function
def square(num):
    return num**2

'''
 Map will return the address of a new object in memory.
 If you pair it with a for loop and work with the items returned
 from each iteration, you can have more direct access to the 
 mutated data.
 map can return individual pieces of data to be printed out to the screen,
 or can be used within list() or set() to return a structured object.
 map() takes a function and a dataset.
''' 
#for item in map(square, test_data):
#     print(item)

#print(list(map(square,test_data)))

## Using map to manipulate data
# def splicer(dataset):
#     if len(dataset)%2 == 0:
#         return 'EVEN'
#     else:
#         return dataset[0]

name = ['Andy','Eve','Sally']

# print(list(map(splicer,name)))



'''
    Filter: looks for and pulls out data matching you target.
    Using a boolean to check for matching value will return True,
    which will cause filter to return the original value in question
    and allow you to add it to a refined data structure.
'''
# def check_even(num):
#     return num%2 == 0

numbs = [1,2,3,4,5,6]

# print(list(filter(check_even,numbs)))


'''
    Converting a function into a Lambda Expression.
    An anonymous function that you plan to only use one time.
'''
# square = lambda num: return num ** 2

#print(list(map(lambda num: num**2, test_data)))

#print(list(filter(lambda even:even%2==0, numbs)))

#print(list(map(lambda name:name[:3], name)))

