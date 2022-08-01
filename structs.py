from random import randint
from copy import deepcopy
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
        self.current_content = None
    
    def set_border(self) -> None:
        for cell in self.cells:
            if cell.y == H_BOUND_COLUMNS-1:
                cell.set_content(GREY); pass
            if (not cell.x) or cell.x == W_BOUND_COLUMNS-1:
                cell.set_content(GREY)
    
    def get_cell(self, x, y) -> Cell:
        if x+y*W_BOUND_COLUMNS > len(self.cells): return None
        return self.cells[x+y*W_BOUND_COLUMNS]

    def set_current_shape(self) -> None:
        self.current_shape = deepcopy(SHAPES[randint(0, 3)])
        self.current_content = randint(0, 5)
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(self.current_content)

    def get_lower_cells(self) -> list():
        checked = dict()
        for x, y in self.current_shape:
            if str(x) not in checked:
                checked[str(x)] = y; pass
            checked[str(x)] = max(y, checked[str(x)])
        return [(int(i), j) for i, j in checked.items()]

    def can_move(self) -> bool:
        bellow_cells = [self.get_cell(x, y+1) for x, y in self.get_lower_cells()]
        for cell in bellow_cells:
            if cell == None or not cell.is_empty: return False
        return True
    
    def move_cells(self) -> None:
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(None)
        for i, (x, y) in enumerate(self.current_shape):
            self.get_cell(x, y+1).set_content(self.current_content)
            self.current_shape[i][1] += 1
    
    def update(self) -> None:
        if self.current_shape is None:
            return self.set_current_shape()
        if self.can_move():
            self.move_cells()
        else:
            self.current_shape = None
    
    def draw(self, surface: pg.Surface) -> None:
        for cell in self.cells: cell.render(surface)