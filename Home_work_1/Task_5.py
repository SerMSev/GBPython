""" Задача 7 (необязательная)
 Напишите программу для. проверки истинности утверждения
  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
 НЕОБЯЗАТЕЛЬНАЯ"""
print('  X  ', '\t', ' Y  ', '\t', '  Z  ', '\t', '     ', 'результат')

x = False
for x in [False, True]:
    y = False
    for y in [False, True]:
        z = False
        for z in [False, True]:
            first = not (x or y or z)
            second = not x and not y and not z
            print(x, '\t', y, '\t', z, '\t', ' -> ', '\t', first == second)