import random
from enum import Enum

def findApproximateValue(value):
    lowestValue = value - value * 0.1
    highestValue = value + value * 0.1
    return random.randint(lowestValue, highestValue)

Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {
                    Event.Chest: 0.6,
                    Event.Empty: 0.4
                  }
eventList = tuple(eventDictionary.keys())
eventProbability = tuple(eventDictionary.values())


Colours = Enum('Colours', {'Green': 'green',
                           'Orange': 'orange',
                           'Purple': 'purple',
                           'Gold': 'gold'
                          }
               )

chestColoursDictionary = {
                            Colours.Green :  0.75,
                            Colours.Orange : 0.2,
                            Colours.Purple : 0.04,
                            Colours.Gold : 0.01
                         }
chestColourList = tuple(chestColoursDictionary.keys())
chestColourProbability = tuple(chestColoursDictionary.values())

rewardsForChests = {
                       chestColourList[reward]: findApproximateValue((reward + 1) * (reward + 1) * 1000)
                       for reward in range(len(chestColourList))
                   }

gameLength = 5
goldAcquired = 0

print("Welcome in my game called KOMNATA")
print("""You have only 5 steps to make,
see yourself how much gold you gonna acquire till the end!""")

while gameLength > 0:
    gamerAnswer = input("Do you want to move forward?")
    if (gamerAnswer == "yes"):
        print("Great, let's see what you got...")
        drawnEvent = random.choices(eventList,eventProbability)[0]
        if (drawnEvent == Event.Chest):
            print("You've drawn a CHEST")
            drawnColour = random.choices(chestColourList,chestColourProbability)[0]
            print("The chest color is", drawnColour.value)
            gamerReward = rewardsForChests[drawnColour]
            goldAcquired = goldAcquired + gamerReward
        elif(drawnEvent == Event.Empty):
            print("You've drawn nothing, you are so unlucky!")
            
    else:
        print("You can go just straight this is beta version")
        continue
    
    gameLength = gameLength - 1

print("Congratulation, you have acquired: ", goldAcquired)
