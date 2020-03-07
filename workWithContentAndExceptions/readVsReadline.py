with open('oceany.txt', 'r', encoding='UTF-8') as file:
    #oceany = file.read().splitlines()
    #oceany2 = file.readline()
    #oceany3 = file.readlines()
    for line in file:
        print(line)
