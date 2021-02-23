
def add(n1,n2):
    # May have an error,
    # This is what to try
    try:
        result = n1 + n2

    # Skips the error and continues to execute code.
    # Also, output a notification of error.
    # There are many types that can be used,
    # ex: except TypeError:
    except TypeError:
        print("Incorrect Data-Type")
    
    else:
        print("Add went well!")
        print(result)


#add(10,20)


# Causing an error below for error handling

number1 = 10
#number2 = input("Please provide a number: ")

#add(number1,number2)


def readNdWrite():
    try:
        f = open('testfile.txt','r')
        f.write("Write a test line")
    except TypeError:
        print("There is was a type error!")
    except OSError:
        print("Hey, you have an OS Error!")
    except:
        print("All other exceptions!")
    finally:
        print("I always run!")



def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! Thas is not a number")
        '''
            You can combine else with except to be able to execute additional
            code if there are no errors.
        '''
        else:
            print("Yes, Thank you!")
            break
        finally:
            print("End or try/except/finally!")
            print("I will always run at the end!")


ask_for_int()