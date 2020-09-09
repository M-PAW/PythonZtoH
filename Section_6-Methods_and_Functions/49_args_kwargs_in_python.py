
#def myfunc(a,b):
    # returns 5% of the sum of a and b
#    return sum((a,b)) * 0.05

'''
    *args create tuples
    **kwargs creates a dictionary of key-value pairs
'''

# def myfunc(*args):
#     return sum(args) * 0.05

def myfunc(**kwargs):
    if 'fruit' in kwargs:
        return ('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        return ('I did not find any fruit here.')

# print(myfunc(fruit='apple', veggie = 'lettuce'))

def myfunc2(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc2(10,20,30, fruit='orange', food='eggs',animal='dog' )