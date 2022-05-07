with open("cookbook.txt", "r", encoding="UTF-8") as cook_book_file:
    # for line in cook_book_file:
    #     # print(line)
    #     print(line.strip().split(" | "))
    #     # print(line.split("|"))
    cook_book = {}
    try:
        while True:
            name = cook_book_file.readline().strip()
            number_of_ingredients = int(cook_book_file.readline().strip())
            # print(name)
            # print(number_of_ingredients)
            # cook_book = {name: cook_book_file.readline().strip().split(" | ") for a in range(number_of_ingredients)}
            # ingredients = cook_book_file.readline().strip().split(" | ")
            # for i in ingredients:
            i = 0
            # ingredients_list = []
            super_ingrediet_listt = []
            while i < number_of_ingredients:
                ingredients_list = cook_book_file.readline().strip().split(" | ")
                ingredients_dict = {'ingredient_name': ingredients_list[0], 'quantity': ingredients_list[1], 'measure':ingredients_list[2]}
                super_ingrediet_listt.append(ingredients_dict)
                cook_book[name] = super_ingrediet_listt
                # ingredients_list.append(cook_book_file.readline().strip().split(" | "))
                i +=  1
            # print(cook_book)
            # print(ingredients_list)
            next(cook_book_file)
    except StopIteration:
        # print(cook_book)
        for key, value in cook_book.items():
            print("{0}: {1}".format(key, value))

            # next(cook_book_file)
# d = {a: a ** 2 for a in range(7)}


