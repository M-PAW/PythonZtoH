
### String Properties and Methods
## Strings are immutable to index assignments

name = "Frodo"
#name[0] ='P'               # Illegal operation, and won't work

## String concatination
name2 = "P" + name[1:]

## String Methods
x = "Hello World"

## upper
print(x.upper())            # uppercase method

## split
x2 = x.split()              # breaks a string into a list
x3 = x.split('o')           # split at a specified char


print("x2", x2)
print("x3", x3)
print("x type:", type(x))
print("x2 type:", type(x2))
print("name", name)
print("name2", name2)
print(2*name)               # Multiplying a string