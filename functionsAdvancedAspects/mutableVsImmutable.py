listSample  = [1, 4, 512, 24]

listSample2 = listSample

listSample2.append(465)

print(listSample)

print(listSample2)

print(id(listSample))

print(id(listSample2))

a = 4

b = a
print(id(b))
b = 7
print(id(b))

print()

def append_element_to_list(listka, element):
    print(id(listka))
    a = [2, 4, 20] 
    listka = a 
    print(id(listka))



print(id(listSample))
append_element_to_list(listSample, 5)
