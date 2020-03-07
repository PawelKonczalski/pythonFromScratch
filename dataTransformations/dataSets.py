names = {"Max", "abigeil", "John", "beatryce", "alan", "Jessica"}


names = {
        name.capitalize()
        for name in names
        if name[0].capitalize() != 'B'
}

print(names)
