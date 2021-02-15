#!/usr/bin python

def interest(p, n=2, r=0.09):
    return n * p * r


def total_sum(msg, *args):
    s = 0 
    for i in args:
        s += i
        
    return f'{msg} {s}'


def stu_info(msg, **kwargs):
    print(msg, end='\n\n')
    
    for kwarg in kwargs:
        print(f'{kwarg}: {kwargs[kwarg]}')
        
    print()


def sum_avg(*numbers):
    s = 0
    
    for number in numbers:
        s += number
        
    avg = s / len(numbers)

    return s, avg


if __name__ == '__main__':
    while True:
        print("Menu")
        print("1. Positional and Default Arguments")
        print("2. Keyword Arguments")
        print("3. Variable length Arguments")
        print("4. Variable length keyword Arguments")
        print("5. Multiple return values")
        print("6. Exit\n")

        ch = input("Enter your choice:")
        print()

        if ch.strip() == '1':
            principal = float(input("Enter the principal: "))
            time = int(input("Enter time: "))
            print(f'Interest calculated: {interest(principal, time)}')

        elif ch.strip() == '2':
            principal = float(input("Enter the principal: "))
            rate = float(input("Enter rate as decimal: "))
            print(f'Interest calculated: {interest(r=rate, p=principal)}')

        elif ch.strip() == '3':
            print(total_sum('The sum is', 1, 2, 3))
            print(total_sum('The sum is', 1, 2, 3, 4, 5))

        elif ch.strip() == '4':
            stu_info('Student Information', roll_no=1, name='AB', grade=12)
            stu_info('Another Student\'s Information', roll_no=1, name='AB', grade=12,
                     marks=[95, 96, 93, 91, 98], gender='M')

        elif ch.strip() == '5':
            t = sum_avg(1, 2, 3, 4, 5, 6)
            print(f'Received tuple: {t}\n\nUsing unpacking:\n')

            s, a = sum_avg(1, 2, 3, 4, 5, 6)
            print(f'Sum: {s}\nAverage: {a}')

        elif ch.strip() == '6':
            break

        print()
