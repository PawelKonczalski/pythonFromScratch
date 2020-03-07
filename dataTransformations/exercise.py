print('Numbers from 2 to 470 divisible by 7 but not divisible by 5')

numbers = (
    number
    for number in range(2, 471)
    if number % 7 == 0
    if number % 5 != 0
    )

for number in numbers:
    print(number)
