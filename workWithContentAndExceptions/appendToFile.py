with open('oceany.txt', 'a', encoding='UTF-8') as file:
    print(file.tell())
    file.write('\nKolejny ocean')
