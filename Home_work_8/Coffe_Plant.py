"""На заводе «Кофейный» открывается новое кафе. Изначально есть некоторое количество
кофейных зерен, молока и взбитых сливок.
Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), которая
возвращает напиток, который можно приготовить из имеющихся продуктов (ingredients). На
вход функция принимает заранее неизвестное количество предпочтений посетителя. Все
напитки перечислены в порядке убывания предпочтений и гарантированно не повторяются.
Бариста готовит наиболее предпочитаемый напиток из доступных.

Для Эспрессо требуется: 1 порция кофейных зерен.
Для Капучино требуется: 1 порция кофейных зерен и 3 порции молока.
Для Маккиато требуется: 2 порции кофейных зерен и 1 порция молока.
Для Кофе по-венски требуется: 1 порция кофейных зерен и 2 порции взбитых сливок.
Для Латте Маккиато требуется: 1 порция кофейных зерен, 2 порции молока и 1 порция взбитых
сливок.
Для Кон Панна требуется: 1 порция кофейных зерен и 1 порция взбитых сливок.

При приготовлении напитка ингредиенты расходуются.
Если недостаточно ингредиентов, то вернуть сообщение: «К сожалению, не можем предложить
Вам напиток»."""

def choose_coffee(pref):
    for cof in pref:
        ind = 0
        for ingr in range(3):
            ingredients[ingr] = int(ingredients[ingr])
            if receips[cof][ingr] <= ingredients[ingr]:
                ind += 1
        if ind == 3:
            for ingr in range(3):
                ingredients[ingr] -= receips[cof][ingr]
            return cof
    return 'К сожалению, не можем предложить Вам напиток'

# Справочник рецептов. Формат записи - name: [bean_qty, milk_qty, cream_qty]
receips = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0], 'Маккиато': [2, 1, 0],
           'По-венски': [1, 0, 2], 'Латте Маккиато': [2, 0, 1], 'Кон Панна': [1, 0, 1]}

# Пополняем склад продуктов
print('Введите количество продуктов, имеющееся на складе в порциях:')
print('через запятую - кофейные зерна, молоко, взбитые сливки')
ingredients = list(input().strip().split(','))
print(ingredients)
print()

# Выводим меню и вводим список предпочтений клиента
print('Наш бариста умеет готовить следующие марки кофе: ')
print(*receips.keys(), sep='\n')
print()
print('Введите (через запятую без пробелов) марки кофе в порядке убывания вашего предпочтения: ')
prefer = list(input().split(','))
print(prefer)

again = 'Д'
while again == 'Д':
    result = choose_coffee(prefer)
    print(result)
    again = input('Еще чашечку? (Д - да): ')

