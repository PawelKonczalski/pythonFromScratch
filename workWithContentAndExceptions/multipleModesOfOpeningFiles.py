with open('oceannny.txt', 'a+', encoding='UTF-8') as file:
    file.write('lets see the result')
    file.seek(0)
    print(file.readline())
    print(file.tell())
    file.write('next test measage')
