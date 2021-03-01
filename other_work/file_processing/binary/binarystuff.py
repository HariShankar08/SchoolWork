import pickle


def insert(a_list):
    with open('foo.dat', 'ab') as file:
        pickle.dump(a_list, file)


def display():
    with open('foo.dat', 'rb') as file:
        try:
            while True:
                a = pickle.load(file)
                print(f'Name: {a[0]}; Roll No.:{a[2]}; Marks:{a[1]}')
        except EOFError:
            pass


while True:
    print('Menu\n'
          '1. Insert\n'
          '2. Search\n'
          '3. Delete\n'
          '4. Update\n'
          '5. Exit')
    ch = input('Enter your choice:')
    print()

    if ch == '1':
        while True:
            n = input("Enter the name: ")
            r = int(input("Enter the roll no.: "))
            m = int(input("Enter the marks: "))
            lst = [n, m, r]
            insert(lst)
            z = input("Enter 'y' to continue or 'n' to break: ").strip().lower()
            if z == 'n':
                break
        print()
        display()

    elif ch == '2':
        pass

    elif ch == '3':
        pass
    elif ch == '4':
        pass
    elif ch == '5':
        break
    else:
        print('Invalid Input')
    print()
