import random

print(random.random())

x = 0
while x < 100:
    x = x + 1
    #print(random.random())
    #print(random.uniform(0, 100))

def willWeaponHit(weaponChanceToHitProcentage):
    hitChance = random.uniform(0, 100)
    if(hitChance < weaponChanceToHitProcentage):
        return 'hit'
    else:
        return 'missed'

x = 0

listHit = []

while x < 100:
    x += 1
    listHit.append(willWeaponHit(50))

from collections import Counter

dictionaryHit = Counter(listHit)

print(dictionaryHit)

x = 0

while x < 100:
    x += 1
    #print(random.randrange(10))
    print(random.randint(1, 10))
