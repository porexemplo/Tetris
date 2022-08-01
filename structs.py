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
        Cell(None, x, y) for y in range(H_BOUND_COLUMNS) 
        for x in range(W_BOUND_COLUMNS)
        ]
        self.current_shape = None
    
    def set_border(self) -> None:
        for cell in self.cells:
            if cell.y == H_BOUND_COLUMNS-1:
                cell.set_content(GREY); pass
            if (not cell.x) or cell.x == W_BOUND_COLUMNS-1:
                cell.set_content(GREY)
    
    def get_cell(self, x, y) -> Cell:
        return self.cells[x+y*W_BOUND_COLUMNS]

    def set_current_shape(self) -> None:
        if self.current_shape is not None: return
        self.current_shape = SHAPES[randint(0, 3)]
        temp_content = randint(0, 5)
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(temp_content)
    
    # def update(self) -> None:
    #     if self.can_move(): self.move_cells()
    #     else: self.current_shape = None
    
    def draw(self, surface: pg.Surface) -> None:
        for cell in self.cells: cell.render(surface)