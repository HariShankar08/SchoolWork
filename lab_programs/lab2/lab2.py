from Geometry import circle, rectangle

while True:
    print('''Menu
1. Area of Circle
2. Perimeter of Circle
3. Area of Rectangle
4. Perimeter of Rectangle
5. Exit\n''')

    ch = input('Enter your choice:')

    if ch == '1':
        r = float(input('Enter radius of the circle:'))
        area = circle.c_area(r)
        print(f'Area of circle: {area}')

    elif ch == '2':
        r = float(input('Enter radius of the circle:'))
        perimeter = circle.c_perimeter(r)
        print(f'Perimeter of circle: {perimeter}')

    elif ch == '3':
        l = float(input('Enter length:'))
        b = float(input('Enter breadth:'))
        area = rectangle.r_area(l, b)
        print(f'Area of rectangle: {area}')

    elif ch == '4':
        l = float(input('Enter length:'))
        b = float(input('Enter breadth:'))
        perimeter = rectangle.r_perimeter(l, b)
        print(f'Perimeter of rectangle: {perimeter}')

    elif ch == '5':
        break

    print()