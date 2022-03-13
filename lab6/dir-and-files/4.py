file = input('Name of the file: ')


def filen(file):
    c = 0
    with open(file) as f:
        for i in f:
            c += 1
    print("The number of lines in the text file: ", c)


filen(file)
