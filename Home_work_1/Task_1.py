""" Задача 6
 Напишите программу, которая принимает на вход цифру, обозначающую день недели,
 и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет"""
week_day_number = int(input())
if 6 <= week_day_number <= 7:
    print('Да')
else:
    print('Нет')