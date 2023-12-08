from logic import *
import pygame
import sys


def draw_interface():  # отрисовка интерфейса
    pygame.draw.rect(screen, COLOR_TITLE, TITLE_REC)  # создание титульника
    font = pygame.font.SysFont("clear sans", 70)  # шрифт
    pretty_print(mas)
    for row in range(BLOCKS):  # создание блоков поля и отображение в них чисел
        for column in range(BLOCKS):
            value = mas[row][column]
            if value == 2 or value == 4:
                text = font.render(f'{value}', True, COLOR_FOR_2_AND_4)  # аргументы = текст, обтекание текста, цвет
            else:
                text = font.render(f'{value}', True, COLOR_FOR_OTHER)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN  # координата блока по Х
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + HEIGHT_TITLE  # координата блока по Y
            pygame.draw.rect(screen, COLORS_BLOCK[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()  # определение длины и ширины текста
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

COLORS_BLOCK = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (238, 225, 201),
    8: (243, 178, 122),
    16: (246, 150, 100),
    32: (247, 124, 95),
    64: (247, 95, 59),
    128: (237, 208, 115),
    256: (237, 204, 98),
    512: (237, 201, 80),
    1024: (229, 195, 85),
    2048: (232, 190, 78)
}
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
COLOR_TITLE = (250, 248, 239)
COLOR_MARGIN = (187, 173, 160)
COLOR_FOR_2_AND_4 = (119, 110, 101)
COLOR_FOR_OTHER = (245, 245, 245)
BLOCKS = 4
SIZE_BLOCK = 110
HEIGHT_TITLE = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + HEIGHT_TITLE
TITLE_REC = pygame.Rect((0, 0, WIDTH, HEIGHT_TITLE))

mas[1][3] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
draw_interface()
pygame.display.update()
while get_empty_list(mas):  # вставляем в массив рандомное число (2 или 4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            # input()
            empty = get_empty_list(mas)
            random.shuffle(empty)  # перемешиванием массив
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)
            draw_interface()
            pygame.display.update()
