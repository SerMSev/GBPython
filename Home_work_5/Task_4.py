# №4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


file_in_name = 'data2-in.txt'
file_out_name = 'data2-out.txt'

print("Кодирование данных из файла")
print("===========================")
with open(file_in_name, 'r', encoding='utf-8') as file_in:
    text = file_in.read()
    print("Исходные данные:       ", text, " - длина ", len(text), "символов")
    encoded_text = rle_encode(text)
print("Закодированные данные: ", encoded_text, " - длина ", len(encoded_text), "символов")
with open(file_out_name, 'w', encoding='utf-8') as file_out:
    file_out.write(encoded_text)
    file_out.close()

print()
print("Декодирование данных из файла")
print("=============================")
with open(file_out_name, 'r', encoding='utf-8') as file_in:
    text = file_in.read()
    print("Закодированные данные: ", text)
    decoded_text = rle_decode(text)
print("Расшифровынные данные: ", decoded_text)


# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# 6A1F2D7C1A17E
