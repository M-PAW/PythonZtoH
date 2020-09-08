
### Userful Operators in Python

from random import shuffle  # shuffles a list
from random import randint  # grabs a random int

mylist = [1,2,3]
## range() function
for num in range(10):       # up to but not including 10,
    print(num)              # range(start,stop,step)

for num in range(0,10,2):   # prints out every second step
    print(num)

'''
    Enumerate
'''

word = 'abdce'

for index,letter in enumerate(word):    # Enumeration, with unpacking
    print(index)
    print(letter)
    print('\n')


'''
    Zipping
'''

mylist1 = [1,2,3]
mylist2 = ['a','b','c']

for item in zip(mylist1,mylist2):   # Zipping into one by matching index locations
    print(item)

'''
    'in' operator
'''

if 'x' in ['x','y','z']:
    print('True')

if 3 in mylist1:
    print('3 is in mylist1')


'''
    min / max methods
'''
mylist = [10,20,30,40,100]

print(min(mylist))
print(max(mylist))


'''
    Random: Shuffle
'''
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)     # Mutates the list in place, no return value
print(mylist)

'''
    Random: randint
'''
myNum = randint(0,100)
print(myNum)

def GuesNumb():
    myNum = randint(1,10)
    guesses = 3
    print(myNum)



    while guesses:
        guess = int(input("Enter a number: "))
        if int(guess) == myNum:
            print("You Won!")
            guesses = 0
        else:
            if guess > myNum:
                print("Too High!")
            else: print("Too Low!")
            guesses -= 1
            if not guesses:
                print("You Lost!")
                break
            print(f"Wrong! {guesses} guesses remaining.")

#GuesNumb()

import unittest
def addTwo():
    return 1+2

assert addTwo() == 3