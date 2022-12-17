"""Задайте список из n чисел последовательности (1 + 1/n) ** n
 и выведите на экран их сумму.
Пример:
-Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06"""

number = int(input('Введите целое число: '))
print(f'Для n={number} ', end='{')
summ = 0
for i in range(1, number):
    formula = (1 + 1 / i) ** i
    summ += formula
    print(f'{i}: {round(formula, 2)}', end=', ')
print(f'{number}: {round((1 + 1 / number) ** number, 2)}', '}')
print('Сумма ', round(summ + (1 + 1 / number) ** number, 2))
