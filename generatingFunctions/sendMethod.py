def unlimitedNumberGenerator():
    number = 0
    while True:
        number = yield number * number

generatedNumbers = []

numberGenerator = unlimitedNumberGenerator()
numberGenerator.send(None)

for i in range(10, 21):
    generatedNumbers.append(numberGenerator.send(i))
             
print(generatedNumbers)


for i in range(30, 50):
    generatedNumbers.append(numberGenerator.send(i))
             
print(generatedNumbers)

