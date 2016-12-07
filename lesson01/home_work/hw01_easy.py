# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

number = int(input ('Input your number: '))
ok = 'Ok, your number is '
print (ok + str(number))

firstNumber = number // 100
secondNumber = ((number % 100) // 10)
thirdNumber = number %10

print(str(firstNumber) + " " + str(secondNumber) + " " + str(thirdNumber))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это неправильное решение!

firstNumber = int(input('Input first number: '))
secondNumber = int(input('Input second number: '))
print('First number: ' + str(firstNumber) + ' & ' + 'Second number: ' + str(secondNumber))

# firstNumber, secondNumber = secondNumber, firstNumber

print('Now... Magic!')

tempN = firstNumber
firstNumber = secondNumber
secondNumber = tempN
print('First number: ' + str(firstNumber) + ' & ' + 'Second number: ' + str(secondNumber))

# Задача-3: Запросите у пользователя год рождения. Если ему есть 18 лет, выведите: "Доступ разрешени",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

print('Hello! In what year you was born?')
userYear = int(input('Year: '))
ages = 2016 - userYear
if ages > 18 : 
	print('Access granted')
else : 
	print('Access denied')
