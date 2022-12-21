"""24 Задайте список из вещественных чисел. Напишите программу, которая найдёт
разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

item_list = input('Введите исходный список вещественных чисел через пробел:').split(' ')

# временный список
temp_list = []
for i in range(len(item_list)):
    temp_list.append(item_list[i])

min = 1
max = 0

for i in range(len(temp_list)):
    # конвертируем строки списка в вещественные числа и вычитаем целую часть
    temp_list[i] = round(round(float(temp_list[i]), 2) - round(float(temp_list[i]) - 0.49, 0), 2)

    if temp_list[i] != 0.0:
        min = temp_list[i] if temp_list[i] < min else min
        max = temp_list[i] if temp_list[i] > max else max

print(item_list, ' => ', round(max-min, 2))
