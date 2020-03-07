sum = 0

numberOfDigits = 4

while numberOfDigits > 0:
    number = int(input('insert number: '))
    sum += number
    numberOfDigits -= 1

print('Sum of given numbers:', sum)
