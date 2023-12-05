from logic import *

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

mas[1][3] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

while get_empty_list(mas):  # вставляем в массив рандомное число (2 или 4)
    input()
    empty = get_empty_list(mas)
    random.shuffle(empty)  # перемешиванием массив
    random_num = empty.pop()
    x, y = get_index_from_number(random_num)
    mas = insert_2_or_4(mas, x, y)
    pretty_print(mas)
