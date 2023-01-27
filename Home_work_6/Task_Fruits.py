""" 1. Фрукты
Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате:
название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта
- это ключ, а количество - значение"""

n = int(input('Сколько будет фруктов? '))
fruits = {}
print('Введите информацию о фруктах в порядке - название количество')
for i in range(n):
    print(f'Фрукт {i}:')
    name = input('назваеие: ')
    qty = input('количество: ')
    fruits[name] = qty
print('Сгенерированный словарь -', fruits)

# решение преподователя

count = int(input())
fruit_dict = {}
for _ in range(count):
    fruit = input()
    count_fruit = int(input())
    fruit_dict[fruit] = count_fruits
print(fuit_dict)