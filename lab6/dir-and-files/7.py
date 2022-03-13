filename1 = input('Enter the name of the copy file to another file: ')
filename2 = input('Name of another file: ')

file1 = open(filename1, 'rb')
file2 = open(filename2, 'wb')

file2.write(file1.read())

file1.close()
file2.close()
print('Backup completed successfully')
# import shutil
# shutil.copyfile('anyfile.txt', 'fileany.txt')
