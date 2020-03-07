import sys

evenNumbers = [element
               for element in range(4400)
               if (element % 2 == 0)
               ]

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                        )

print(evenNumbers)
print(evenNumbersGenerator)

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))

print(sum(evenNumbersGenerator))

for item in evenNumbersGenerator:
    print(item)

print(sys.getsizeof(evenNumbersGenerator))

