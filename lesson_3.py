'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

#num = int(input('введите делимое:'))
num = 3

#num_2 = int(input('введите делитель:'))
num_2 = 0


def cilc_devision (a, b):
    if b == 0:
        return -1
    else:
       return a / b


print ( cilc_devision(num,num_2))


'''
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''
b = []

def show_address(*addition, **kwaddition):
    if addition:
        print(addition)
    if kwaddition:
        for key, val in kwaddition.items():
            print(f'{key} : {val}', end= ' ')


show_address(name = 'Max', surname = 'Popov', year_birthday = 1990,
             city = 'moscow', email = 'asd@mail.job', phone = 12345 )



#show_address('Max', 'Popov', 1990, 'moscow', 'asd@mail.job', 12345 )


'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''



def print_summ (a, b, c):
    sum_max = []
    sort_2 = []
    sum_max.append(a)
    sum_max.append(b)
    sum_max.append(c)
    while True:
        if len(sum_max) == 0:
            break
        for i in range (len(sum_max) - 1):
            if sum_max[i] > sum_max[i + 1]:
                sum_max[i], sum_max[i + 1] = sum_max[i + 1], sum_max[i]
            else:
                i += 1
        sort = sum_max.pop()
        sort_2.insert(0,sort)
    result = sort_2[-1] + sort_2[-2]
    return result



print(print_summ(64,36,5))



'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def print_my_func(x, y):
    print(x ** y)



print_my_func(10,-3)



def print_my_func_2(x,y):
    cnt = 0
    aws = 1
    res = []
    if y < 0:
        y = abs(y)
        while cnt < y:
            res.append(x)
            cnt += 1
            aws *= x
        print(1 / aws)
    else:
        while cnt < y:
            res.append(x)
            cnt += 1
            aws *= x
        print(aws)


print_my_func_2(10,-3)




'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''
def print_sum():
    print('выход из программы "q" ')
    count = 0
    cnt = 0
    num_2 = []
    num_3 = []
    er = []
    while True:
        #num = input('введите числа через пробел: ').split()
        num = '1' '2' '3' '4' 'q'
        if num == ['q']:
            print('выход')
            break

        else:

            for item in num:
                if item == 'q':
                    er.append(item)
                    break
                num_2.append(int(item))
                while cnt != len(num_2):
                    count += num_2[cnt]
                    cnt += 1
            num_3.append(count)
            count = 0
            print(num_3)
            if er == ['q']:
                print('выход')
                break



print_sum()



'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def conv_int_func(word):
    result_2 = []
    result = chr(ord(word[0]) - 32)
    result_2.append(result)
    for item in range(1,len(word)):
        result_2.append(word[item])
        result_2 = [''.join(result_2)]
    return result_2


def print_int_func_2(text):
    result_2 = []
    result_3 = []
    result = (text).split()
    for itm in range(len(result)):
        result_2.append(conv_int_func(result[itm]))

    for dex in result_2:
        for word in dex:
            result_3.append(word)
    result_3 = (' '.join(result_3))
    print(result_3)



#print_int_func_2(input('введите пердложение : '))
print_int_func_2('hello world')


