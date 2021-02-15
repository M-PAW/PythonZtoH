
#Game List
game_list = [0,1,2]

# Game On/Off 
game_on = True

# Display Function
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


# Position Choice Function
def position_choice():

    choice = 'wrong'

    while choice not in ['0','1','2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0','1','2']:
            print("Sorry, invalid choice!")

    return int(choice)


# Replacement Function
def replacement_choice(game_list, position):

    user_placement = input("Type a string to place at position: ")

    game_list[position] = user_placement

    return game_list

# Game-on Function
def gameon_choice():

    choice = 'wrong'

    while choice.lower() not in ['y','n']:

        choice = input("Keep playing? (Y or N) ")

        if choice.lower() not in ['y','n']:
            print("Sorry, I didn't catch that.  Please try again.")

    if choice.lower() == "y":
        return True
    else:
        return False


while game_on:

    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice ()
