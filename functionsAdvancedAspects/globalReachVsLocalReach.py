def add():
    global c
    c += 5
    print(c)

def add2(c, amount = 1):
    c +=amount
    print(c)

c = 1
add()
add2(c)

print(c)

