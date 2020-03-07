room = {49: 'Konrad Mech', 87: 'Jaroslaw Kot', 33: 'Joahim Szmit'}

print(room)
room[49] = 'Zbigniew Kwacz'
print(room)
room[50] = 'Janusz Dabek'
print(room)

room.update({39: 'Malwina Krok', 102: 'Nina Foks'})
print(room)

del(room[87])
print(room)

room.pop(50)
print(room)

room.popitem()
print(room)
