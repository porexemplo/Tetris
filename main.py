import pygame as pg
import os
from structs import Cell, Grid
from game_data import *


def update_window():
    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by YummyBread')
    
    SCREEN.fill(RGB_BLACK)


def get_user_input(grid):
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        try:
            if grid.can_move_left(): grid.move_left()
        except TypeError: pass

    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        try:
            if grid.can_move_right(): grid.move_right()
        except TypeError: pass
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        grid.update()


def main():
    grid = Grid()
    pg.init()
    clock = pg.time.Clock()
    update_window()
    grid.set_border()
    grid.set_current_shape()
    grid.draw(SCREEN)
    pg.display.update()
    pg.time.set_timer(UPDATE, 10*1000//FPS)

    while 1:    # Main game loop
        clock.tick(FPS)
        get_user_input(grid)
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.KEYDOWN:
                if event.key in [pg.K_p, pg.K_ESCAPE]:
                    SCREEN.blit(PAUSE_SCREEN, (0, 0))
                    pg.display.update()
                    is_paused = True
                    while is_paused:
                        clock.tick(FPS)
                        for event in pg.event.get():
                            if event.type == pg.QUIT: return
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_c: is_paused = False
                                if event.key == pg.K_q: return
                                if event.key == pg.K_r: return main()
            if event.type == UPDATE:
                grid.update()
            if event.type == GAME_OVER:
                SCREEN.blit(GAME_OVER_SCREEN, (0, 0))
                pg.display.update()
                while True:
                    clock.tick(FPS)
                    for event in pg.event.get():
                        if event.type == pg.QUIT: return
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_r: return main()
                            if event.key == pg.K_q: return
        update_window()
        grid.set_border()
        grid.draw(SCREEN)
        pg.display.update()


if __name__ == '__main__':
    main()
    pg.quit()