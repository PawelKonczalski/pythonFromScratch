def double(x):
    return x *2

print(double(4))

myList = [2, 14, 22, 7, 6, 4 ,5 , 17]

myListFiltered = list(filter(lambda x: x % 2 == 0, myList))

print(myListFiltered)
