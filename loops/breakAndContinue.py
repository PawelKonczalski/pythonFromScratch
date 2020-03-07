'''
sum = 0

for numberOfDigits in range(3):
    number = int(input('Enter a positive number: '))
    if(number > 0):
        sum += number
    else:
        break
        print('the number was not positive')
    print('result of adding it:', sum)

'''

sum = 0
i = 0

while i < 3:
    number = int(input('Enter a positive number: '))
    if(number > 0):
        sum += number
    else:
        print('the number was not positive')
        continue
    print('result of adding it:', sum)
    i += 1
