'''
    Three Cup Monte
'''

# example = [1,2,3,4,5,6,7]

from random import shuffle

# result = shuffle(example)
# print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

# print(result)

def player_guess():

    guess = ''

    while guess not in ['0','1','2']:   
        guess = input("Pick a number: 0,1 or 2: ")
        print(guess)

    return int(guess)


def check_guess(myList,myIndex):
    if myList[guess] == "O":
        print("Corret!")
    else:
        print("Wrong Guess!")
        print(f"It was at index {myList.index('O')}!")

guess = player_guess()
mixed_list = shuffle_list(['X','O','X'])

check_guess(mixed_list, guess)