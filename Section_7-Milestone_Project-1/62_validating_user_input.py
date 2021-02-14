
def user_choice():
    choice = "Wrong"
    while not choice.isdigit():
        choice = input("Please enter a number (0-10): ")
        if not choice.isdigit():
            print("Invalid Input!")
    return int(choice)

print(type(user_choice()))