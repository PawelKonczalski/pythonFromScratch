def greet(name, message, separator=' '):
    print(message, name, sep=separator)

greet('Tom', 'Hello', '\n')

greet(message='Hello', name='Tom')
