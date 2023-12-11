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


def insert_2_or_4(mas, x, y):  # вставляем в ячейку по ее индексу 2 (вероятность 90%) и 4 (вероятность 10%)
    if random.random() <= 0.9:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def move_left(mas):  # движение влево
    delta = 0
    for row in mas:
        while 0 in row:  # сдвиг чисел влево
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):  # слияние равных чисел
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas, delta


def move_right(mas):  # движение вправо
    delta = 0
    for row in mas:
        while 0 in row:  # сдвиг чисел вправо
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):  # слияние равных чисел
        for j in range(3, 0, -1):
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)
    return mas, delta


def move_up(mas):  # движение вверх
    delta = 0
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
                delta += column[i]
                column.pop(i + 1)
                column.append(0)
        for i in range(4):  # переворачиваем строку в столбец
            mas[i][j] = column[i]
    return mas, delta


def move_down(mas):  # движение вниз
    delta = 0
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
                delta += column[i]
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):  # переворачиваем строку в столбец
            mas[i][j] = column[i]
    return mas, delta


def can_move(mas):  # проверка на то, возможно ли совершить одно из предыдущих четырех действий
    for i in range(3):
        for j in range(3):
            if (mas[i][j] == mas[i + 1][j] and mas[i][j] != 0) or (mas[i][j] == mas[i][j + 1] and mas[i][j] != 0):
                return True
    return False
# def is_zero_in_mas(mas):  # проверяем массив на наличие пустых ячеек
#     for row in mas:
#         if 0 in row:
#             return True
#         else:
#             return False
