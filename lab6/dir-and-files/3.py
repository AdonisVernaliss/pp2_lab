import os

path = input('Enter the path: ')
if os.path.exists(path):
    print(' File name: ', os.path.basename(path), '\n', 'Dir name: ', os.path.dirname(path))
