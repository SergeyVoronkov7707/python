'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

def calc_salary(a,b,c):
    the_salary = a * b + c
    return the_salary

__name__ = '__main__'

# print(calc_salary(int(input('введите часы: ')),
#                   int(input('введите ставку: ')), int(input('введите премию: '))))

print(calc_salary(131,140,15000))


'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
'''

import random


result_list = []

a = list(random.randint(1,15) for i in range(15))
print(a)

result_list2 = [ result_list.append(a[i])  if a[i] > a[i + 1] else result_list.append(a[i + 1])   for i in range(len(a) - 1)]

print(result_list)


'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''
from random import randint

a = [randint(20, 240) for i in range(100)]
print(a)
c = []

b = [c.append(a[num]) if a[num] % 20 == 0 or a[num] % 21 == 0  else num   for num in range(len(a))]
print(c)


'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''
from random import randint

a = [randint(1,100) for _ in range(15)]
print(a)

result = []

c = [result.append(num) if num not in result else num for num in a]
print(result)


'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce as rd
from random import randint

a = [randint(100,1000 + 1) for i in range(15)]
print(a)

a_reduce = rd(lambda x, y: x * y, a)
print(a_reduce)


'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
from itertools import cycle, count



for el in count(3):
    print(el)



for el in cycle('abc'):
    print(el)