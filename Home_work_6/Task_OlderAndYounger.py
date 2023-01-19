""" 2. Старший и младший
Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
Создайте список friends и добавьте в него N словарей с ключами name и age.
Найдите самого младшего из друзей и выведите его имя"""

n = int(input('Сколько будет друзей? '))
friends = {}
min_age = 999
min_name = str()
print('Введите информацию о друзьях')
for i in range(n):
    print(f'Друг {i}:')
    name = input('имя: ')
    age = int(input('возраст: '))
    friends[name] = age
    if age < min_age:
        min_age = age
        min_name = name

print('')
print('Сгенерированный словарь -', friends)
print('Самый младший - ', min_name)