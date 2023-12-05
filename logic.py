import random


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):  # определяет номер ячейки по ее индексам
    return i * 4 + j + 1


def get_index_from_number(num):  # определяет индексы ячейки по ее номеру
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_empty_list(mas):  # составляет список с номерами пустых ячеек
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):  # заполнение ячеек 2 (вероятность 75%) и 4 (вероятность 25%)
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


# def is_zero_in_mas(mas):  # проверяем массив на наличие пустых ячеек
#     for row in mas:
#         if 0 in row:
#             return True
#         else:
#             return False

