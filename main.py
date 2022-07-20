import pygame as pg
from screeninfo import get_monitors

SCREEN_HEIGHT = get_monitors()[0].height


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

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: return None
        pg.display.flip()


if __name__ == '__main__':
    main()