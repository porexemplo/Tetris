import pygame as pg
import os
from structs import Cell, Grid
from game_data import *


grid = Grid()   


def update_window():
    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by YummyBread')
    
    SCREEN.fill(RGB_BLACK)
    pg.display.update()


def main():
    pg.init()
    update_window()
    grid.set_border()
    grid.draw(SCREEN)
    pg.display.update()

    while 1:    # Main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT: return


if __name__ == '__main__':
    main()
    pg.quit()