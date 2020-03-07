# len() - length
# .append(arg) - add
# .extend([tab]) - extend
# .insert(index, what) - insert
# .index(what) - index of a given item
# sort(reverse = False) - sorting in ascending order
# max(    )
# min(    )
# .count(    ) - how many times something occurs
# .pop() - delete last item
# .remove(     ) - Delete the first occurrence
# .clear() - clear list 3.3+ use list *= 0
# .reverse - reorder

names = ['Peter', 'Roxi', 'Max', 'Karma']
numbers = [1, 65, -45, 12]
x = [1, 2, 3, "Max", "John"]

print(len(names))

numbers.append(7)
print(numbers)

numbers.extend([14, -45, 5])
print(numbers)

numbers.insert(1, 99)
print(numbers)

print(names.index('Max'))

numbers.sort(reverse = True)
print(numbers)

print(max(numbers))

print(min(numbers))

print(numbers.count(-45))

numbers.pop()
numbers.pop()
print(numbers)

numbers.remove(99)
print(numbers)

x *= 0
print(x)

names.reverse()
print(names)
