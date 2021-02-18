#!/usr/bin python

'''
file = open('doc.txt', 'w')

file.writelines(["Hello\n", "How do you do?\n"])

file.close()
'''

'''
f = open('doc.txt')

print(f.read())
'''

'''
# Append mode for files

## Using with as a substitute for file = open() ... file.close()
## Use with, over the old method
with open('doc.txt', 'a') as file:
    file.write("...Ok then.\n")
'''

'''
# Reading AND writing
with open('doc.txt', 'w+') as file:
    file.writelines(["Hello\n", "How do you do?\n"])
    file.seek(0)  # seek() method: force shift of file pointer
    print(file.read())

# file.seek(0, x) -> x bytes from beginning of file
# file.seek(1, x) -> x bytes from current pointer location
# file.seek(2, x) -> x bytes from end of file (backwards)
'''

'''
with open('doc.txt', 'r') as file:
    content = file.read()  # This is not a with-scope variable,
                           # but is accessible by the rest of the program
    content = content.replace('o', 'O')

with open('doc.txt', 'w') as file:
    file.write(content)
'''

# The above code is equivalent to:
with open('doc.txt', 'r+') as file:
    content = file.read()
    content = content.replace('o', 'O')
    file.seek(0)  # This is absolutely necessary!!!
                  # File pointer is at EOF,
                  # so writing will write from EOF, effectively appending to the file.
    file.write(content)
# In this program, w+ instead of r+ will first try to write,
# If file.write() is not executed before file.read(), the file is made blank,
# So, basically wrecking the whole program.
