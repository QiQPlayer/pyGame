import pygame as pg
import random
from Player import Player

time = 60
clock = pg.time.Clock()
pg.init()
player = Player(500, 400)
all_sprite = pg.sprite.Group(player)

screen = pg.display.set_mode((1000, 800))
back_ground = pg.image.load('texture/Fon.png')
back_groundD = pg.image.load('texture/Died.png')

run = True
life = True
while run:
    if life:
        clock.tick(time)
        for event in pg.event.get():
            screen.blit(back_ground, (0, 0))
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            Player.w
        all_sprite.draw(screen)
        all_sprite.update()
        pg.display.update()
    else:
        for event in pg.event.get():
            screen.blit(back_groundD, (0, 0))
            if event.type == pg.QUIT:
                run = False
        pg.display.update()
