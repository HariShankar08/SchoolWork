with open('adoc.txt', 'w') as file:
    words = file.write('Hello, Hello. How are you?\n')


with open('adoc.txt', 'r') as file:
    words = file.read().strip().split()

cleaned_words = []
for word in words:
    word = word.strip()
    if word[-1] in r'.,?!':
        word = word[:-1]
    cleaned_words.append(word.lower())

d = dict.fromkeys(cleaned_words, 0)
for word in cleaned_words:
    d[word] += 1

with open('progoutput.txt', 'w') as foo:
    foo.write('Frequency of words\n')
    for k, v in d.items():
        foo.write(f'{k.title()}: {v}\n')
    


