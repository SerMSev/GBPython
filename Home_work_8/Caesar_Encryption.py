"""Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, которая
отстоит в алфавите на некоторое фиксированное число позиций.
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша
функция кодирует сдвиг алфавита на 3 позиции:
А→Г,А→Г,
Б→Д,Б→Д,
В→Е,В→Е,
……
Э→А,Э→А,
Ю→Б,Ю→Б,
Я→ВЯ→В
Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
превращаться в маленькие, большие — в большие.
Напишите также функцию декодирования decrypt_caesar(msg, shift), также
использующую сдвиг по умолчанию. При написании функции декодирования используйте
вашу функцию кодирования.
3  Да здравствует салат Цезарь!     Зг кзугефхецих фгогх Щикгуя!
5  Да здравствует салат Цезарь!     Йе мйхезцчзшкч цереч Ыкмехб!
"""

def encrypt_caesar(msg, shift=3):
    small_symbols1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big_symbols1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small_symbols1)
    small_symbols2 = small_symbols1[shift:] + small_symbols1[:shift]
    big_symbols2 = big_symbols1[shift:] + big_symbols1[:shift]
    translation = msg.maketrans(small_symbols1 + big_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)

# s = 3
text1 = 'Да здравствует салат Цезарь!'
text = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ  абвгдежзийклмнопрстуфхцчшщъыьэюя'
print(text)
enc_text = encrypt_caesar(text)
print(enc_text)
print()
#
print(decrypt_caesar(enc_text))
