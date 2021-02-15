from math import pi

"""Circle module for Lab2 Program

Various functions regarding circles (Area and Perimeter)"""


def c_area(r):
    """Function for calculating Area of Circle

    Value is calculated and rounded to 2 decimal places."""
    return round(pi * r * r, 2)


def c_perimeter(r):
    """Function for calculating Perimeter of Circle

    Value is calculated and rounded to 2 decimal places."""
    return round(2 * pi * r, 2)
