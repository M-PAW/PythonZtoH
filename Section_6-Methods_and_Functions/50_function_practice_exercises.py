


# def lesser_of_two_evens(a,b):
#     if (a+b)%2==0 and a < b:
#             return a
#     return b

# print(lesser_of_two_evens(2,4)) # 2
# print(lesser_of_two_evens(2,5)) # 5

# def animal_crackers(text):
    #  wordArray = text.lower().split(' ')

    #  return wordArray[0][0] == wordArray[1][0]

# # Check
# print(animal_crackers('Levelheaded Llama'))

# # Check
# print(animal_crackers('Crazy Kangaroo'))

# def makes_twenty(n1,n2):
#     return (n1+n2) == 20 or n1 == 20 or n2 == 20

# print(makes_twenty(20,10))
# print(makes_twenty(12,8))
# print(makes_twenty(2,3))

# def old_mcdonald(name):
#     return name[:2].capitalize() + name[2:].capitalize()

# print(old_mcdonald('mcdonald'))

#def master_yoda(text):
    #wordList = text.split(' ')
    # reverseString = ''
    # for word in wordList:
    #     reverseString = word + " " + reverseString
    # print(reverseString)

#     revese_word_list = wordList[::-1]
#     print(' '.join(revese_word_list))

# master_yoda('I am home')
# master_yoda('We are ready')


########  Definitely Something Wrong With This, Instructors Solution ABS
#def almost_there(n):
#    return (abs(100-n) <= 10) or (abs(200-n) <= n)

# Check
#print(almost_there(90))
# Check
#print(almost_there(104))
# Check
#print(almost_there(150))
# Check
#print(almost_there(209))

# def has_33(nums):
#     idx = 1
#     for num in nums:
#         if idx+1 > len(nums):
#             return False
#         if num == nums[idx]:
#             return True
#         idx += 1

# for i in range(0,len(nums)-1):
#     if nums[i:i+2] == [3,3]:
#         return True
# return False

# print(has_33([1,3,3]))
# print(has_33([1,3,1,3]))
# print(has_33([3,1,3]))

#def blackjack(a,b,c):
#     if a > 10: a=1
#     if b > 10: b=1
#     if c > 10: c=1
#     if sum([a,b,c]) > 21:
#         print('BUST') 
#     else: print(sum([a,b,c]))

#    if sum([a,b,c]) <= 21:
#        print(sum([a,b,c]))
#    elif 11 in [a,b,c] and sum([a,b,c])-10 <= 21:
#        print(sum([a,b,c])-10)
#    else:
#        print('BUST')

# # Check
#blackjack(5,6,7)

# # Check
#blackjack(9,9,9)

# # Check
#blackjack(9,9,11)

def spy_game(nums):
#     watch_dog = 0
#     agent_card = [0,0,7]
#     for num in nums:
#         if num == agent_card[watch_dog]:
#             watch_dog += 1

#         if watch_dog == len(agent_card):
#             return True
#     return False

    code = [0,0,7,'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))