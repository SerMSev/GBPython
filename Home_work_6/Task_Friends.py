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

# Правильное решение - преподавателем

N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
summa = 0
max_name = dict_list[0]['name']
for i in dict_list
    summa += i['age']
    if len(i['name']) > len(max_name):
        max_name = i['name']
print(summa / N)
print(max_name)


# как добавить в словарь список

N = int(input())
dict_list = []
for _ in range(N):
    name = input()
    age = int(input())
    dict_list.append({'name': name, 'age': age})
print(dict_list)
big_dict = {'name': [], 'age': []}
for el in dict_list:
    big_dict['name'].append(el['name'])
    big_dict['age'].append(el['age'])
print(big_dict)
print(big_dict.values())

