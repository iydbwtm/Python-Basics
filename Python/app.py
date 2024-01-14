#print('Задание: Посчитайте сумму трех введенных целых чисел')
#number1 = int(input('Введите одно число: '))
#number2 = int(input('Введите одно число: '))
#number3 = int(input('Введите одно число: '))
#print(number1, '+', number2, '+', number3, '=', number1 + number2 + number3)
#print('Задание: Пользователь вводит стороны прямоугольника, выведите его площадь; Задание: Пользователь вводит стороны прямоугольника, выведите его периметр')
#height= int(input('Введите длину прямоугольника: '))
#width = int(input('Введите ширину прямоугольника: '))
#print('Площадь прямоугольника: ', height * width)
#print('Периметр прямоугольника: ', height + width + height + width)
#print('Задание: Пользователь вводит радиус круга, выведите площадь круга')
#rd = float(input('Введите радиус круга: '))
#print('Радиус круга -', (rd ** 2) * 3.14)
#print('Задание: Посчитайте сумму трех введенных дробных чисел.')
#floata = float(input('Введите дробное число: '))
#if floata % 2 == 0 or floata % 2 == 1:
#    print('НУЖНО БЫЛО ВВЕСТИ ДРОБНОЕ ЧИСЛО!')
#else:
#    floatb = float(input('Введите второе дробное число: '))
#    if floatb % 2 == 0 or floata % 2 == 1:
#        print('НУЖНО БЫЛО ВВЕСТИ ДРОБНОЕ ЧИСЛО!')
#    else:
#        floatc = float(input('Введите третье дробное число: '))
#        if floatc % 2 == 0 or floatc % 2 == 1:
#         print('НУЖНО БЫЛО ВВЕСТИ ДРОБНОЕ ЧИСЛО!')
#        else:
#            print(floata, '+', floatb, '+', floatc, '=', floata + floatb + floatc)
#print('Задание: n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?')
#n = int(input('Сколько яблок ты принесешь? '))
#k = int(input('Со сколькими людьми поделишься? '))
#print('Всем досаниться по',n // k)
#print('Останется',n % k)
#print('Задание: Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность".')
#a = int(input('Введите первое число: '))
#b = int(input('Введите второе число: '))
#if a % 2 == b % 2:
#    print('Эти числа имеет одинаковую четность')
#else:
#    print('Эти два числа не имеют одинаковую четность')
#print('Задание: Даны три целых числа: A, B, C. Проверить истинность высказывания: "Хотя бы одно из чисел A, B, C положительное')
#numb1 = int(input('Введите 1 число: '))
#numb2 = int(input('Введите 2 число: '))
#numb3 = int(input('Введите 3 число: '))
#if numb1 >= 1 or numb2 >= 1 or numb3 >= 1:
#    print('Там есть положительное число')
#else:
#    print('Там нету положительного числа')
#print('Задание: Дано натуральное число. Выведите его последнюю цифру.')
#f = int(input('Введите число: '))
#print('Последнее число вашей цифры это', f % 10)
#print('Задание: Дано двузначное число. Найдите сумму его цифр.')
#user_input = input("Enter a two-digit number: ")
#if len(user_input) != 2:
#    print("Это не двухзначное число")
#else:     
#    first_digit = int(user_input[0])
#    second_digit = int(user_input[1]) 
#    sum_digits = first_digit + second_digit
#    print(f"Сумма цифр в числе {user_input} равняется: {sum_digits}")
#print('Задание: Дано трехзначное число. Найдите сумму его цифр.')
#user_input = input("Enter a two-digit number: ")
#if len(user_input) != 3:
#    print("Это не трехзначное число число")
#else:     
#    first_digit = int(user_input[0])
#    second_digit = int(user_input[1])
#    third_digit = int(user_input[2])
#    sum_digits = first_digit + second_digit + third_digit
#    print(f"Сумма цифр в числе {user_input} равняется: {sum_digits}")
#print('Задание: Дано трехзначное число. Проверить истинность высказывания: "Все цифры данного числа различны".')
#gg = input('Введите трехзначное число: ')
#if len(gg) != 3:
#    print('Это число не трехзначное!')
#else:
#    gg1 = int(gg[0])
#    gg2 = int(gg[1])
#    gg3 = int(gg[2])
#    if gg1 != gg3 and gg1 != gg2 and gg2 != gg3:
#        print('True')
#    else:
#        print('False')
#print('Задание: С начала суток прошло N секунд (N - целое). Найти количество часов, минут и секунд на электронных часах.')
#total_seconds = int(input("Введите число секунд: "))     
#hours = total_seconds // 3600  # Calculate hours
#minutes = (total_seconds % 3600) // 60  # Calculate remaining minutes
#seconds = total_seconds % 60  # Calculate remaining seconds
#print(f"{total_seconds} секунд равняется:")
#print(f"{hours} часов, {minutes} минут, и {seconds} секунд.")
#print('Задание: Пользователь вводит целое число. Выведите YES, если это число является четырехзначным, и NO в противном случае.')
#text = int(input('Введите число: '))
#if 10000 > text > 999:
#    print('YES')
#else:
#    print('NO')
#print('Задание: Пользователь вводит число N. Выведите все числа от 0 до N включительно.')
#dsd = int(input('Введите число: '))
#dsdn = dsd + 1
#for bsm in range(dsdn):
#    print(bsm)
#print('Задание: Пользователь вводит числа K и N. Выведите все числа от K до N включительно.')
#fgf = int(input('Введите k: '))
#fgg = int(input('Введите n: '))
#fggn = fgg + 1
#for bms in range(fgf, fggn):
#    print(bms)
#print('Задание: Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно.')
#hjh = int(input('Введите k: '))
#hjj = int(input('Введите n: '))
#hjjn = fgg + 1
#ghj = 0
#for bss in range(hjh, hjjn):
#    ghj += bss
#print(ghj)
#print('Задание: Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно.')
#dfg = int(input('Введите k: '))
#dff = int(input('Введите n: '))
#dffg = fgg + 1
#dddd = 0
#for bsffs in range(hjh, hjjn):
#    if bsffs % 2 == 0:
#       dddd += bsffs
#print(dddd)
#print('Задание: Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).')
#bhb = float(input('Введите N: '))
#print('Задание: Пользователь вводит числа A и B (A > B). Выведите четные числа от A до B включительно.')
#A = int(input('Введите число A: '))
#B = int(input('Введите число B: '))
#while A >= B:
#    A -= 1
#    if A % 2 == 1:
#        continue
#    print(A)
#print('Задание: Пользователь вводит числа A и B (A < B, A меньше B). Выведите числа от A до B включительно, которые делятся на три.')
#Ab = int(input('Введите число A: '))
#Ba = int(input('Введите число B: '))
#while Ab <= Ba:
#    Ab += 1
#    if Ab % 3 == 0:
#        print(Ab)
#print('Задание: Пользователь вводит числа до тех пор, пока не введет 0. Выведите сумму введенных чисел (0 считать не нужно).')
#abc = int(0)
#while True:
#    cba = int(input('Введите число: '))
#    if cba == 0:
#        break
#    abc += cba
#print(abc)
#print('Задание: Пользователь вводит числа до тех пор, пока не введет 0. Выведите максимальное введенное число (0 считать не нужно).')
#asd = int(0)
#dsa = int(input('Введите число: '))
#while dsa != 0:
#    if dsa >= asd:
#        asd = int(0)
#        asd += dsa
#    dsa = int(input('Введите число: '))
#if dsa == 0:
#    print(asd)
#print('Задание: Пользователь вводит числа до тех пор, пока не введет 0. Выведите минимальное введенное число (0 считать не нужно).')
#rty = int(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
#ytr = int(input('Введите число: '))
#while ytr != 0:
#    if rty >= ytr:
#        rty = int(0)
#        rty += ytr
#    ytr = int(input('Введите число: '))
#if ytr == 0:
#    print(rty)
#print('Задание: Пользователь вводит число N. Выведите факториал число N. Факториал числа N - это произведение всех чисел от 1 до N включительно. Например, факториал числа 5 равен 120.')
#J = int(input('Введите число: '))
#Ja = int(J + 1)
#K = int(1)
#for Java in range(1, Ja):
#    K *= Java
#print(K)
#print('Задание: Пользователь вводит число N. Выведите N-ное по счету число Фибоначчи. Последовательность чисел Фибоначчи рассчитывается по такой формуле: F(1) = 1, F(2) = 1, F(K) = F(K-2) + F(K-1). Идея такая: каждое следующее число равно сумму двух предыдущих.Первые 10 чисел последовательности: 1 1 2 3 5 8 13 21 34 55 ...')
#print('Задание: Создайте список из 10 четных чисел и выведите его с помощью цикла for')
#ten_even_nums = list(range(0, 20, 2))
#for iedf in ten_even_nums:
#    print(iedf, end=' ')
#print(' ')
#print('Задание: Создайте список из 5 элементов. Сделайте срез от второго индекса до четвертого')
#five_drinks = ['Pepsi', 'Fanta', 'Lipton', 'Water', 'Green Tea']
#print(five_drinks[1:4])
#print('Задание Напишите функцию, которая возвращает True, если число делится на 3, и False, если - нет.')
#def isaac(z):
#    return z % 3 == 0

