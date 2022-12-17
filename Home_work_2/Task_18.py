"""Реализуйте алгоритм перемешивания списка"""

import random
text = 'шла Саша по шоссе и сосала сушку'
word_list = text.split(' ')
print(word_list)

random.shuffle(word_list)

print(word_list)