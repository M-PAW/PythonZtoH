
# Card
# Suit, Rank, Value

# Card Value Dictionary
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 11,
    'Queen': 12,
    'King': 13,
    'Ace': 14
}

# Card Class
class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        # I made a mistake here and believed that .capitalize should 
        # have been applied to the internal assignment of rank
        # when it needed to used on the attribute rank being used
        # to find the value in self.value. 
        # Both are using the same passed in attribute but don't relate to one another.
        self.value = values[rank.capitalize()]

    # This gives a default return when the OBJ is called without an accessor.
    def __str__(self):
        return f"{self.rank} of {self.suit}"

two_hearts = Card("hearts", "two")

print(two_hearts)

print(two_hearts.value)


three_hearts = Card("hearts", "three")

print(two_hearts.value < three_hearts.value)