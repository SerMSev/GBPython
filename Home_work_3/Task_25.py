"""25 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10"""
import time

n = int(input('Введите десятичное число: '))

# с помощью встроенной функции
start1 = time.perf_counter()
b1 = bin(n)
end1 = time.perf_counter()

# математически через накопление в строке
start2 = time.perf_counter()
b2 = ''
i = n
while i > 0:
    b2 = str(i % 2) + b2
    i = i // 2
end2 = time.perf_counter()

# через список
start3 = time.perf_counter()
b3 = []
i = n
while i != 0:
    b3.append(i % 2)
    i //= 2
b3.reverse()
end3 = time.perf_counter()

print()
print('Результаты трех вариантов:')
print(b1, ' = ', b2, ' = ', *b3, sep='')

print()
print('Затраченное время:')
print(end1 - start1, '\t', end2 - start2, '\t', end3 - start3)
print('если принять время выполнения для 1 варианта за еденицу, то получим:')
print(1, (end2 - start2) / (end1 - start1), (end3 - start3) / (end1 - start1), sep='\t')