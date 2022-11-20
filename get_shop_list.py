cook_book = {
    'Омлет': [
        {'ingridient_name': 'Яйца', 'quantity': 2, 'measure': 'шт'},
        {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'}
    ],
    'Фахитос': [
        {'ingredient_name': 'Говядина', 'quantity': 500, 'measure': 'гр'},
        {'ingredient_name': 'Перец сладкий', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Лаваш', 'quantity': 2, 'measure': 'шт'},
        {'ingredient_name': 'Винный уксус', 'quantity': 1, 'measure': 'ст.л'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ]
}


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print(
            '{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчёте на одного человека (через запятую):').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print(shop_list)


create_shop_list()
