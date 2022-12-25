"""30
Вычислить число Пи c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$"""

import math
import fractions

print(math.pi)
with open('data30.txt', 'r', encoding='utf-8') as file:
    str_input = file.readline().split('.')
    # в виде одного выражения
    print(int(math.pi * 10 ** len(str_input[1])) / 10 ** len(str_input[1]))

    # с разбивкой выражения на части и описанием каждой из них
    precision = len(str_input[1])  # кол-во знаков после запятой - 3 в нашем примере
    mult = 10 ** precision  # десять в степени precision - 1000 в нашем примере
    result = int(math.pi * mult) / mult  # отбрасываем лишние знаки- 3.141 в нашем примере
    print(result)
