import pygame as pg
from screeninfo import get_monitors
import os

SCREEN_HEIGHT = get_monitors()[0].height
SCREEN_WIDTH  = get_monitors()[0].width


def get_shape(shape: int, colour: int):
    path = os.path.join('assets',
                        'shape-' + str(shape),
                        'shape-' + str(shape) + '-' + str(colour) + '.png'
                        )
    return pg.image.load(path)


def main():
    pg.init()

    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by Redwane')

    screen = pg.display.set_mode((.7*SCREEN_HEIGHT, .6*SCREEN_HEIGHT))
    screen.fill((0, 40, 0))

    logo_2 = pg.image.load('logo_2.png')
    # screen.blit(logo_2, (0, 0))
    # screen.blit(logo_2, (100, 100))

    image = pg.image.load('random.png')
    image.set_colorkey((255, 0, 255))
    image.set_alpha(128)
    screen.blit(image, (100, 100))

    # path = os.path.join('assets', 'shape-1', 'shape-1-0.png')
    # shape_1 = pg.image.load(path)
    # screen.blit(shape_1, (200, 200))


    xShape, yShape = 100, 100
    screen.blit(get_shape(3, 0), (xShape, yShape))

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: return None
        if yShape < SCREEN_HEIGHT - 100:
            if xShape < .5*SCREEN_WIDTH: xShape += 1
            yShape += 2
        screen.fill((0, 40, 0))
        screen.blit(get_shape(3, 0), (xShape, yShape))
        pg.display.flip()


if __name__ == '__main__':
    main()