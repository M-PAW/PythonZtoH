
### While Loops in Python

## While can be combined with else

x = 0
while x < 5:
    print(f'Current value of x: {x}')
    x += 1
else:
    print("While Loop Complete.")

## break, continue, pass

x = [1,2,3]

for item in x:          # pass, a place holder
    pass

mystring = "sammy"
for letter in mystring: # continue, continues through the loop
    if letter =='a':
        continue
    print(letter)

for letter in mystring: # break, breaks out of the current loop
    if letter == 'y':
        break;
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break;
    print(x)
    x += 1


