import pygame as pg
import os
from structs import Cell, Grid
from settings import *


def init_window():
    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by Redwane')


def main():
    pg.init()
    init_window()

    while 1:    # Main game loop
        for event in pg.event.get():
            if event.type == pg.QUIT: return


if __name__ == '__main__':
    main()
    pg.quit()