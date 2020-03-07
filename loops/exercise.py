sum = 0
i = 0

while i < 3:
    numberEntered = int(input('enter a positive even number: '))
    if (numberEntered > 0 and numberEntered % 2 == 0):
        sum +=numberEntered
    else:
        print('you must enter a positive even number')
        continue
    i += 1
print('result of adding numbers:', sum)
        
