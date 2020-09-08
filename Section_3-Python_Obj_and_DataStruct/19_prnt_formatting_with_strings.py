
### Print Formatting with Strings

## Formatted String Literals

hobbit_first = "Bilbo"
hobbit_last = "Baggins"

## .Format() method
print("Run home {}".format(hobbit_first))
print("My name is {1} {0}".format(hobbit_last,hobbit_first))
print("My name is {o} {s}".format(o=hobbit_first, s=hobbit_last))

# .Format() floating
result = 100 / 777
print("The result was {r:1.3f}".format(r=result)) # {value:width.precision}


## f strings
print(f'Hello, my name is {hobbit_first}')
print(f'The result was {result:1.3f}')
