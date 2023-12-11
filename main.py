from logic import *
import pygame
import sys
from database import get_best_3, cur

GAMERS_DB = get_best_3()


def draw_top_gamers():
    font_top = pygame.font.SysFont("consolas", 26)  # шрифт для счёта
    font_gamer = pygame.font.SysFont("consolas", 24)
    text_head = font_top.render("Best tries: ", True, COLOR_TOP)
    screen.blit(text_head, (290, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index + 1}. {name}-{score}'
        text_gamer = font_gamer.render(s, True, COLOR_TOP)
        screen.blit(text_gamer, (290, 30 + 20 * index))
        print(index, name, score)


# consolas,franklingothicmedium,microsoftjhenghei
def draw_interface(score, delta=0):  # отрисовка интерфейса с заполнением ячеек числами
    pygame.draw.rect(screen, COLOR_TITLE, TITLE_REC)  # создание титульника
    font = pygame.font.SysFont("consolas", 70)  # шрифт для чисел
    font_score = pygame.font.SysFont("consolas", 40)  # шрифт для счёта
    font_delta = pygame.font.SysFont("consolas", 30)
    text_score = font_score.render("Score: ", True, COLOR_SCORE)  # аргументы = текст, обтекание текста, цвет
    text_score_value = font_score.render(f'{score}', True, COLOR_SCORE)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (155, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_SCORE)
        screen.blit(text_delta, (155, 73))
    pretty_print(mas)
    draw_top_gamers()
    for row in range(BLOCKS):  # создание блоков поля и отображение в них чисел
        for column in range(BLOCKS):
            value = mas[row][column]
            if value == 2 or value == 4:
                text = font.render(f'{value}', True, COLOR_FOR_2_AND_4)
            else:
                text = font.render(f'{value}', True, COLOR_FOR_OTHER)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN  # координата блока по Х
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + HEIGHT_TITLE  # координата блока по Y
            pygame.draw.rect(screen, COLORS_BLOCK[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()  # определение длины и ширины текста
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2 + 4
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
COLOR_FOR_2_AND_4 = COLOR_SCORE = COLOR_TOP = (119, 110, 101)
COLOR_FOR_OTHER = (245, 245, 245)
BLOCKS = 4
SIZE_BLOCK = 110
HEIGHT_TITLE = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + HEIGHT_TITLE
TITLE_REC = pygame.Rect((0, 0, WIDTH, HEIGHT_TITLE))
score = 0

mas[1][3] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

# for gamer in get_best():
#     print(gamer)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")
draw_interface(score)
pygame.display.update()
while get_empty_list(mas) or can_move(mas):  # условия, при которых игра продолжается
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # выход из игры
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:  # процесс игры
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            if get_empty_list(mas):
                empty = get_empty_list(mas)  # вставляем в массив рандомное число (2 или 4)
                random.shuffle(empty)  # (перемешиванием массив)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                draw_interface(score, delta)
                pygame.display.update()
