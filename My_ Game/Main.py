import pygame as pg
import random
from Player import Player
from Point import Point
from Ball import Ball

pg.mixer.init()
sound = pg.mixer.Sound('point_mp.mp3')

High = [20, 740]
vector = [-5, -4, -2, 2, 4, 5]
time = 60
score = 0
clock = pg.time.Clock()

pg.init()
pg.font.init()
font = pg.font.SysFont("None", 80)
font_died = pg.font.SysFont("None", 160)
font_died_cont = pg.font.SysFont("None", 100)
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
        if point.rect.x > 250 and point.rect.x < 750 and point.rect.y > 175 and point.rect.x < 150 or point.rect.x > 400 and point.rect.x < 600 and point.rect.y > 500 and point.rect.x < 525 or point.rect.x > 100 and point.rect.x < 125 and point.rect.y > 350 and point.rect.x < 700 or point.rect.x > 100 and point.rect.x < 125 and point.rect.y > 875 and point.rect.x < 900 or point.rect.x > 0 and point.rect.x < 200 and point.rect.y > 0 and point.rect.x < 100 or point.rect.x > 750 and point.rect.x < 1000 and point.rect.y > 0 and point.rect.x < 100:
            points = pg.sprite.Group()

        screen.blit(back_ground, (0, 0))
        if player.HP == 3:
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
            sound.play()

        pg.display.update()
    else:
        for event in pg.event.get():
            screen.blit(back_groundD, (0, 0))
            if event.type == pg.QUIT:
                run = False
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            life = True
            score = 0
            player.HP = 3
            player.rect.x = 500
            player.rect.y = 400
        text_score = font_died.render(F"Score: {score}", False, (184, 134, 11))
        text_continue = font_died_cont.render(F"to continue press (Space)", False, "white")
        screen.blit(text_continue, (75, 50))
        screen.blit(text_score, (300, 600))
        pg.display.update()
