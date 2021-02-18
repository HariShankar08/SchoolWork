#!usr/bin python
'''
# Part1 - Writing
print("Part 1-Writing\n\n")
file = open('foo2.txt', 'w')
while True:
    line = input('Enter any sentence, or exit using "q":\n')
    if line.strip().lower() == 'q':
        break
    file.write(line+'\n')
    file.flush()
    print()

file.close()

# Part2 - Reading
print("Part 2-Reading\n\n")
file = open('foo2.txt')
for word in file.read().strip().split():
    if len(word) == 3:
        print(word)

file.close()
'''

#Part2.2 - Reading Vowels
file = open('foo2.txt')
counter = 0
for letter in file.read():
    if letter.lower() in 'aeiou':
        counter += 1

file.close()
print(f'Found {counter} vowels.')
