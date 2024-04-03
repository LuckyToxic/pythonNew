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


# Модуль 2 Часть 2
# Задание 1

day = input('Введите номер дня недели :')

if day == '1' :
    print('Ваш день недели - это понедельник!')
elif day == '2' :
    print('Ваш день недели - это вторник!')    
elif day == '3' :
    print('Ваш день недели - это среда!')    
elif day == '4' :
    print('Ваш день недели - это четверг!')    
elif day == '5' :
    print('Ваш день недели - это пятница!')    
elif day == '6' :
    print('Ваш день недели - это суббота!')    
elif day == '7' :
    print('Ваш день недели - это воскресенье!')
else:
    print('Дней в недели всего 7,введите число от 1 до 7!') 


# Задание 2

mounth = input('Введите номер месяца :')

if mounth == '1' :
    print('Ваш месяц - это январь!')
elif mounth == '2' :
    print('Ваш месяц - это февраль!')
elif mounth == '3' :
    print('Ваш месяц - это март!')
elif mounth == '4' :
    print('Ваш месяц - это апрель!')
elif mounth == '5' :
    print('Ваш месяц - это май!')
elif mounth == '6' :
    print('Ваш месяц - это июнь!')
elif mounth == '7' :
    print('Ваш месяц - это июль!')
elif mounth == '8' :
    print('Ваш месяц - это август!')
elif mounth == '9' :
    print('Ваш месяц - это сентябрь!')
elif mounth == '10' :
    print('Ваш месяц - это октябрь!')
elif mounth == '11' :
    print('Ваш месяц - это ноябрь!')
elif mounth == '12' :
    print('Ваш месяц - это декабрь!')
else:
    print('Месяцев в году всего 12.Введите число от 1 до 12!')


# Задание 3

number = int(input('Введите ваше число:'))

if number > 0 :
    print('Number is positive!')
elif number < 0 :
    print('Number is negative!')
elif number == 0 :
    print('Number is equalto zero!')
else:
    print('Нужно вести число!')           


# Задание 4

num1 = int(input('Введите ваше первое число :'))

num2 = int(input('Введите ваше второе число :'))

if num1 > num2 :
    print(num1,num2)
elif num2 > num1 :
    print(num2,num1)
elif num1 == num2 :
    print('Ваше числа',num1,'и',num2,'равны!')
else:
    print('Что-то пошло не так...')     


# Модуль 2 Часть 3
# Задание 1

number = int(input('Введите число вдиапазоне от 1 до 100 : '))

if number > 0 and number <= 100 :
    if number % 3 == 0 and number % 5 == 0 :
        print('Fizz Buzz')
    elif number % 3 == 0 :
        print('Fizz')
    elif number % 5 == 0 :
        print('Buzz')
    else: 
        print(number)
else:
    print('Ошибка!Число должно быть от 1 до 100!')   

# Задание 2


# Задание 4

man1 = int(input('Уровень продаж первого менеджера : '))

man2 = int(input('Уровень продаж второго менеджера : '))

man3 = int(input('Уровень продаж третьего менеджера : '))

salary_man1 = 200

salary_man2 = 200

salary_man3 = 200

if man1 <= 500 :
    salary_man1 += (man1*3)/100
    print('Зарпалата первого менеджера : ',salary_man1)
    if man1 > 500 and man1 <= 1000 :
        salary_man1 += (man1*5)/100
        print('Зарпалата первого менеджера : ',salary_man1)
else:    
    salary_man1 += (man1*8)/100
    print('Зарпалата первого менеджера : ',salary_man1)

if man2 <= 500 :
    salary_man2 += (man2*3)/100
    print('Зарпалата второго менеджера : ',salary_man2)
    if man2 > 500 and man2 <= 1000 :
        salary_man2 += (man2*5)/100
        print('Зарпалата второго менеджера : ',salary_man2)
else:    
    salary_man2 += (man2*8)/100
    print('Зарпалата второго менеджера : ',salary_man2)

if man3 <= 500 :
    salary_man3 += (man3*3)/100
    print('Зарпалата третьего менеджера : ',salary_man3)
    if man3 > 500 and man3 <= 1000 :
        salary_man3 += (man3*5)/100
        print('Зарпалата третьего менеджера : ',salary_man3)
else:    
    salary_man3 += (man3*8)/100
    print('Зарпалата третьего менеджера : ',salary_man3)

if man1 > man2 > man3 :
    print('По итогам первый менеджер был лучшим и получает премию 200$\n Его зарпалата будет равна :',salary_man1 + 200)
elif man2 > man3 > man1 :
    print('По итогам второй менеджер был лучшим и получает премию 200$\n Его зарпалата будет равна :',salary_man2 + 200)
elif man3 > man2 > man1 :
    print('По итогам третий менеджер был лучшим и получает премию 200$\n Его зарпалата будет равна :',salary_man3 +200)


# Модуль 3 Часть 1
# Задание 1

num1 = int(input('Введите первое число(начало диапазона) : '))

num2 = int(input('Введите второе число(конец дипазона) : '))

if num1 < num2 :
    while num1 < num2 :
        num1 += 1
        if num1 % 7 == 0 :
            print(num1)
elif num1 > num2 :
    while num2 < num1 :
        num2 += 1
        if num2 % 7 == 0 :
            print(num2)
else:
    print('Error!')        

# Задание 2




