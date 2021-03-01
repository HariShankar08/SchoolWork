import pickle


def insert():
    condition = True
    with open('file3.dat', 'wb') as file:
        while condition:
            d = {'Name': input('Enter the name: '), 'Class': int(input('Enter the class:')),
                 'Age': int(input('Enter the age: '))}

            pickle.dump(d, file)
            if input('Enter \'y\' to continue: ').strip().lower() != 'y':
                break


def display():
    with open('file3.dat', 'rb') as file:
        while True:
            try:
                d = pickle.load(file)
                print(d)
            except EOFError:
                break


def search():
    name = input('Enter the name to find: ')
    with open('file3.dat', 'rb') as file:
        while True:
            try:
                d = pickle.load(file)
                if d['Name'].strip().lower() == name.strip().lower():
                    print('Found!')
                    print(d)
                    return
            except EOFError:
                print('Did not find the name in the data.')


def update():
    with open('file3.dat', 'rb+') as file:
        try:
            while True:
                d = pickle.load(file)
                if d['Class'] == 12:
                    d['Age'] = 18
        except EOFError:
            pass


def delete():
    pass


while True:
    print('''Menu
1. Insert
2. Search
3. Delete
4. Update
5. Exit\n''')
    ch = input('Enter your choice:')

    if ch == '1':
        insert()
        display()

    elif ch == '2':
        search()

    elif ch == '3':
        delete()
        display()

    elif ch == '4':
        update()
        display()

    elif ch == '5':
        break

    else:
        print('Invalid Input')

    print()
