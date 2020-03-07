print('The program calculates the area of the rectangle')

def rectangleArea(x, y):
    return x * y

x = int(input('the length of the first side: '))
y = int(input('the length of the other side: '))

area = rectangleArea(x, y)

print('the area of the rectangle is:', area)

def division(a, b):
    if(b == 0):
        return
    return a / b

z = division(10, 2)

if(z):
    print('divided correctly', z)
else:
    print('cannot be divided by 0')
