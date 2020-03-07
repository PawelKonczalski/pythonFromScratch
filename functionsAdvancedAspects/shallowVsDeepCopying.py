import copy

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    print(toBeDestroyedList)
   
myList = [1, 4, 2, 1, 52, 3]

print(id(myList))
evil_function(myList[:])
