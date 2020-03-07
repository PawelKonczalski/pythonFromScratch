searchedNumber = 40
givenNumber = -1

print('guess the number')
while (searchedNumber != givenNumber):
    givenNumber = int(input('enter any positive number: '))
    if(givenNumber > searchedNumber):
        print('the number provided is too big')
    elif(givenNumber < searchedNumber):
        print('the number provided is too small')
    else:
        print('congratulations you guessed it!!')
