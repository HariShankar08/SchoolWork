import mysql.connector as msq
from tabulate import tabulate

user = 'root'
passwd = 'deens'

connection = msq.connect(host='localhost', user=user, passwd=passwd,
                         database='grade12')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS emp (
e_no INT,
e_name CHAR(25),
dept CHAR(25),
gender CHAR(1))''')

connection.commit()
'''
want_to_insert = input('Do you want to insert values [Y/n]: ').strip().lower() == 'y'
while want_to_insert:
    e_no = int(input("Enter the number: "))
    e_name = input("Enter the name:")
    dept = input("Enter the department:")
    gender = input('Enter gender (M/F): ').strip().upper()

    cmd = f"INSERT INTO emp VALUES ({e_no}, '{e_name}', \
'{dept}', '{gender}')"

    cursor.execute(cmd)
    connection.commit()

    print()
    if input("Do you want to enter one more row? [Y/n]: ").strip().lower() == 'n':
        break

print()
table_name = input("Enter the table name to select: ")
cursor.execute('SELECT * FROM {}'.format(table_name.strip()))
for row in cursor:
    print(row)

print()

print('Searching employee number 2')
cursor.execute(f'SELECT * FROM emp WHERE e_no = 2')
for row in cursor:
    print(row)

print()

emp_no = int(input("Enter the employee number to search: "))
cursor.execute(f'SELECT * FROM emp WHERE e_no = {emp_no}')
for row in cursor:
    print(row)    

print()

print("Ordering by user input;")
column = input('Enter the column name to order:')
order_method = input('How to order (ASC/ DESC): ').strip().lower()

cursor.execute(f'SELECT * FROM emp ORDER BY {column} {order_method}')
for row in cursor:
    print(row)
print()


print('Grouping;')
m_or_f = input("Enter the gender to group by [M/F]: ").strip().upper()
cmd = f"SELECT COUNT(*), gender FROM emp GROUP BY gender HAVING gender='{m_or_f}'"
cursor.execute(cmd)

for row in cursor:
    print(row)


print()
cursor.execute('SELECT * FROM emp WHERE dept=\'Z\' AND gender=\'M\'')
for row in cursor:
    print(row)


print()
dept = input("Enter the department: ").strip().upper()
gender = input("Enter the gender [M/F]: ").strip().upper()
cursor.execute(f'SELECT * FROM emp WHERE dept=\'{dept}\' AND gender=\'{gender}\'')
for row in cursor:
    print(row)
'''

cursor.execute('SELECT * FROM emp')
cursor.fetchall()

print(f'Fetched {cursor.rowcount} values')
connection.close()
