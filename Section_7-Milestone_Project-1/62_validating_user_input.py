
def user_choice():

    choice = "Wrong"
    acceptable_range = range(0,10)
    within_range = False
    # Two Conditions to check
    # Digit OR within_range == false
    while not choice.isdigit() or not within_range:
        choice = input("Please enter a number (0-10): ")

        # Digit Check
        if not choice.isdigit():
            print("Sorry that is not a digit!")

        # Range Check
        if choice.isdigit():
            if int(choice) in acceptable_range:
                within_range = not within_range
            else:
                print("That number is out of range! ")

            
    return int(choice)

print(user_choice())