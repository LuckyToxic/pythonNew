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


# МОДУЛЬ 2 ЧАСТЬ 1
# Задание 1

numb1 = int(input('Введите первое число :'))

numb2 = int(input('Введите второе число :'))

numb3 = int(input('Введите третье число :'))

choice = input('Вывести на экран сумму введите "1"\nВывести произведение на экран введите "2"\nВаш выбор :')

if choice == 1 :
    print('Сумма ваших чисел :',numb1+numb2+numb3)
else :
    print('Произведение ваших чисел :',numb1*numb2*numb3) 


# Задание 2

numb1 = int(input('Введите первое число :'))

numb2 = int(input('Введите второе число :'))

numb3 = int(input('Введите третье число :'))

choice = input('Для вывода наибольшего числа введите "a"\nДля вывода наименьшего числа введите "b"\nДля отображения среднеарефметического числа введите "с"\nВведите ваш вариант :')

if choice == 'a' :
    if numb1<numb2<numb3 :
        print('Наименьшее число из трех :',numb1)
    elif numb2<numb3<numb1 :
        print('Наименьшее число из трех :',numb2)
    else :    
        print('Наименьшее число из трех :',numb3)
elif choice == 'b' :
    if numb1>numb2>numb3 :
        print('Наибольшее число из ваших трех :',numb1)
    elif numb2>numb3>numb1 :
        print('Наибольшее число из ваших трех :',numb2)
    else :    
        print('Наибольшее число из ваших трех :',numb3)
elif choice == 'c' :
    print('Среднее арифметическое ваших трех чисел равно :',(numb1+numb2+numb3)//3)      


# Задание 3

meters = int(input('Введите ваше количество метров :'))

print('В какую еденицу преобразовать : мили, дюймы или ярды?')

choice = input('Введите ваш выбор словом :')

if choice == 'мили' :
    print('Количество заданых метров в милях будет равна', meters *(62E-5))
elif choice == 'дюймы' :
    print('Количество заданых метров в дюймах будет равна :', meters * 39.3701)
elif choice == 'ярды' :
    print('Количество заданых метров в ярдах будет равна :', meters * (109361E-5))        
