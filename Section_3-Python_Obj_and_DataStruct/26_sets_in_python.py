
''' Sets in Python
     Will not allow duplicates, only unique values
     Unorderd collection of unique elements
'''

myset = set()
mylist = [1,1,1,2,2,3,3,3,3,4]

myset.add(1)                        # adding 1 to the set
myset.add(2)                        # adding 2 to the set
myset.add(2)                        # cannot add a duplicate 2

print("myset:", myset)              # print the set
print("set(mylist):", set(mylist))  # print the list converted to set

