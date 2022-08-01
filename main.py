import pygame as pg
import os
from structs import Cell, Grid
from game_data import *


def update_window():
    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by YummyBread')
    
    SCREEN.fill(RGB_BLACK)


def main():
    grid = Grid()
    pg.init()
    clock = pg.time.Clock()
    update_window()
    grid.set_border()
    grid.set_current_shape()
    grid.draw(SCREEN)
    pg.display.update()

    while 1:    # Main game loop
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == GAME_OVER:
                SCREEN.blit(GAME_OVER_SCREEN, (0, 0))
                pg.display.update()
                while True:
                    clock.tick(FPS)
                    for event in pg.event.get():
                        if event.type == pg.QUIT: return
                
        
        grid.update()
        update_window()
        grid.set_border()
        grid.draw(SCREEN)
        pg.display.update()        


if __name__ == '__main__':
    main()
    pg.quit()