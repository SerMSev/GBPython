# 4.Создайте список из случайных чисел. Найдите количество различных элементов в нем.

# Генерируем случайный набор данных
n = int(input('Сколько будет элементов? '))
list_in = []
for i in range(n):
    list_in.append(random.randint(1, 10))
print('Сгенерированный набор данных -', list_in)

# Решаем задачу
print()
print('1-ый вариант - список, цикл for')
start = perf_counter()
list_out = []
for el in list_in:
    if el not in list_out:
        list_out.append(el)
end = perf_counter()
print('Различных элементов в списке - ', len(list_out))
print('Список неповторяющихся элементов последовательности (в порядке появления): ', list_out)
print('Вермя работы - ', round(end - start, 6))

print()
print('2-ой вариант - списковое включение (list comprehension)')
start = perf_counter()
list_out = []
[list_out.append(el) for el in list_in if el not in list_out]
end = perf_counter()
print('Различных элементов в списке - ', len(list_out))
print('Список неповторяющихся элементов последовательности (в порядке появления): ', list_out)
print('Вермя работы - ', round(end - start, 6))

print()
print('3-ий вариант - множество')
start = perf_counter()
set_out = set()
[set_out.add(el) for el in list_in]
end = perf_counter()
print('Различных элементов в списке - ', len(set_out))
print('Множество неповторяющихся элементов последовательности : ', set_out)
print('Вермя работы - ', round(end - start, 6))

# решение - преподавателем
import random
some_list = [random.randint(1, 10) for _ in range(10)]
some_set = set(some_list)
print(len(some_set))