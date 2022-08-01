import pygame as pg
from screeninfo import get_monitors
import os


SCREEN_WIDTH = get_monitors()[0].width
SCREEN_HEIGHT = get_monitors()[0].height

WIDTH = 0.5*SCREEN_HEIGHT
HEIGHT = 0.6*SCREEN_HEIGHT

SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

W_BOUND_COLUMNS = 12
H_BOUND_COLUMNS = 21


CELL_WIDTH = (.70*WIDTH) // W_BOUND_COLUMNS
CELL_HEIGHT = HEIGHT // H_BOUND_COLUMNS

IMAGE_SET = [
    pg.transform.scale(pg.image.load(os.path.join('assets', 'sq_' + str(i) + '.png')),
        (CELL_WIDTH, CELL_HEIGHT))
        for i in range(0, 7)
]

# Colors
YELLOW  = 0
BLUE    = 1
RED     = 2
PURPLE  = 3
ORANGE  = 4
GREEN   = 5
GREY    = 6

RGB_BLACK = (0, 0, 0)