import pickle
import os


def insert():
    with open('file.dat', 'wb') as file:
        while True:
            print()
            n = input("Enter the name: ")
            r = int(input("Enter the roll no.: "))
            m = int(input("Enter the marks: "))
            lst = [n, m, r]
            pickle.dump(lst, file)
            z = input("Enter 'y' to continue or 'n' to break: ").strip().lower()
            if z == 'n':
                break


def display():
    with open('file.dat', 'rb') as file:
        try:
            while True:
                a = pickle.load(file)
                print(f'Name: {a[0]}; Roll No.:{a[2]}; Marks:{a[1]}')
                print()
        except EOFError:
            pass


def search():
    roll_no = int(input("Enter the roll number:"))
    print()
    try:
        with open('file.dat', 'rb') as f:
            while True:
                lst = pickle.load(f)
                if roll_no in lst:
                    print('Found!')
                    print(f'Name: {lst[0]}; Roll No.:{lst[2]}; Marks:{lst[1]}')
                    return
    except EOFError:
        print('Did not find the roll number in the data.')


def update():
    try:
        with open('file.dat', 'rb') as file, open('temp.dat', 'wb') as temp:
            while True:
                x = pickle.load(file)
                if x[1] <= 35:
                    x[1] += 5
                pickle.dump(x, temp)
    except EOFError:
        os.remove('file.dat')
        os.rename('temp.dat', 'file.dat')


def delete(roll_no):
    flag = False
    try:
        with open('file.dat', 'rb') as file, open('temp.dat', 'wb') as temp:
            while True:
                x = pickle.load(file)
                if x[2] != roll_no:
                    pickle.dump(x, temp)
                    flag = True
    except EOFError:
        if flag:
            os.remove('file.dat')
            os.rename('temp.dat', 'file.dat')
            print('Deleted the record')
        else:
            print('The Roll Number was not found.')


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
        print('Old records:')
        display()
        rn = int(input('Enter the roll number to delete:'))
        print('\nNow attempting to delete:')
        delete(roll_no=rn)
        print('Records after delete operation:')
        display()

    elif ch == '4':
        print('Old records:')
        display()
        print('\nNow updating:')
        update()
        display()

    elif ch == '5':
        break

    else:
        print('Invalid Input')

    print()
