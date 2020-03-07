import math

print('1 - rectangle area')
print('2 - square area')
print('3 - triangle area')
print('4 - trapezoidal area')
print('5 - wheels area')
print('6 - exit')

def rectangleArea(a, b):
    return a * b

def squareArea(a):
    return a * a

def triangleArea(a, h):
    return a * h / 2

def trapezoidalArea(a, b, h):
    return (a + b) * h / 2

def wheelsArea(r):
    return math.pi * r ** 2

while(True):
    choice = input('what you want to do?: ')
    if(choice == '1'):
        a = int(input('the length of the first side: '))
        b = int(input('length of the other side: '))
        print('Rectangle area =', rectangleArea(a, b))
    elif(choice == '2'):
        a = int(input('side length: '))
        print('Square area =', squareArea(a))
    elif(choice == '3'):
        a = int(input('triangle base: '))
        h = int(input('triangle height: '))
        print('Triangle area =', triangleArea(a, h))
    elif(choice == '4'):
        a = int(input('shorter base length: '))
        b = int(input('length of the longer base: '))
        h = int(input('trapezoidal height: '))
        print('Triangle area =', trapezoidalArea(a, b, h))
    elif(choice == '5'):
        PI = math.pi
        r = int(input('wheel radius: '))
        print('Wheels area =', wheelsArea(r))
    elif(choice == '6'):
        print('see you next time')
        break
    else:
        print('illegal operation!!')
        
