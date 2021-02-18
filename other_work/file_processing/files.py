'''Files: Figuring out files'''

'''
# Writing to files:
file = open('foo.txt', 'w')

file.write("Welcome"+"\n"+"Hello World")
# file.write(1) || file.write() argument must be str
# file.write(['1','2','3']) || Same as above

# Consecutive writes do not separate by \n, instead just continues
# at the file pointer
file.close()
'''

'''
# Reading from files
file = open('foo.txt')

var = file.read(2)
v2 = file.read(3)
print(var)
print(v2)


# file.read() is like a generator, kinda.
# Once file.read() is executed once, there is no more data
# left to read.

for i in file.read().strip().split():
    print(i)    
'''

#Writing lists to files
file = open('foo3.txt', 'w')
file.writelines(['Hello','Wait','Bye'])
# Writelines: Still writes in the same line, unless escaped
file.close()
