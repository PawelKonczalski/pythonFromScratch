with open('oceany.txt', 'r', encoding='UTF-8') as file:
    print(file.readline())
    print(file.tell())
    print(file.readline())
    print(file.tell())
    file.seek(0)
    print(file.tell())
    print(file.readline())
    print(file.tell())
