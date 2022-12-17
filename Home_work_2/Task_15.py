"""Напишите программу, которая принимает на вход число N и выдает
 набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)"""

def factor(x):
    if x == 0:
        return 1
    else:
        return factor(x - 1) * x

number = int(input('Введите целое число: '))
print('[', end=' ')
for i in range(1, number):
    print(factor(i), end=', ')
print(factor(number), ']')



