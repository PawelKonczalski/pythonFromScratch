sum = 0

for numberOfDigits in range(4):
    number = int(input('insert number: '))
    sum += number
   

print('Sum of given numbers:', sum)

#exercise

for i in range(201):
    if( i % 5 == 0 and i % 7 != 0):
        print('value:', i, 'is divisible by 5 and not divisible by 7')
