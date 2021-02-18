"""This module opens a document.txt and will write lines to the document.
Utilizes the writelines() method of files."""

'''
file = open('document.txt', 'w')

lines_lst = []

while True:
    line = input('Enter a line, or type "q" to exit and write the lines:\n')
    if line.strip().lower() == 'q':
        break
    line += '\n'
    lines_lst.append(line)

print('You have exited. Writing the lines now...')
file.writelines(lines_lst)
file.close()
'''

'''
# Option 1 - Read
file = open('document.txt')
print(file.read())
file.close()
'''
'''
# Option 2 - Read
file = open('document.txt')
for i in file:
    print(i)
file.close()
'''
'''
# Option 3 - Read line
file = open('document.txt')
print(file.readline(10))  # Takes an optional argument limit, an integer
file.close()
'''

'''
# Reading full document using readline()
file = open('document.txt')
var = file.readline()
while var:
    if var[0].lower() == 'f':
        print(var)
    var = file.readline()

file.close()
'''

# Option 4 - readlines()
file = open('document.txt')
"""
lines = file.readlines()  # Returns lines as a list
for line in lines:
    print(line)"""
lines = file.readlines()
for line in lines:
    if line.strip()[-2:] == 'ow':
        print(line)
file.close()
