def generateEvenNumbers():
    for element in range(400):
        if(element % 2) == 0:
            yield element

eventNumbersGenerator = (element
                         for element in range(100)
                         if(element % 2 == 0))

a = generateEvenNumbers()

def generateTenNumbers():
    x = 0
    while x < 10:
        yield x
        x += 1
        
print(list(generateTenNumbers()))
print(list(generateTenNumbers()))
print(list(generateTenNumbers()))

generateTenNumbersExpression = (x
                                for x in range(10))
print()
print(list(generateTenNumbersExpression))
print(list(generateTenNumbersExpression))
