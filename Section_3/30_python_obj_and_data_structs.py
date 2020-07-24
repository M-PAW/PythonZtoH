
import math

### Python Objects and Data Structures
## Test / Exam

'''
Describe each of the following:

    Numbers: a data type called integer
    Strings: a composite data type made of chars
    Lists: a mutable and indexable list/array of variables not restricted to variable type
    Tuples: a non-mutable and indexable list/array of variables not restricted to variable type
    Dictionaries: a mutable list of key value pairs

'''

# Numbers
print((20*4)+(7*3)-0.75)            # equals 100.25

'''
    What are the values of the following expressions:

    4 * (6 + 5)  // 44
    4 * 6 + 5    // 29
    4 + 6 * 5    // 34
'''

print(4*(6+5))          # 44
print(4*6+5)            # 29
print(4+6*5)            # 34

'''
    What is the data type of the following equation:

    3 + 1.5 + 4 // float

'''

print(type(3+1.5+4))    # float


'''
    For the number 9, find the square root and the square:
'''

print(math.sqrt(9))
print(math.pow(9,2))


'''
    Given the word 'Hello', use an index command that returns the letter 'e'
    Then reverse the string using slicing
    Lastly, give two method of producing the last letter, 'o'
'''
word = 'Hello'
print(word[1])
print(word[::-1])
print(word[4])
print(word[-1])

'''
    Build the list [0,0,0] two separate ways
'''
list1 = [0] * 3

list2 = []
while len(list2) < len(list1):
    list2.append(0)

list3 = []
list_size = 3
for i in range(list_size):
    list3.append(0)

print(list1)
print(list2)
print(list3)

'''
    Reassign 'hello' in this nested list to say 'goodbye'
'''
list4 = [1,2,[3,4,'hello']]

list4[2][2] = 'goodbye'

print(list4)

'''
    sort the list below
'''
list5 = [5,3,4,6,1]
list5.sort()
print(list5)

list5 = [5,3,4,6,1]
# list5.sort() is also acceptable
print(sorted(list5))

'''
    Dictionaries
    Using keys and indexing, grab the 'hello' from the following dictionaries:
'''

d = {'key1': 'hello'}
print(d['key1'])

d = {'k1': {'k2':'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

'''
    What is the major difference between tuples and lists?

    How do you create a tuple
'''

# a tuple is immutable
t = (1,2,3)
print('t is type:', type(t))

'''
    What is unique about a set?
    
    Use a set to find the unique values of the list below.
'''

# a set cannot have duplicates

ls5 = [1,2,2,33,4,4,11,22,3,3,2]
# ls.set() is also acceptable
print(set(ls5))

'''
    What is the output of the boolean expression bellow.
'''

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

if l_one[2][0] >= l_two[2]['k1']:
    print("Wrong, it's true.")
else:
    print("Correct, it's false")

