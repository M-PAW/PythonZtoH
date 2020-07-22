
### List in Python

my_list = [1,2,3]

types_list = ['string',100, 23.2]

my_list[1] = "two"  # changing an index value

my_list.append("four")  # add items to a list

popped_item = my_list.pop()   # remove an item from a list
index_pop = my_list.pop(0)

print("Index of my_list:", my_list[1])
print("Length of my_list:", len(my_list))  # length of list
print("My_List slice:", my_list[1:])       # Slicing a list
print("Popped item:", popped_item)
print("Index pop:", index_pop)

#-----
    ### Sorting Lists
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

new_list.sort()                 # This will not work on alpha chars
num_list.sort()                 # This will sort but only mutates, no return data
sorted_list = sorted(num_list)  # This will sort and return data

print(new_list)
print(num_list)
print(sorted_list)

