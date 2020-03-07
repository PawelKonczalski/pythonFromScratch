numbers = [1, 2, 3, 4, 5, 6]

'''
powersOfTwo = []
for element in numbers:
    powersOfTwo.append(element**2)
'''

powersOfTwo =[
              element**2
              for element in numbers
             ]

'''
evenNumbers = []
for element in numbers:
    if(element % 2 == 0):
        evenNumbers.append(element)
'''
evenNumbers = [
               element
               for element in numbers
               if(element % 2 ==0)
              ]
