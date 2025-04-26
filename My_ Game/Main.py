import pygame as pg
import random
from Player import Player
from Ball import Ball

High = [20, 740]
vector = [-5, -4, -2, 2, 4, 5]
time = 60
clock = pg.time.Clock()

pg.init()
pg.font.init()
font = pg.font.SysFont("None", 80)
player = Player(500, 400, 3)
players = pg.sprite.Group(player)
Balls = pg.sprite.Group()

screen = pg.display.set_mode((1000, 800))
back_ground = pg.image.load('texture/Fon.png')
back_groundD = pg.image.load('texture/Died.png')

pg.time.set_timer(pg.USEREVENT, 4000)

run = True
life = True
while run:
    if life:
        clock.tick(time)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.USEREVENT:
                ball = Ball(random.randint(20, 940), random.choice(High), random.choice(vector), random.choice(vector))
                Balls.add(ball)

        if player.HP <= 0:
            life = False

        screen.blit(back_ground, (0, 0))
        collor = 34, 139, 34
        if player.HP == 2:
            collor = 255, 215, 0
        if player.HP == 1:
            collor = 178, 34, 34
        Balls.draw(screen)
        Balls.update()
        players.draw(screen)
        players.update()
        text = font.render(F"Hp: {player.HP}", False, (collor))
        screen.blit(text, (440, 5))
        if pg.sprite.spritecollide(player, Balls, False):
            player.HP -= 1
            Balls = pg.sprite.Group()
        pg.display.update()
    else:
        for event in pg.event.get():
            screen.blit(back_groundD, (0, 0))
            if event.type == pg.QUIT:
                run = False
        pg.display.update()
