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

num1 = int(input('Введите первое число(начало диапазона) : '))

num2 = int(input('Введите второе число(конец дипазона) : '))


for c in range(num1,(num2+1),+1) :
    print(c,end=' ')
print('')
for c in range(num2,(num1-1),-1) :
    print(c ,end=' ')
print('')        
for c in range(num1,(num2+1),+1) :
    if c % 7 == 0 :
        print(c,end=' ')
print('') 
count = 0
for c in range(num1,(num2+1),+1) :
    if c % 5 == 0 :
        count += 1
print(count)        


# Задание 3

num1 = int(input('Введите первое число(начало диапазона) : '))

num2 = int(input('Введите второе число(конец дипазона) : '))

for i in range(num1,(num2+1),+1) :
    if i % 3 == 0 and i % 5 == 0 :
        print('Fizz Buzz')
    elif i % 3 == 0 :
        print('Fizz')
    elif i % 5 == 0 :
        print('Buzz')
    else:
        print(i)            

# Модуль 3 Часть 2
# Задание 1

num1 = int(input('Введите первое число(начало диапазона) : '))

num2 = int(input('Введите второе число(конец дипазона) : '))

even = 0

not_even = 0

multiples9 = 0

for i in range(num1,(num2+1),+1):
    if i % 2 == 0 :
        even += 1
    if i % 9 == 0 :
        multiples9 += 1
    if i % 2 != 0 :
        not_even += 1
print(even)
print(not_even)
print(multiples9)
print((even + not_even + multiples9)//3)               


# Задание 2

long = int(input('Введите длину линии :'))

symbol = input('Введите символ :')

count = 0

while count < long :
    count += 1
    print(symbol)


# Задание 3

while True:
    num = int(input('Введите ваше число : '))
    if num > 0 and num != 7 :
        print('Number is positive!')
    elif num < 0 :
        print('Number is negative!')
    elif num == 0 :
        print('Number is equeal to zero!')
    elif num == 7 :
        print('Good bye!')
        break            

# Модуль 3 Часть 3
# Задание 1

while True :
    x = int(input('Введите первое целое число : '))
    y = int(input('Введите второе целое число : '))
    degree = x**y
    print('Ваше число ',x,'в степени ',y,',будет равно : ',degree)


# Задание 2

count = 0 
for i in range(100, 1000,+1): 
    num = str(i) 
    if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]: 
        count += 1 
print('Количество чисел у которых есть две одинаковых цыифры равна : ',count)

# Задание 3

count = 0 
for i in range(100, 1000,+1): 
    num = str(i) 
    if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]: 
        count += 1 
for j in range(1000,10000,+1):
    num1 = str(j)
    if num1[0] != num1[1] and num1[0] != num1[2] and num1[1] != num1[2] and num1[0] != num1[3] and num1[1] != num1[3] and num1[2] != num1[3]:
        count += 1   
print('Количество чисел у которых разные все цыифры равна : ',count)

# Модуль 4 Часть 1 
# Задание 1

x = input('Введите вашу строку :')

y = ''.join(reversed(x))

for i in x :
    x = str(i)
for j in y:
    y = str(j)
if x == y :
    print('Палиндром')
else :
    print('Не палиндром!')   

# Задание 2

text = input('Введите ваш текст :')

word1 = input('Введите зарезервированное слово : ')
word2 = input('Введите зарезервированное слово : ')
word3 = input('Введите зарезервированное слово : ')

text = text.replace(word1,word1.upper())
text = text.replace(word2,word2.upper())
text = text.replace(word3,word3.upper())

# Задание 3 

text = input('Введите ваш текст : ')

count = 0

text = list(text)

for i in text:
    if i == '.' or i == '!' or i == '?' :
        count += 1

print('Колчисетво предложений в вашем тексте : ',count)       
        
# МОДУЛЬ 4 ЧАСТЬ 2
# Задание 1

import re

expression = input('Введите ваше выражение : ')

numbers = re.split('[+]|[-]|[*]|[/]',expression)

print(numbers)

