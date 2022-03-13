import os

path = input()
if os.access(path, os.F_OK):
    print('Test the existence')
else:
    print('Test is not the existence')
if os.access(path, os.R_OK):
    print('Test the readable')
else:
    print('Test is not the Readable')
if os.access(path, os.W_OK):
    print('Test the writable')
else:
    print('Test is not the writable')
if os.access(path, os.X_OK):
    print('Test the executable')
else:
    print('Test is not the executable')
