# # МОДУЛЬ 1
# # Задание 1

num1 = int(input('Введите ваше первое число: '))

num2 = int(input('Введите ваше второе число: '))

num3 = int(input('Введите ваше третье число: '))

print('Сумма ваших трех чисел будет равна : ',num1 + num2 + num3)

print('Произведение ваших трех чисел будет равно : ',num1 * num2 * num3)


# # Задание 2

salary = int(input('Введите вашу зарплату за месяц :'))

credit = int(input('Введите сумму месячного платежа по кредиту :'))
 
debt = int(input('Введите сумму задолженности за коммунальные услуги :'))

print('Остаток зарплаты после выплат всех выплат составит',salary - credit - debt,'рублей')


# # Задание 3

diagonal1 = int(input('Введите длину первой диагонали ромба :'))

diagonal2 = int(input('Введите длину второй диагонали ромба :'))

print('Площадь ромба равна : ',(diagonal1 * diagonal2)//2)


# # Задание 4

print('To be','or not','to be',sep='\n')


# # Задание 5

print('"Life is what happens','\twhen','\t\tyou\'re busy making other plans"','\t\t\t\t\tJohn Lennon.',sep='\n')


# МОДУЛЬ 1 ЧАСТЬ 3
# Задание 1

num1 = input('Введите ваше первое число: ')

num2 = input('Введите ваше второе число: ')

num3 = input('Введите ваше третье число: ')

print('Ваше число :',num1+num2+num3)


# Задание 2

numbers = int(input('Введите ваше четырехзначное число :'))

num1 = numbers // 1000

num2 = (numbers // 100) % 10

num3 = (numbers % 100) //10

num4 = numbers % 10

print('Результат произведения вашего числа :',num1 * num2 * num3 * num4)

# Задание 3

meters = int(input('Введите количество метров :'))

centimeters = meters * 100

decimeters = meters * 10

millimeters = meters * 1000

conv_fac = 62E-5

miles = meters * conv_fac

print('Ваше значение в сантиметрах будет:',centimeters,'\nВ дециметрах :',decimeters,'\nВ миллиметрах :',millimeters,'\nВ милях :',miles)


# Задание 4

main_trio = int(input('Введите размер основания триугольника :'))

height_trio = int(input('Введите высоту триугольника :'))

square = main_trio * (height_trio/2)

print('Площаль вашего триугольника будет равна :',square)


# Задание 5

numbers = int(input('Введите ваше четырехзначное число :'))

num1 = numbers // 1000

num2 = (numbers // 100) % 10

num3 = (numbers % 100) //10

num4 = numbers % 10

print('Ваше развернутое число будет :',str(num4)+str(num3)+str(num2)+str(num1) )

