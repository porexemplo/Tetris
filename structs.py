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
        self.data = { 'score': 0, 'lines': 0 }
        self.next = {'shape': None, 'content': None}
    
    def set_border(self) -> None:
        for cell in self.cells:
            if cell.y == H_BOUND_COLUMNS-1:
                cell.set_content(GREY); pass
            if (not cell.x) or cell.x == W_BOUND_COLUMNS-1:
                cell.set_content(GREY)
    
    def get_cell(self, x, y) -> Cell:
        if x+y*W_BOUND_COLUMNS > len(self.cells): return None
        return self.cells[x+y*W_BOUND_COLUMNS]

    def fetch_next(self) -> None:
        self.next['shape'] = deepcopy(SHAPES[randint(0, 3)])
        self.next['content'] = randint(0, 5)

    def set_current_shape(self) -> None:
        self.current_shape = deepcopy(self.next.get('shape'))
        self.current_content = self.next.get('content')
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
    
    def line_full(self, y) -> bool:
        for x in range(W_BOUND_COLUMNS):
            if self.get_cell(x, y).is_empty: return False
        return True

    def remove_line(self, y) -> None:
        for x in range(W_BOUND_COLUMNS):
            self.get_cell(x, y).set_content(None)
    
    def shift_down(self, start=0) -> None:
        for y in range(start, 1, -1):
            for x in range(W_BOUND_COLUMNS):
                self.get_cell(x, y).set_content(self.get_cell(x, y-1).content)

    def reset_line(self, y) -> None:
        self.data['lines'] += 1
        self.remove_line(y)
        self.shift_down(start=y)

    def update_score(self, line_count: int) -> None:
        self.data['score'] += SCORE_SHEET[line_count]

    def render_next(self, surface: pg.Surface) -> None:
        surface.blit(SETS_MAP.get(f'set_{SHAPES.index(self.next.get("shape"))}')[self.next.get('content')],
        (
            (W_BOUND_COLUMNS+2)*CELL_WIDTH,
            int(.1*3.5*HEIGHT)
        ))

    def update(self) -> None:
        if self.current_shape is None:
            self.set_current_shape()
            return self.fetch_next()
        if self.can_move_down():
            self.move_cells_down()
        else:
            line_count = 0
            for _, line in self.current_shape:
                if self.line_full(line):
                    line_count += 1
                    self.reset_line(line)
            self.update_score(line_count)
            self.current_shape = None

    def render_text(self, surface: pg.Surface) -> None:
        # Constant text
        for i, text in enumerate(TEXT):
            surface.blit(text, ((W_BOUND_COLUMNS+1)*CELL_WIDTH, int(.1*(.8*i+1)*HEIGHT)))
        
        score_text = FONT.render(str(self.data.get('score')), True, RGB_LIGHT_YELLOW)
        lines_text = FONT.render(str(self.data.get('lines')), True, RGB_LIGHT_YELLOW)

        surface.blit(score_text, ((W_BOUND_COLUMNS+1.2)*CELL_WIDTH, int(.14*HEIGHT)))
        surface.blit(lines_text, ((W_BOUND_COLUMNS+1.2)*CELL_WIDTH, int(.122*1.8*HEIGHT)))

    def draw(self, surface: pg.Surface) -> None:
        for cell in self.cells: cell.render(surface)
        self.render_text(surface)
        self.render_next(surface)