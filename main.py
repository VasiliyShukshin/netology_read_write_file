with open("cookbook.txt", "r", encoding="UTF-8") as cook_book_file:
    cook_book = {}
    try:
        while True:
            name = cook_book_file.readline().strip()
            number_of_ingredients = int(cook_book_file.readline().strip())
            i = 0
            super_ingrediet_listt = []
            while i < number_of_ingredients:
                ingredients_list = cook_book_file.readline().strip().split(" | ")
                ingredients_dict = {'ingredient_name': ingredients_list[0], 'quantity': int(ingredients_list[1]),
                                    'measure': ingredients_list[2]}
                super_ingrediet_listt.append(ingredients_dict)
                cook_book[name] = super_ingrediet_listt
                i += 1
            next(cook_book_file)
    except StopIteration:
        None
        # for key, value in cook_book.items():
        #     print("{0}: {1}".format(key, value))


def get_shop_list_by_dishes(dishes, person_count=int()):
    shop_dict = {}
    # для каждого блюда из  списка заказаннных блюд
    for dish in dishes:
        # если заказанное блюдо есть в кулинарной книге
        if dish in cook_book:
            # перебираем необходдимы продукты и добавляем в список покупок
            for product in cook_book[dish]:
                # если продукт уже есть в списке
                if product['ingredient_name'] in shop_dict:
                    shop_dict[product['ingredient_name']]['quantity'] += product['quantity']
                    # print(shop_dict[product['ingredient_name']]['quantity'])
                    # print(product['quantity'])
                else:
                    shop_dict[product['ingredient_name']] = {'measure': product['measure'],
                                                             'quantity': int(product['quantity'])}
        else:
            print(f"{dish} - такого  блюда нет в cook_book")
    for key, val in shop_dict.items():
        val['quantity'] = val['quantity'] * person_count
        # print(key, val)
        # print(shop_dict)
    return print(shop_dict)


get_shop_list_by_dishes(['Омлет', 'Омлет', 'Яичница'], 2)
