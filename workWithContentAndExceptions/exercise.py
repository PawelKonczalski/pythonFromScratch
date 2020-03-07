def readContentOfFile(path):
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return print(file.read())
    except FileNotFoundError:
        print('Fille not exist')

nameOfFile = input('Enter the file name to open: ')
readContentOfFile(nameOfFile)
