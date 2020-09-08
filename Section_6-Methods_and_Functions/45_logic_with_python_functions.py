'''
    Comment
'''

def even_check(num):
    return num % 2 == 0;

# print(even_check(7))
# print(even_check(8))


def check_even_list(numList):
    # return all of the even numbers in the list
    even_list = []
    for num in numList:
        if num %2 == 0:
            even_list.append(num)
        else:
            pass
    return even_list

# print(check_even_list([1,3,4,7,8]))

