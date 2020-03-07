names = {"Max", "Abigeil", "John", "Beatryce", "Alan", "Jessica"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

namesLength = {
    name: len(name)
    for name in names
}

print(namesLength)

multipliedNumbers = {
    number: number * number
    for number in numbers
}
print(multipliedNumbers)

numberToTheThirdPower = {
    number: number ** 3
    for number in numbers
}
print(numberToTheThirdPower)

temperatureInFarenchytes = {
    key: temperature * 1.8 + 32
    for key, temperature in celcius.items()
}
print(temperatureInFarenchytes)
