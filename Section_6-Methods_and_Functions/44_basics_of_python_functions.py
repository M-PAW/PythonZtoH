
'''
    Basics of Python Function:

        use print statements to check outputs

'''

def say_hello(name = "Guy"):    # Using a default value in params
    print(f'Hello {name}')

say_hello("Dragon")



def add_num(num1,num2):
    return num1+num2

number = add_num(1,2)           # able to store the returned value
print(number)