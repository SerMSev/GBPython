"""31
Задайте натуральное число N. Напишите программу, которая составит список
 простых множителей числа N"""

with open('data31.txt', 'r', encoding='utf-8') as file:
    num = int(file.read())
    print('Введено число: ', num)
    result = []
    ind = 2
    while ind * ind <= num:
        while num % ind == 0:
            result.append(ind)
            num /= ind
        ind += 1
    if num > 1:
        result.append(int(num))
    print('Простые множители: ', *result)
