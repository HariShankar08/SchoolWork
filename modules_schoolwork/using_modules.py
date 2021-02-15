from my_module import welcome


def welcome():  # Overrides the welcome() from my_module
    print('welcome')


print(f'In {__name__}\n')

welcome()


