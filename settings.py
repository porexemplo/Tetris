import pygame as pg
from screeninfo import get_monitors

SCREEN_WIDTH  = get_monitors()[0].width
SCREEN_HEIGHT = get_monitors()[0].height

WIDTH = 0.6*SCREEN_HEIGHT
HEIGHT = 0.5*SCREEN_HEIGHT

SCREEN = pg.display.set_mode((HEIGHT, WIDTH))

W_BOUND = 20
H_BOUND = 21

CELL_WIDTH = WIDTH // W_BOUND
CELL_HEIGHT = HEIGHT // W_HEIGHT

# Colors
BLACK = (0, 0, 0)