import pygame as pg
import os
from structs import Cell, Grid
from settings import *


grid = Grid()


def draw_bounds():
    for i in range(H_BOUND):
        grid.get_cell(0, i).set_content(bg_square)
        grid.get_cell(W_BOUND, i).set_content(bg_square)

    for i in range(W_BOUND):
        grid.get_cell(i, H_BOUND).set_content(bg_square)        


def init_window():
    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by YummyBread')
    
    SCREEN.fill(BLACK)
    # pg.display.update()


def main():
    pg.init()
    init_window()
    grid.render()

    while 1:    # Main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT: return


if __name__ == '__main__':
    main()
    pg.quit()