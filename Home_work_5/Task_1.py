# №1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
letters = ["а", "б", "в"]
filename = "data1.txt"
result = str()

with open(filename, encoding='utf-8') as file_in:
    for line in file_in:
        line = line.rstrip()
        result = ''
        print(line)
        for word in line.lower().split():
            splited = [char for char in word if char not in letters]
            if word == ''.join(splited):
                result = result + word + ' '

        print(result)
        print()
