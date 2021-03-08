import csv
import os


def insert():
    with open('csv_file.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Roll No.', 'Name', 'Marks'])
        while True:
            lst = [int(input("Enter roll no: ")),
                   input("Enter name: "),
                   int(input("Enter marks: "))]
            writer.writerow(lst)
            print()
            if input("Do you want to continue [Y/n]:").lower().strip() == 'n':
                return


def display():
    with open('csv_file.csv', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search():
    roll_no = int(input("Enter roll number: "))
    with open('csv_file.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the column headers
        for row in reader:
            if int(row[0]) == roll_no:
                print(row)
                return
        else:
            print(f"Did not find roll number {roll_no} in the data.")


def update():
    with open('csv_file.csv', 'r', newline='') as file, \
            open('temp.csv', 'w', newline='') as temp:
        reader = csv.reader(file)
        writer = csv.writer(temp)

        col_heads = next(reader)
        writer.writerow(col_heads)

        rows = [row for row in reader]
        for row in rows:
            print(row, '\n')
            ch_ = input("Enter [1] to update roll number, [2] to update name, [3] to update marks:\n"
                        "Enter nothing to skip:")
            try:
                if ch_:
                    if ch_.strip() == '1':
                        roll = int(input("Enter new roll number:"))
                        if roll in [r[0] for r in rows]:
                            print("The Roll Number already exists. Aborting.")
                            raise ValueError("Custom Error")
                        row[0] = roll

                    elif ch_.strip() == '2':
                        name = input("Enter name:")
                        row[1] = name

                    elif ch_.strip() == '3':
                        marks = int(input("Enter marks:"))
                        row[2] = marks

                    else:
                        print("Invalid Input. Aborting operation.")
                        raise ValueError("Custom Error")

                writer.writerow(row)

            except ValueError as ve:
                if str(ve) != "Custom Error":
                    print("Bad Input. Aborting.")

                del temp, writer
                os.remove('temp.csv')
                return

    os.remove('csv_file.csv')
    os.rename('temp.csv', 'csv_file.csv')
    print()


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