for i in expression :
    if i == '+' :
        expression = int(numbers[0]) + int(numbers[1])
    elif i == '-' :
        expression = int(numbers[0]) - int(numbers[1])
    elif i == '*' :
        expression = int(numbers[0]) * int(numbers[1])
    elif i == '/' :
        expression = int(numbers[0]) // int(numbers[1])

print(expression)

# Задание 2

list4 = [ random.randrange(-10,10) for i in range(10)]

print(list4)

min_num = min(list4)

max_num = max(list4)

negative_num = 0

positive_num = 0

null = 0

for i in list4 :
    if i > 0 :
        positive_num += 1
    elif i < 0 :
        negative_num += 1
    else :
        null = 0

print('Минимальное число : ',min_num,'\nМаксимальное число : ',max_num)
print('Отрицательных елементов :',negative_num,'\nПоложительных элементов : ',positive_num,'\nНулей : ',null)

# МОДУЛЬ 4 ЧАСТЬ 3
# Задение 1

list1 = [ random.randrange(0,15) for i in range(5) ]

list2 = [ random.randrange(0,15) for i in range(5) ]
# Сформировать третий список, содержащий элементы обоих списков;
list3 = list1 + list2

print(list1)
print(list2)
print(list3)
# Сформировать третий список, содержащий элементы обоих списков без повторений;
for i in list3 :
    if list3.count(i) >= 2 :
        list3.remove(i)
print(list3)
#Сформировать третий список, содержащий элементы общие для двух списков; 
list3 = []

for i in list1 :
    if i in list2 :
        list3.append(i)

print(list3)
#Сформировать третий список, содержащий только уникальные элементы каждого из
list3 = []

for i in list1 :
    if list1.count(i) == 1 :
        list3.append(i)
for j in list2 :
    if list2.count(j) == 1 :
        list3.append(j)

print(list3)
#Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
list3 = [max(list1),min(list1),max(list2),min(list2)]
 
print(list3)

# МОДУЛЬ 5 ЧАСТЬ 1
#Задание 1 

def showText():
    print('"Don`t compare yourself with anyone in this world...\nif you do so you are insilting yourself."\n\t\t\t\tBill Gates')

showText()

# Задание 2

def evenNum(a,b):
    for i in range(a,b):
        if i % 2 == 0:
            print(i)

# Задание 3

def square(long,symbol,bool=False):
    if bool == False :
        arr = []
        for i in range(long) :
            arr.append(symbol)
        print(' '.join(arr))
        for i in range(long-2):
            print(symbol.ljust(long) + symbol.rjust(long-1))
        print(' '.join(arr))
    elif bool == True :
        arr = []
        for i in range(long) :
            arr.append(symbol)
        print(' '.join(arr))
        for i in range(long-2):
            print(symbol.ljust(long,symbol) + symbol.rjust(long-1,symbol))
        print(' '.join(arr))
         
       
square(10,'@',True)

# Задание 4

def minNumb(*args):
    print(min(args))

# Задание 5

def composition(a,b):
    if a < b :
        result = 1
        arr = [i for i in range(a,b+1)]
        for i in arr:
            result = result * i
        return print(result)
    elif a > b :
        result = 1
        arr = [ i for i in range(b,a+1)]
        for i in arr :
            result = result * i
        return print(result)  

# Задание 6

def countNumb(num):
    arr = str(num)
    arr = list(arr)
    return print(len(arr))

countNumb(12345678)

# Задание 7

def isPalindrome(num):
    num = list(str(num))
    num1 = []
    num2 = []
    for i in num[:3]:
        num1.append(i)    
    for i in num[3:]:
        num2.append(i)
    num1 = ''.join(num1)
    num2 = ''.join(reversed(num2)) 
    num1 = int(num1)
    num2 = int(num2)
    if num1 == num2 :
        print(True) 
    else :
        print(False)       

# МОДУЛЬ 7 ЧАСТЬ 1
# Задание 1

myList = [999999.5,8, 10, 6, 2, 4,12,54,23,5,123,35,4,631265,45643,21,35,6] 

l = len(myList)

k = l//3

center = sum(myList)//l

if center > 0 :
    myList = sorted(myList[:k*2]) + reversed(myList[k*2:])


