import pickle


def insert(filename='file.dat'):
    with open(filename, 'wb') as pkl_file:  # 'wb' for Writing, Binary Mode.
        c = True
        while c:
            roll_no = int(input("Roll Number:"))
            name = input("Name:")
            marks = int(input("Marks:"))

            lst = [roll_no, name, marks]
            pickle.dump(lst, pkl_file)
            c = input("Type 'y' to continue: ").strip().lower() == 'y'
    return


if __name__ == '__main__':
    insert()
