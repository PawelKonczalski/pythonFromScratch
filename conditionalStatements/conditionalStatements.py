import math
mathematicalOperation = int(input('1 - add, 2 - odd, 3 - multiplication, '
				  '4 - division, 5 - the absolute value, '
				  '6 - exponentiation: '))

if(mathematicalOperation == 5):
	z = int(input('enter value: '))
	print('The absolute value is:', abs(z))
elif(mathematicalOperation > 6):
	print('Unforeseen mathematical operation')
else:
	x = int(input('value of x: '))
	y = int(input('value of y: '))

	if(mathematicalOperation == 1):
		print('Addition result:', x + y)
	elif(mathematicalOperation == 2):
		print('Subtraction result:', x - y)
	elif(mathematicalOperation == 3):
		if(x == 0 or y == 0):
			print('Cannot be multiplied by zero!')
		else:
			print('Multiplication result:', x * y)
	elif(mathematicalOperation == 4):
		if(y == 0):
			print('Cannot be divided by zero!')
		else:
			print('Division result:', x / y)
	elif(mathematicalOperation == 6):
		print('Exponentiation result:', x ** y)
		
