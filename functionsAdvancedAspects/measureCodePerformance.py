import time

print('The program calculates the sum of numbers to the given value.')

def sumOfNumber(number):
    sum = 0
    for value in range(1, number+1):
        sum += value
    return sum

def sumOfNumber2(number):
    return sum ([number for number in range(1, number+1)])

def sumOfNumber3(number):
    return sum ({number for number in range(1, number+1)})

def sumOfNumber4(number):
    return sum ((number for number in range(1, number+1)))

def sumOfNumber5(number):
    return (1 + number) / 2 * number

num = int(input('your number: '))

start = time.perf_counter()
print('sum of number from 1 to your number is: ', sumOfNumber(num))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print('sum of number from 1 to your number is: ', sumOfNumber2(num))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print('sum of number from 1 to your number is: ', sumOfNumber3(num))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print('sum of number from 1 to your number is: ', sumOfNumber4(num))
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
print('sum of number from 1 to your number is: ', sumOfNumber5(num))
end = time.perf_counter()
print(end - start)

