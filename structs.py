from random import randint
import pygame as pg
from game_data import *


class Cell:

    is_empty: bool = True

    def __init__(self, content, x: int, y: int) -> None:
        self.content = content
        if content is not None: self.is_empty = False
        self.x = x
        self.y = y
    

    def render(self, surface: pg.Surface) -> None:
        if self.is_empty: return
        surface.blit(IMAGE_SET[self.content], (CELL_WIDTH*self.x, CELL_HEIGHT*self.y))

    def set_content(self, content) -> None:
        self.content = content
        self.is_empty = True if content is None else False




class Grid:
    def __init__(self) -> None:
        self.cells: list = [
        Cell(None, i, j) for i in range(W_BOUND_COLUMNS)
            for j in range(H_BOUND_COLUMNS)
        ]
        self.current_shape = None
    
    def set_border(self) -> None:
        for cell in self.cells:
            if cell.y == H_BOUND_COLUMNS-1:
                cell.set_content(GREY); pass
            if (not cell.x) or cell.x == W_BOUND_COLUMNS-1:
                cell.set_content(GREY)
    
    def get_cell(self, x, y) -> Cell:
        for i, cell in enumerate(self.cells):
            if cell.x == x and cell.y == y:
                return i

    def set_current_shape(self) -> None:
        if self.current_shape is not None: return
        self.current_shape = SHAPES[randint(0, 3)]
        temp_content = randint(0, 5)
        for coord in self.current_shape:
            self.cells[self.get_cell(coord[0], coord[1])].set_content(temp_content)
    
    def draw(self, surface: pg.Surface) -> None:
        for cell in self.cells: cell.render(surface)