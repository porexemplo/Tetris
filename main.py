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
    pg.time.set_timer(UPDATE, 1000//(9*FPS), loops=1)
    C_FRAME = 0

    while 1:    # Main game loop
        clock.tick(FPS)
        C_FRAME = C_FRAME%FPS + 5
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.KEYDOWN:
                if event.key in [pg.K_LEFT, pg.K_a]:
                    if grid.can_move_left(): grid.move_left()
                if event.key in [pg.K_RIGHT, pg.K_d]:
                    if grid.can_move_right(): grid.move_right()
            if event.type == GAME_OVER:
                SCREEN.blit(GAME_OVER_SCREEN, (0, 0))
                pg.display.update()
                while True:
                    clock.tick(FPS)
                    for event in pg.event.get():
                        if event.type == pg.QUIT: return
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_r: return main()
                            if event.key == pg.K_q: return pg.QUIT
                
        if C_FRAME == FPS:
            grid.update()
        update_window()
        grid.set_border()
        grid.draw(SCREEN)
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()