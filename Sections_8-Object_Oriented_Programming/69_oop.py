
# List
mylist = [1,2,3]

# Set
myset = set()


# Classes
class Dog():
    '''
        When you create an instance,
        the init is called and allows it to refer to itself
    '''
    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots
    
    def spotNoSpot(self):
        if self.spots:
            return "has spots"
        else:
            return "doesn't have spots"



#Class Instantiation
my_dog = Dog("Irish Wolfhound", "Spectre", False)

#Accessing Object Vars
print(f"{my_dog.name} is an {my_dog.breed} and {my_dog.spotNoSpot()}")
