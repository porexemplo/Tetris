import pygame as pg
from screeninfo import get_monitors
import os


# Game Settings
SCREEN_WIDTH = get_monitors()[0].width
SCREEN_HEIGHT = get_monitors()[0].height

WIDTH = 0.5*SCREEN_HEIGHT
HEIGHT = 0.6*SCREEN_HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

W_BOUND_COLUMNS = 12
H_BOUND_COLUMNS = 21

FPS = 17

CELL_WIDTH = (.70*WIDTH) // W_BOUND_COLUMNS
CELL_HEIGHT = HEIGHT // H_BOUND_COLUMNS

# Images
IMAGE_SET = [
    pg.transform.scale(pg.image.load(os.path.join('assets', 'sq_' + str(i) + '.png')),
        (CELL_WIDTH, CELL_HEIGHT))
        for i in range(0, 7)
]

GAME_OVER_SCREEN = pg.transform.scale(pg.image.load(os.path.join('assets', 'game_over.png')),
                   (WIDTH, HEIGHT))

# Events
GAME_OVER = pg.USEREVENT + 1
UPDATE = pg.USEREVENT + 2

# Shapes
SHAPE_L = [
    [5, 0],
    [5, 1],
    [5, 2], [6, 2]
]
SHAPE_O = [
    [5, 0], [6, 0],
    [5, 1], [6, 1]
]
SHAPE_N = [
            [6, 0],
    [5, 1], [6, 1],
    [5, 2]
]
SHAPE_I = [
    [5, 0],
    [5, 1],
    [5, 2],
    [5, 3]
]

SHAPES = [SHAPE_I, SHAPE_L, SHAPE_O, SHAPE_N]

# Colors
YELLOW  = 0
BLUE    = 1
RED     = 2
PURPLE  = 3
ORANGE  = 4
GREEN   = 5
GREY    = 6

RGB_BLACK = (0, 0, 0)
RGB_LIGHT_YELLOW = (253, 255, 146)

# Fonts & Text
pg.font.init()
FONT_SIZE = 23
FONT = pg.font.Font(os.path.join('assets', 'fonts', 'spacemono_regular.ttf'), FONT_SIZE)

SCORE_STR = FONT.render("Score :", True, RGB_LIGHT_YELLOW)
LINES_STR = FONT.render("Lines :", True, RGB_LIGHT_YELLOW)
NEXT_STR = FONT.render("Next :", True, RGB_LIGHT_YELLOW)

SCORE_RECT = SCORE_STR.get_rect()
LINES_RECT = LINES_STR.get_rect()
NEXT_RECT = NEXT_STR.get_rect()

TEXT = [SCORE_STR, LINES_STR, NEXT_STR]