
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
        
            #You can combine else with except to be able to execute additional
            #code if there are no errors.
        
        else:
            print("Yes, Thank you!")
            break
        finally:
            print("End or try/except/finally!")
            print("I will always run at the end!")


#ask_for_int()

#### Homework

## Problem 1
def square(arr):
    try:
        for i in arr:
            print(i**2)
    except TypeError:
        print("The contents of your array are not the correct data-type for the operation.")
    except:
        print("An unknown error has occured.")
    finally:
        print("Operation complete.")

#square(['a','b','c'])

## Problem 2
def divideByZero(a=5,b=0):
    print("Starting Operation...")
    try:
        z = a/b
        print(z)
    except ZeroDivisionError:
        print("Division error: cannot divide by zero.")
    except:
        print("An unknown error has occured.")
    finally:
        print("Operation Complete.")

#divideByZero(5,2)

def ask():
    print("Beginning Operation")
    while True:
        number = input("Enter a number to square: ")  
        try:
            if number.isdigit():
                number = int(number)
            print(number**2)
            break
        except TypeError:
            print("Incorrect Data-Type Entered, Try Again.")
        except:
            print("An Unknow Error Has Occured.")
        finally:
            print("Operation Complete")

ask()