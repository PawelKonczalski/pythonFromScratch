import random

def chooseRandomNumbers(amount, totalAmount):    
    print(random.sample(range(1, totalAmount + 1), amount))

chooseRandomNumbers(6, 49)

chooseRandomNumber = set([])
while len(chooseRandomNumber) < 6:
    chooseRandomNumber.add(random.randint(1, 50))
print(chooseRandomNumber)
