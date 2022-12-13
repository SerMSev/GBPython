"""Напишите программу, которая по заданному номеру четверти, показывает
 диапазон возможных координат точек в этой четверти (x и y)."""
quarter = int(input())
if quarter == 1:
    print('x>0 y>0')
if quarter == 2:
    print('x<0 y>0')
if quarter == 3:
    print('x<0 y<0')
else:
    print('x>0 y<0')