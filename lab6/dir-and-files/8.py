import os
path = input()
if os.path.exists(path):
    os.remove(path)
else:
    print("Can not delete the file as it doesn't exists")