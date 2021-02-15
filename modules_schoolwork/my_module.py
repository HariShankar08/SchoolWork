"""This is my module.

Pretty pointless tbh, has only one function, welcome()
Don't judge me this was a primer on using help()"""


def welcome(person='Person'):
    """The welcome() function

    Takes an argument person, or defaults person to "Person", prints __name__
    and welcomes the person.

    Now scram."""
    print(f'In {__name__}')
    print(f'Welcome, {person}')


if __name__ == '__main__':
    welcome()
