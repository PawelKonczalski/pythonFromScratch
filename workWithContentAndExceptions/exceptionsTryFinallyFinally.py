try:
    file = open('test.txt', 'w')

    print(0/0)
    file.write('sample')
finally:
    file.close()
