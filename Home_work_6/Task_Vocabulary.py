"""4. Английский словарь
"Пора учить английский язык", - сказал себе Степа и решил написать программу
для изучения английского языка. Программа получает на вход слово на английском
языке и несколько его переводов на русском языке. Составьте словарь, в котором
ключ - это английское слово, а значение - это список русских слов. В этой задаче
нужно использовать строчный метод split().
apple - яблоко
orange - оранжевый, апельсин, рыжий
grape - виноград, виноградный, гроздь
easy - простой, легкий, нетрудный, удобный, несложный"""

n = int(input('Сколько будет слов? '))
vocab = {}
print('Введите информацию о словах')
for i in range(n):
    name = input('слово: ')
    trans = input('переводы через пробел: ').split(' ')
    vocab[name] = trans

print('')
print('Сгенерированный словарь -', vocab)

# Правильное решение - преподавателем

count = int(input())
translate_dict = {}
for _ in range(count):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
print(translate_dict)
# запрос к словарю
eng_word = input('Введите слово для перевода: ')
print(', '.joint(translate_dict[eng_word]))
print(translate_dict.get(eng_word))   # не будет ошибки если слова нет (напр. banana)
print(translate_dict.get(eng_word), 'такого слова нет в словаре')

if translate_dict.get(eng_word):
    print(translate_dict.get(eng_word)
else:
    print('такого слова нет в словаре')
