import pygame as pg
from settings import *


class Cell:

    isEmpty: bool = True
    x, y = 0, 0     # Cell coordinates
    fill = pg.Rect(x, y, CELL_WIDTH, CELL_HEIGHT)



    def __init__(self) -> None:
        pass


class Grid:
    def __init__(self, size) -> None:
        pass