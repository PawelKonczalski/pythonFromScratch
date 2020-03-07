import howToImportOwnModule
import math

from enum import IntEnum

FigureFields = IntEnum('FigureFields', 'Rectangle Square Triangle Trapezoidal Wheels')

choice = int(input('''You want to calculate fild of:
1 - rectangle area
2 - square area
3 - triangle area
4 - trapezoidal area
5 - wheels area
'''))
if(choice == FigureFields.Rectangle):
    a = int(input('the length of the first side: '))
    b = int(input('length of the other side: '))
    print('Rectangle area =', howToImportOwnModule.rectangleArea(a, b))
elif(choice == FigureFields.Square):
    a = int(input('side length: '))
    print('Square area =', howToImportOwnModule.squareArea(a))
elif(choice == FigureFields.Triangle):
    a = int(input('triangle base: '))
    h = int(input('triangle height: '))
    print('Triangle area =', howToImportOwnModule.triangleArea(a, h))
elif(choice == FigureFields.Trapezoidal):
    a = int(input('shorter base length: '))
    b = int(input('length of the longer base: '))
    h = int(input('trapezoidal height: '))
    print('Triangle area =', howToImportOwnModule.trapezoidalArea(a, b, h))
elif(choice == FigureFields.Wheels):
    PI = math.pi
    r = int(input('wheel radius: '))
    print('Wheels area =', howToImportOwnModule.wheelsArea(r))
else:
    print('illegal operation!!')
