'''
    Tuples with Python
     not mutable
'''

t = ('a','a','b')

mylist = [1,2,3]

print("tuple type:", type(t))
print("mylist type:",type(mylist))

print("t[1]: ", t[1])                   # index through tuple
print("t[-2]:", t[-2])                  # reverse index through tuple
print("t.count('a')", t.count('a'))     # Counts the number of occurances for a char in tuple
print("t.index('a')", t.index('a'))     # returns the idx loc of the first occurance



