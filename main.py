import pygame as pg

def main():
    pg.init()

    logo = pg.image.load('logo.png')
    pg.display.set_icon(logo)
    pg.display.set_caption('Tetris by Redwane')

    pg.display.set_mode((800, 600))

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT: return None


if __name__ == '__main__':
    main()