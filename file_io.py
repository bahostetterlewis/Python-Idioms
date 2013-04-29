# reading from a file
with open('myfile.txt', 'r') as f:
    for line in f:
      print(line, end='')  # do any work here, I replicated cat!

# writing to a file
with open('myfile.txt', 'w') as f:
    f.write('some data')

# using print to write to file
with open('myfile.txt', 'w') as f:
    print('some data', file=f)

# read file with sentinal
with open('myfile.txt', 'r') as f:
    for line in iter(f.readline, 'end'):  # replace end with any sentinal to end iteration
        print(line)  # do any work here again
  
# read binary file with sentinal
# partial allows us to set a block size so that iter
# can create an iterator since it takes a function of 0 params
from functools import partial
with open('myfile', 'rb') as f:
    for block in iter(partial(f.read, 256), ''):  # replace '' with any sentinal your file is expecting
        # do work with block
