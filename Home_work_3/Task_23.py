"""23 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый
 и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

item_list = input('Введите исходный список целых чисел через пробел:').split(' ')
for i in range(len(item_list)):
    item_list[i] = int(item_list[i])

result_list = []
iterations = len(item_list) // 2 +1 if len(item_list) % 2 else len(item_list) // 2

for i in range(len(item_list)):
    result_list.append(item_list[i] * item_list[len(item_list)-1-i])
    iterations -= 1
    if iterations == 0:
        break
print(item_list, ' => ', result_list)

