import pygame as pg
from screeninfo import get_monitors

SCREEN_HEIGHT = get_monitors()[0].height


def main():
    pg.init()

    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by Redwane')

    pg.display.set_mode((.7*SCREEN_HEIGHT, .6*SCREEN_HEIGHT))

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: return None


if __name__ == '__main__':
    main()