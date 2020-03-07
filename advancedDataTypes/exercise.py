definitions = {}

print('1: Add definition')
print('2: Find definition')
print('3: Delete definition')
print('4: End program')

while(True):
    choice = input('What you want to do? :')
    if(choice == '1'):
        key = input('Enter the word: ')
        definition = input('Provide a word definition: ')
        definitions[key] = definition
    elif(choice == '2'):
        key = input('Enter the word: ')
        if key in definitions:
            print(key, '-', definitions[key])
        else:
            print('The definition does not exist in the dictionary')  
    elif(choice == '3'):
        key = input('Enter the word: ')
        if key in definitions:
            definitions.pop(key)
        else:
            print('The definition does not exist in the dictionary')  
    elif(choice == '4'):
        print('Program closed')
        break
    else:
        print('Undefined operation')
