import pickle


def insert():
    outer_lst = []
    with open('file2.dat', 'wb') as file:
        while True:
            print()
            n = input("Enter the name: ")
            r = int(input("Enter the roll no.: "))
            m = int(input("Enter the marks: "))
            outer_lst.append([n, r, m])
            print()
            z = input("Enter 'y' to continue or 'n' to break: ").strip().lower()
            if z == 'n':
                pickle.dump(outer_lst, file)
                print()
                return


def display():
    with open('file2.dat', 'rb') as file:
        while True:
            try:
                outer_lst = pickle.load(file)
            except EOFError:
                break

        for lst in outer_lst:
            print(f'Name: {lst[0]}; Roll No: {lst[1]}; Marks: {lst[2]}')


def search():
    roll_no = int(input('Enter the roll number: '))
    with open('file2.dat', 'rb') as file:
        outer_lst = pickle.load(file)
        for lst in outer_lst:
            if lst[1] == roll_no:
                print('\nFound!')
                print(f'Name: {lst[0]}; Roll No: {lst[1]}; Marks: {lst[2]}')
                return
        else:
            print('Did not find the roll number.')


def update():
    roll_no = int(input('Enter the roll number: '))
    with open('file2.dat', 'rb+') as file:
        outer_lst = pickle.load(file)
        for lst in outer_lst:
            if lst[1] == roll_no:
                idx = int(input('\nEnter 0 to modify name, 1 to modify roll no, 2 to modify marks: '))
                modified_val = input('Enter the new value:')
                try:
                    modified_val = int(modified_val)
                    if idx == 1:
                        if modified_val in [i[1] for i in outer_lst]:
                            print('Roll Number already exists. Aborting operation...')
                            return

                except ValueError:
                    pass
                lst[idx] = modified_val
        file.seek(0)
        pickle.dump(outer_lst, file)
        print()


def delete():
    roll_no = int(input('Enter the roll number: '))
    with open('file2.dat', 'rb+') as file:
        outer_lst = pickle.load(file)
        outer_lst = [inner_lst for inner_lst in outer_lst if inner_lst[1] != roll_no]
        print(outer_lst)
        file.seek(0)
        pickle.dump(outer_lst, file)
        print()


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
