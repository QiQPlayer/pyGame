import pygame as pg
import random
from Player import Player
from Ball import Ball
from Point import Point

High = [20, 740]
vector = [-5, -4, -2, 2, 4, 5]
time = 60
score = 0
clock = pg.time.Clock()

pg.init()
pg.font.init()
font = pg.font.SysFont("None", 80)
font_died = pg.font.SysFont("None", 160)
points = pg.sprite.Group()
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
        if len(points) == 0:
            point = Point(random.randint(20, 980), random.randint(20, 780))
            points.add(point)

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
        points.draw(screen)
        text_hp = font.render(F"Hp: {player.HP}", False, (collor))
        text_score = font.render(F"Score: {score}", False, (184, 134, 11))
        screen.blit(text_score, (760, 5))
        screen.blit(text_hp, (30, 5))
        if pg.sprite.spritecollide(player, Balls, False):
            player.HP -= 1
            Balls = pg.sprite.Group()
        if pg.sprite.spritecollide(player, points, False):
            score += 1
            points = pg.sprite.Group()
        pg.display.update()
    else:
        for event in pg.event.get():
            screen.blit(back_groundD, (0, 0))
            if event.type == pg.QUIT:
                run = False
            text_score = font_died.render(F"Score: {score}", False, (184, 134, 11))
            screen.blit(text_score, (300, 600))
        pg.display.update()