with open("cookbook.txt", "r", encoding="UTF-8") as cook_book:
    for num_line, line in enumerate(cook_book):
        # print(num_line)
        # print(line)
        line = line.strip()
        # cook_book_dict = {}

        # if line.find(" | ") == -1:
        if " | " not in line:
            # print(line)
            # print(line.strip().split(" | "))
            # line.isdigit()
            if line and line.splitlines():
                print(line)
                if not line.isdigit():
                    cook_book_dict = {line: []}
        print(cook_book_dict)
        # if line in " | ":
        #     print(line)
#         # print(line)
#         print(line.strip().split(" | "))
#         # print(line.split("|"))
#     cook_book_dict = {}
#     while True:
#         name = cook_book.readline().strip()
#         number_of_ingredients = int(cook_book.readline().strip())
#         # print(name)
#         # print(number_of_ingredients)
#         # cook_book_dict = {name: [cook_book.readline().strip().split(" | ")] for a in range(number_of_ingredients)}
#         # ingredients = cook_book.readline().strip().split(" | ")
#         # for i in ingredients:
#         i = 0
#         ingredients_list = []
#         while i < number_of_ingredients:
#             ingredients_list.append(cook_book.readline().strip().split(" | "))
#             i +=  1
#         print(ingredients_list)
#
#         if next(cook_book) == 'StopIteration':
#             break
#     # print(cook_book_dict)
#
#             # next(cook_book)
# # d = {a: a ** 2 for a in range(7)}