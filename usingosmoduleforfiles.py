# Another method - reading and writing without r+
import os

file = open('doc.txt', 'r')
f2 = open('f.txt', 'w')

content = file.read()
content = content.replace('o', 'O')

f2.write(content)

file.close()
f2.close()

os.remove('doc.txt')
os.rename('f.txt', 'doc.txt')

