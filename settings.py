import pygame as pg
from screeninfo import get_monitors

SCREEN_HEIGHT = get_monitors()[0].height
SCREEN_WIDTH  = get_monitors()[0].width

HEIGHT = 0.8*SCREEN_HEIGHT
WIDTH = 0.8*SCREEN_HEIGHT

SCREEN = pg.display.set_mode((HEIGHT, WIDTH))

CELL_HEIGHT = HEIGHT // 21
CELL_WIDTH = WIDTH // 20