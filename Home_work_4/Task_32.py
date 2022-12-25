"""32
Задайте последовательность чисел. Напишите программу, которая выведет список
 неповторяющихся элементов исходной последовательности."""

import random

# создаем файл с входными данными
num = int(input('Сколько будет чисел в последовательности? '))
with open('data32.txt', 'w', encoding='utf-8') as file:
    for i in range(num - 1):
        file.write(str(random.randint(-num, num)) + ' ')
    file.write(str(random.randint(-num, num)))

# решаем задачу
str_output = []
s = []
with open('data32.txt', 'r', encoding='utf-8') as file:
    str_input = file.readline().split(' ')
    print('Исходная последовательность чисел (считано из файла): ', str_input)
    for el in str_input:
        if el not in str_output:
            str_output.append(el)
    print('Список неповторяющихся элементов последовательности (в порядке появления): ', str_output)
