
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
#print(f"{my_dog.name} is an {my_dog.breed} and {my_dog.spotNoSpot()}. A {my_dog.species}!")



'''
    Part 2
'''
# Another Example
class Circle():

    pi = 3.14

    def __init__(self, radius=1):

        Circle.radius = radius

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
        print(Circle.radius * Circle.pi * 2)

#my_circle = Circle(30)

#my_circle.get_circumference()



'''
    Part 3
'''
class Line:

    def __init__(self,coor1,coor2):
        Line.coor1 = coor1
        Line.coor2 = coor2

    def distance(self):
        # Unpack the tupple
        x1,y1 = Line.coor1
        x2,y2 = Line.coor2

        print(((x2 - x1)**2 + (y2 - y1)**2)**0.5)

    def slope(self):
        # Unpack the tupple
        x1,y1 = Line.coor1
        x2,y2 = Line.coor2

        print((y2-y1)/(x2-x1))

coordinate1 = (3,2)
coordinate2 = (8,10)

myLine = Line(coordinate1,coordinate2)

#myLine.distance()

#myLine.slope()


## Cylinder Class
class Cylinder:

    def __init__(self, height=1, radius=1):
        Cylinder.height = height
        Cylinder.radius = radius

    def volume(self):
        print(Cylinder.height * 3.14 * (Cylinder.radius)**2)

    def surface_area(self):
        top = 3.14 * (Cylinder.radius**2)
        print((2*top) + (2*3.14*Cylinder.radius*Cylinder.height))

myCylinder = Cylinder(2,3)

#myCylinder.volume()

#myCylinder.surface_area()


'''
    OOP Programming Challenge, Bank Account
'''

class Account:
    def __init__(self, owner,balance):
        Account.owner = owner
        Account.balance = balance

    def deposit(self):
        deposited = int(input("How much would you like to deposite? "))

        Account.balance = Account.balance + deposited

        print("You successfully deposited ${:.2f}, your new balance is ${:.2f}".format(deposited,Account.balance))

    def withdraw(self):
        
        withdrawn = int(input("How much would you like to withdraw? "))

        if withdrawn > Account.balance:
            print("You have insufficient funds.")
        else:
            Account.balance = Account.balance - withdrawn

            print("You successfully withdrew ${:.2f}, your new balance is ${:.2f}".format(withdrawn,Account.balance))

    def checkbalance(self):
        print("Your current account balance is ${:.2f}".format(Account.balance))

# Step 1, Instantiate the class with an owner and initial balance

accnt145 = Account("Jones",150.00)

# Step 2, Create a method to check the account balance

accnt145.checkbalance()

# Step 3, Create a method to withdraw from the account

accnt145.withdraw()

# Step 4, Create a method to deposite into the account

accnt145.deposit()