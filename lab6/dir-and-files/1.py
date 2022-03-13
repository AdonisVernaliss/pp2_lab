import os

path = input("Enter the path: ")
print("\nOnly directories:")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
# print([i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))])
print("\nFiles and directories:")
for i in os.listdir(path):
    print(i)
# print([i for i in os.listdir(path)])
print("\nOnly files:")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)
# print([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))])
