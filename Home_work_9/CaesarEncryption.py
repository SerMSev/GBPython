"""Вариант с рекурсией"""

small_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]


def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:
        return symbols[(index - n) % len(symbols)]


def encrypt(text, n=3, i=0, res=""):
    if (len(res) == len(text)): return res

    if text[i].isupper():
        res += shift(text[i], big_symbols, n)

    elif text[i].islower():
        res += shift(text[i], small_symbols, n)
    else:
        res += text[i]

    return encrypt(text, n, i + 1, res)


def decrypt(text, n=3, i=0, res=""):
    if (len(res) == len(text)): return res

    if text[i].isupper():
        res += back_shift(text[i], big_symbols, n)

    elif text[i].islower():
        res += back_shift(text[i], small_symbols, n)
    else:
        res += text[i]

    return decrypt(text, n, i + 1, res)

# 3  Да здравствует салат Цезарь!     Зг кзугефхецих фгогх Щикгуя!
# 5  Да здравствует салат Цезарь!     Йе мйхезцчзшкч цереч Ыкмехб!

input_str = 'Да здравствует салат Цезарь!'
input_str1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ  абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
str = encrypt(input_str1)
print(str)
print(decrypt(str))


"""Вариант без рекурсии"""

small_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]


def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:
        return symbols[(index - n) % len(symbols)]


def encrypt(text, n=3):
    res = ""

    for i in range(0, len(text)):
        if text[i].isupper():
            res += shift(text[i], big_symbols, n)

        elif text[i].islower():
            res += shift(text[i], small_symbols, n)
        else:
            res += text[i]

    return res


def decrypt(text, n=3):
    res = ""

    for i in range(0, len(text)):
        if text[i].isupper():
            res += back_shift(text[i], big_symbols, n)

        elif text[i].islower():
            res += back_shift(text[i], small_symbols, n)
        else:
            res += text[i]

    return res


str = encrypt(input())
print(str)
print(decrypt(str))

""" Описание 

Рассмотрим подробнее второй вариант. Сначала я создал списки из русских букв 
верхнего и нижнего регистра. Далее идёт функция смещения (shift). Зачем 
функция? Чтобы не копипастить код, с различием только в списке букв для поиска.

Сама функция принимает на вход одну букву (ну, или надеется, что вы дадите 
1 букву), список букв для поиска, смещение. Далее вычисляет индекс этой буквы 
в списке (метод find), потом проверяет, можно ли получить букву, смещённую на 
n позиций. Если да - возвращает эту букву. Если же нет, определяет букву по 
принципу Э →А, Ю →Б, Я →В и т. д. и всё равно возвращает изменённую букву.

Функция back_shift делает тоже самое, только наоборот.

И теперь интересное - функция encrypt. Она получает текст и смещение.

Зачем n=3, можно же просто n? Нельзя. Благодаря этому функция использует 
стандартное смещение (3), если не указано пользовательское. Иначе вы бы 
получали ошибку:

TypeError: encrypt() missing 1 required positional argument: 'n'

Далее запускается цикл for, который проходится по всей строке. Он проверяет - 
если буква text[i] является маленькой - запускает функцию смещения, как для 
маленькой буквы. И соответственно также для больших букв. (Вот он, плюс 
использовать функцию! Иначе пришлось бы копировать кусок кода от шифрования 
маленьких букв и менять список на список больших. И так каждый раз, когда 
нужно поменять регистр или язык символов... С функцией можно просто передавать, 
как аргумент список других букв.)

И если буква не является ни большой, ни маленькой - значит это другой символ 
(пробел, точка, кавычки и т.д.). В таком случае ничего не меняется.

И расшифровка, тоже самое, только наоборот (где-то я это уже видел...)

А вот и часть кода, которая выполнится при старте программы (наконец-то мы её 
нашли!). Она просто ждёт ввода пользователя - запускает шифрование, а потом 
дешифрирование.

P.S - пример с рекурсией выглядит красиво, но будет работать чуть медленнее, и 
при строках не больше 2000 - 3000 символов. (Такие уж в python ограничения).

Поделиться
Улучшить ответ
Отслеживать
ответ дан 19 июн 2020 в 15:22
Стас's user avatar
Стас
1,84311 золотой знак66 серебряных знаков24
"""