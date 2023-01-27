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

# Правильное решение - преподавателем

N = int(input())
dict_list = []
# min_age = 1000
min_name = ''
for _ in range(N):
    name = input()
    age = int(input())
    # if age < min_age:
    #     min_age = age
    #     min_name = name
    dict_list.append({'name': name, 'age': age})
print(dict_list)
# решаем далее  через список словарей
# сначала ищем мин возраст (это вместо 3-х строк вышезакоментированного if
min_age = dict_list[0]['age']   # минимальным считаем возраст первого друга
for some_dict in dict_list:
    if some_dict['age'] < min_age:
        min_age = some_dict['age']
        min_name = some_dict['name']
# for some_dict in dict_list:
#     if some_dict['age'] == min_age:
#         print(some_dict['name'])
#         break