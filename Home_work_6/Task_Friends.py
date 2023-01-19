"""3. Еще немного о друзьях
Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
Создайте список friends и добавьте в него N словарей с ключами name и age. Выведите
средний возраст всех друзей и самое длинное имя."""

n = int(input('Сколько будет друзей? '))
friends = {}
ave_age = int()
name_length = int()
longest_name = str()
print('Введите информацию о друзьях')
for i in range(n):
    print(f'Друг {i}:')
    name = input('имя: ')
    age = int(input('возраст: '))
    friends[name] = age
    ave_age += age
    if len(name) > name_length:
        name_length = len(name)
        longest_name = name
ave_age = ave_age / n

print('')
print('Сгенерированный словарь -', friends)
print('Средний возраст - ', round(ave_age, 2))
print('Самый длинное имя - ', longest_name)