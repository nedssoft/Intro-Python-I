import os

"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"


"""
with open ensures that the file closes automatically after the r/w operation
"""
with open(os.getcwd()+'/foo.txt') as f:
    data = f.read()
    print(data)

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

with open(os.getcwd()+'/bar.txt', 'w') as f:
    content = ['This is python language, or what the fuck?', 'Hell yeah, it is the freaking python language']
    for line in content:
        f.write(line+'\n')
f.close()
# YOUR CODE HERE