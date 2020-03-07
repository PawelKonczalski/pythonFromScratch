name: 'Alan'
age: 27
gender: 'male'

name2: 'Viki'
age2: 19
gender2: 'female'

person1 = ('Alan', 27, 'male')
person2 = ('Viki', 19, 'female')
person3 = ('John', 35, 'male')

guestList = [
                ['Alan', 27, 'male'],
                ['Viki', 19, 'female'],
                ['John', 35, 'male']
            ]

print(guestList[0])
print(guestList[0][0])
guestList[2][1] = 24
print(guestList[2])


guestList2 = [
                ('Alan', 27, 'male'),
                ('Viki', 19, 'female'),
                ('John', 35, 'male')
             ]

guestList2.append(('Paula', 31, 'female'))
print(guestList2)

guestList3 = {
                ('Alan', 27, 'male'),
                ('Viki', 19, 'female'),
                ('John', 35, 'male')
             }

guestList3.add(('Paula', 31, 'female'))
print(guestList3)
