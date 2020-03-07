def unlimitedNumberGenerator():
    number = 0
    while True:
        number += 1
        result = number * number
        yield result

generatedNumbers = []

numberGenerator = unlimitedNumberGenerator()

for _ in range(20):
    generatedNumbers.append(next(numberGenerator))
             
print(generatedNumbers)

for _ in range(30):
    generatedNumbers.append(next(numberGenerator))
             
print(generatedNumbers)
