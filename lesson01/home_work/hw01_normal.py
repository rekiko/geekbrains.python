# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа

number = int(input ('Input your number: '))
ok = 'Ok, your number is '
print (ok + str(number))

firstNumber = number // 100
secondNumber = ((number % 100) // 10)
thirdNumber = number % 10

if firstNumber > secondNumber :
	if firstNumber > thirdNumber :
		print('The biggest number is' + ' ' + str(firstNumber))
	else :
		print('The biggest number is' + ' ' + str(thirdNumber))
else:
	if secondNumber > thirdNumber : 
		print('The biggest number is' + ' ' + str(secondNumber))
	else : 
		print('The biggest number is' + ' ' + str(thirdNumber))


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

firstNumber = int(input('Input first number: '))
secondNumber = int(input('Input second number: '))
print('First number: ' + str(firstNumber) + ' & ' + 'Second number: ' + str(secondNumber))
firstNumber, secondNumber = secondNumber, firstNumber
print('Now... Magic!')
print('First number: ' + str(firstNumber) + ' & ' + 'Second number: ' + str(secondNumber))

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
print('Let`s find "x" from ax^2 + bx + c = 0')

a = int(input('Input number for "a": '))
b = int(input('Input number for "b": '))
c = int(input('Input number for "c": '))

discr = b**2 - 4*a*c

if discr == 0:
	x = (-1*b)/(2*a)
	print(x)
else:
	if discr > 0:
		x1 = (-1 * b + math.sqrt(discr))/(2*a)
		x2 = (-1 * b - math.sqrt(discr))/(2*a)
		print(str(x1) + ' ' + str(x2))
	else:
		print('Discriminant < 0 => we hasn`t root')