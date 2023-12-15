import random
import copy


def pretty_print(mas):
    """ Displays the list in an easy-to-understand form.
    :param mas: list containing numerical values of cells of the playing field
    :type: list
    :return: list, displayed in an easy-to-understand format
    """
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):  # определяет номер ячейки по ее индексам
    """ Determines the cell number by its indices.
    :param i: number of the row in which cell is located
    :param j: number of the column in which cell is located
    :type: int
    :return: cell number
    :rtype: int
    """
    return i * 4 + j + 1


def get_index_from_number(num):  # определяет индексы ячейки по ее номеру
    """ Defines cell indices by cell number.
    :param num: cell number of the playing field
    :type: int
    :return: cell indices (number of the row and column in which it is located)
    :rtype: int
    """
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_empty_list(mas):  # составляет список с номерами пустых ячеек
    """ Generates a list of empty cell numbers.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return: list of empty cell numbers
    :rtype: list
    """
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):  # вставляем в ячейку по ее индексу 2 (вероятность 90%) и 4 (вероятность 10%)
    """ With 90% probability the function inserts 2 into an list cell and with 10% probability it inserts 4.
    :param mas: list containing numerical values of cells of the playing field
    :param x: list row number (x cell coordinate)
    :param y: list column number (y cell coordinate)
    :type mas: list
    :type x: int
    :type y: int
    :return: mas, whose cell with coordinates x and y now has a new value
    :rtype: list
    """
    if random.random() <= 0.9:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def move_left(mas):  # движение влево
    """ Shifts all list cells to the left.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return mas: list, with cells shifted to the left
    :return delta: the number of points the player will get after making this move
    :return mas != origin: check whether the position of the cells has changed
    :rtype mas: list
    :rtype delta: int
    :rtype mas != origin: bool
    """
    origin = copy.deepcopy(mas)
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
    return mas, delta, mas != origin


def move_right(mas):  # движение вправо
    """ Shifts all list cells to the right.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return mas: list, with cells shifted to the right
    :return delta: the number of points the player will get after making this move
    :return mas != origin: check whether the position of the cells has changed
    :rtype mas: list
    :rtype delta: int
    :rtype mas != origin: bool
    """
    origin = copy.deepcopy(mas)
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
    return mas, delta, mas != origin


def move_up(mas):  # движение вверх
    """ Shifts all list cells upwards.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return mas: list, with cells shifted up
    :return delta: the number of points the player will get after making this move
    :return mas != origin: check whether the position of the cells has changed
    :rtype mas: list
    :rtype delta: int
    :rtype mas != origin: bool
    """
    origin = copy.deepcopy(mas)
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
    return mas, delta, mas != origin


def move_down(mas):  # движение вниз
    """ Shifts all list cells down.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return mas: list, with cells shifted down
    :return delta: the number of points the player will get after making this move
    :return mas != origin: check whether the position of the cells has changed
    :rtype mas: list
    :rtype delta: int
    :rtype mas != origin: bool
    """
    origin = copy.deepcopy(mas)
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
    return mas, delta, mas != origin


def can_move(mas):  # проверка на то, возможно ли совершить одно из предыдущих четырех действий
    """ Checking whether one of the previous four actions can be performed.
    :param mas: list containing numerical values of cells of the playing field
    :type mas: list
    :return: the answer to the question of whether one of the previous four actions can be performed
    :rtype: bool
    """
    for i in range(4):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1]:
                return True
    for i in range(3):
        for j in range(4):
            if mas[i][j] == mas[i + 1][j]:
                return True
    return False



