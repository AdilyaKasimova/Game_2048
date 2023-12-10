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
    if random.random() <= 0.9:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def move_left(mas):  # движение влево
    for row in mas:
        while 0 in row:  # сдвиг чисел влево
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):  # слияние равных чисел
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas


def move_right(mas):
    for row in mas:
        while 0 in row:  # сдвиг чисел вправо
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):  # слияние равных чисел
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)
    return mas


def move_up(mas):
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i + 1] and column[i] != 0:
                column[i] *= 2
                column.pop(i + 1)
                column.append(0)
        for i in range(4):  # переворачиваем строку в столбец
            mas[i][j] = column[i]
    return mas


def move_down(mas):
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):  # переворачиваем строку в столбец
            mas[i][j] = column[i]
    return mas


# def is_zero_in_mas(mas):  # проверяем массив на наличие пустых ячеек
#     for row in mas:
#         if 0 in row:
#             return True
#         else:
#             return False
