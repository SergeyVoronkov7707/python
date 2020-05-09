'''
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''


with open('test.txt', 'w', encoding= 'utf-8') as f:
    while True:
        word = input('введите текст: ')
        if word == '':
            break
        else:
            f.write(f'{word} \n')

with open('test.txt', encoding= 'utf-8') as fn:
    print(fn.read())

'''
2. Создать текстовый файл (не программно),
 сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
'''


with open('/home/sergey/учеба/voina_stih.txt', 'r', encoding='utf-8') as f:
    file_read = f.read()
    print(file_read)

with open('/home/sergey/учеба/voina_stih.txt', 'r', encoding='utf-8') as f:
    file = f.read().splitlines()
    print(f'кол-во строк : {len(file)}')

    for cnt, word in enumerate(file, 1):
        count = len(word.split())
        print(f'в строке {cnt} слов : {count} ')


'''
3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''


def print_salary(file):
    with open(file, encoding='utf-8') as fn:
        read_line = fn.read().splitlines()
    print(read_line)
    print(f'Cотрудники с доходом менее 20т.р.: ', end='')
    value_ap = 0
    for word in read_line:
        key, value = word.split()
        value_ap += int(value)
        if int(value) < 20000:
            print(key, end=', ')
    print(f'\nCумма доходов: {value_ap}, кол-во чел: {len(read_line)}, средний доход: {value_ap / len(read_line)}')


print_salary('salary.txt')


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
'''

rus_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def fch(x):
    ind = x.find(' ')
    key = x[0:ind]
    z = rus_dict[key]
    x = x.replace(key, z)
    with open('new_num.txt', 'a', encoding='utf-8') as fw:
        fw.write(x)


with open('numbers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        fch(line.lower())


'''
5. Создать (программно) текстовый файл,
записать в него программно набор чисел,разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

from random import randint

a = (randint(-10, 10) for i in range(4))

with open('wr.txt', 'w', encoding='utf-8') as f:
    for i in a:
        f.write(str(i) + " ")

with open('wr.txt', 'r', encoding='utf-8') as fn:
    read_file = fn.read()
    print(read_file)
    read_file = read_file.split()

g = 0
list_fl = list(map(int, read_file))

for i in list_fl:
    g += i
print(f'сумма = {g}')


'''
6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
result = {}

with open('lesson.txt', encoding='utf-8') as f:
    read_file = f.read().splitlines()
    read_file = [word.split() for word in read_file]
    print(read_file)

for i in range(len(read_file)):
    x = 0
    for y in range(1, 4):
        if read_file[i][y] != '-':
            t = str(read_file[i][y])
            ind = t.find('(')
            x = x + int(t[0:ind])
    result.update({read_file[i][0]: x})

print(result)


'''
7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные
о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью.
  Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json

result = {}
result_ap = {}

with open('firm.txt', encoding='utf-8') as f:
    read_file = f.read().splitlines()
    read_file = [word.split() for word in read_file]
    print(read_file)

profit2 = 0
n = 0
for i in range(len(read_file)):
    profit = int(read_file[i][2]) - int(read_file[i][3])
    result.update({read_file[i][0]: profit})
    if profit >= 0:
        profit2 = profit + profit2
        n += 1

result_ap.update({"average_profit": round(profit2 / n, 2)})

s = str([result, result_ap])
print(s)
with open('profit.json', 'w', encoding='utf-8') as fn:
    json.dump(s, fn)

with open('profit.json', encoding= 'utf-8') as fr:
    print(json.load(fr))
