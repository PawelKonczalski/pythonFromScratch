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

def functionPerformance(function, arg):
    start = time.perf_counter()
    function(arg)
    end = time.perf_counter()
    return end - start

def showMessage(arg):
    print(arg)

print(functionPerformance(sumOfNumber, 500000))
print(functionPerformance(sumOfNumber2, 500000))
print(functionPerformance(sumOfNumber3, 500000))
print(functionPerformance(sumOfNumber4, 500000))
print(functionPerformance(sumOfNumber5, 500000))

