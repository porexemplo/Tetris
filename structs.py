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
            if not self.get_cell(x, y).is_empty:
                pg.event.post(pg.event.Event(GAME_OVER))
                return None
            self.get_cell(x, y).set_content(self.current_content)

    def get_lower_cells(self) -> list():
        checked = dict()
        for x, y in self.current_shape:
            if str(x) not in checked:
                checked[str(x)] = y; pass
            checked[str(x)] = max(y, checked[str(x)])
        return [(int(i), j) for i, j in checked.items()]
    
    def get_right_cells(self) -> list():
        checked = dict()
        for x, y in self.current_shape:
            if str(y) not in checked:
                checked[str(y)] = x; pass
            checked[str(y)] = max(x, checked[str(y)])
        return [(j, int(i)) for i, j in checked.items()]

    def get_left_cells(self) -> list():
        checked = dict()
        for x, y in self.current_shape:
            if str(y) not in checked:
                checked[str(y)] = x; pass
            checked[str(y)] = min(x, checked[str(y)])
        return [(j, int(i)) for i, j in checked.items()]

    def can_move_down(self) -> bool:
        bellow_cells = [self.get_cell(x, y+1) for x, y in self.get_lower_cells()]
        for cell in bellow_cells:
            if cell is None or not cell.is_empty: return False
        return True
    
    def can_move_right(self) -> bool:
        right_cells = [self.get_cell(x+1, y) for x, y in self.get_right_cells()]
        for cell in right_cells:
            if cell is None or not cell.is_empty: return False
        return True

    def can_move_left(self) -> bool:
        left_cells = [self.get_cell(x-1, y) for x, y in self.get_left_cells()]
        for cell in left_cells:
            if cell is None or not cell.is_empty: return False
        return True
    
    def move_cells_down(self) -> None:
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(None)
        for i, (x, y) in enumerate(self.current_shape):
            self.get_cell(x, y+1).set_content(self.current_content)
            self.current_shape[i][1] += 1
    
    def move_left(self) -> None:
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(None)
        for i, (x, y) in enumerate(self.current_shape):
            self.get_cell(x-1, y).set_content(self.current_content)
            self.current_shape[i][0] -= 1

    def move_right(self) -> None:
        for x, y in self.current_shape:
            self.get_cell(x, y).set_content(None)
        for i, (x, y) in enumerate(self.current_shape):
            self.get_cell(x+1, y).set_content(self.current_content)
            self.current_shape[i][0] += 1
    
    def update(self) -> None:
        if self.current_shape is None:
            return self.set_current_shape()
        if self.can_move_down():
            self.move_cells_down()
        else:
            self.current_shape = None

    def render_text(self, surface: pg.Surface) -> None:
        for i, text in enumerate(TEXT):
            surface.blit(text, ((W_BOUND_COLUMNS+1)*CELL_WIDTH, int(.1*(.8*i+1)*HEIGHT)))

    def draw(self, surface: pg.Surface) -> None:
        for cell in self.cells: cell.render(surface)
        self.render_text(surface)