#isaaac = int(input('Введите число: '))
#print(isaac(isaaac))
#def maxList(a, b, c):
#    if a > b and a > c:
#        return a
#    elif b > a and b > c:
#        return b
#    elif c > a and c > b:
#        return c
#    else:
#        return a
#numlist = [2, 6, 4]
#print(maxList(numlist[0], numlist[1], numlist[2]))
#print('Задание: Напишите функцию, которая возвращает количество четных элементов в списке.')
#evenlist = []
#def evenCounter(a, b, c, d, e):
#    if a % 2 == 0:
#        evenlist.append(a)
#    if b % 2 == 0:
#        evenlist.append(b)
#    if c % 2 == 0:
#        evenlist.append(c)
#    if d % 2 == 0:
#        evenlist.append(d)
#    if e % 2 == 0:
#        evenlist.append(e)
#    return len(evenlist)
#print(evenCounter(2, 6, 5, 7, 8))
#print('Задание: Пользователь вводит имя, фамилия, возраст. Создайте словарь user и запишите данные пользователя в него.')
#firstnamei = input('Введите имя: ')
#lastnamei = input('Введите фамилию: ')
#agei = input('Введите свой возраст: ')

#user = dict(firstname=firstnamei, lastname=lastnamei, age=agei)
#print(user)
#print('Пользователь вводит 3 фрукта в формате: название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.c')
#fruits = dict()
#fruit1 = input('Введите первый фрукт: ')
#fruit1value = input('Его количество: ')
#fruit2 = input('Введите второй фрукт: ')
#fruit2value = input('Его количество: ')
#fruit3 = input('Введите третий фрукт: ')
#fruit3value = input('Его количество: ')
#fruits.setdefault(fruit1, fruit1value)
#fruits.setdefault(fruit2, fruit2value)
#fruits.setdefault(fruit3, fruit3value)
#fruitss = fruits.items
#print(fruits)
#print('Задание: Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.')
#learningenglish = dict()
#englishlesson1 = input()
#englishlesson2 = input()
#englishlesson3 = input()
#englishlesson1.split('-', maxsplit=1)
#englishlesson2.split('-', maxsplit=1)
#englishlesson3.split('-', maxsplit=1)
#learningenglish.setdefault(englishlesson1)
#learningenglish.setdefault(englishlesson2)
#learningenglish.setdefault(englishlesson3)
#print(learningenglish)
