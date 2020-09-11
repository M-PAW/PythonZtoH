'''
    I/O with basic files in python
'''

with open("Section_3/testfile.txt", mode='r') as myfile:     # Open a file using filepath
    file_read = myfile.read()                                # read mode declared 'r'
                                                             # 'a' append, 'w' write

contents = file_read.split('\n')                             # Split it into a list by new line


## If using .readline(), position needs to be
## reset using .seek(position#)

print(contents)                                              # print out the list of lines
print(file_read)                                             # print out the read-in file

myfile.close()                                               # close the file


with open('Section_3/writefile.txt', mode='w') as w:         # creat new file and write to it  
    w.write("This is a new file.")
w.close()

with open('Section_3/writefile.txt',mode='r') as w:          # open file and read, close
    file_read = w.read()
    print(file_read)
w.close()
