import os
import pickle

print("Working on directory:")
print(os.getcwd(), '\n')

with open('b1.dat', 'wb') as file:
    pass


with open('b1.dat', 'rb') as foo:
    var = os.getcwd()
    a = var + r'/b1.dat'
    if os.path.exists(var):  # Checks whether the file exists.
        print(f"Found a file at {var}")
        if not os.path.exists(var + '/f1/'):
            os.mkdir('f1/')
        os.chdir('f1/')
        print(f"\n\nNow in {os.getcwd()}")
    else:
        assert os.path.exists(var), "Did not find the file."
