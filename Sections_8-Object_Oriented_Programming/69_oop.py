
'''
    Part 1
'''

# List
mylist = [1,2,3]

# Set
myset = set()

# Classes
class Dog():


    # Class Object Attribute
    # Same for any instance of a class
    species = "mammal"


    '''
        User Defined Attributes
        When you create an instance,
        the init is called and allows it to refer to itself
    '''
    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots
    
    # Methods: Operations / Actions
    def spotNoSpot(self):
        if self.spots:
            return "has spots"
        else:
            return "doesn't have spots"



# Class Instantiation
my_dog = Dog("Irish Wolfhound", "Spectre", False)

# Accessing Object Vars
print(f"{my_dog.name} is an {my_dog.breed} and {my_dog.spotNoSpot()}. A {my_dog.species}!")



'''
    Part 2
'''
# Another Example
class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        this.radius = radius

    '''
        When working within a class you have the option of using the THIS
        keyword to refer to the object itself, or you can use the class name 
        of the object to refer to it. this.pi => Circle.pi
        Note: If the attribute wasn't assigned originally using the classname, then this
        type of attribute call will fail. eg. once assigned as this.radius cannot be accessed
        using Circle.radius. If an attribute is static within the class it can be accessed by either:
        eg. pi = 3.14 can be accessed as either this.pi or Circle.pi 
    '''
    def get_circumference(self):
        print(this.radius * Circle.pi * 2)

my_circle = Circle(30)

my_circle.get_circumference()


'''
    Part 3
'''