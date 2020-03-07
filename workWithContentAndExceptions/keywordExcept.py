namesAndSurnames = []

with open('fullnames.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        namesAndSurnames.append(tuple(line.replace('\n', '').split(' ')))
    print(namesAndSurnames)

with open('names.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        file.write(item[0] + '\n')

with open('surnames.txt', 'w', encoding='UTF-8') as file:
    for item in namesAndSurnames:
        try:
            file.write(item[1] + '\n')
        except IndexError:
            file.write('\n')
