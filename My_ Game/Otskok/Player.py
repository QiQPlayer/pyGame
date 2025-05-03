import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        self.image = pg.image.load('texture/Player.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.HP = hp

    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > 950:
            self.rect.x = 950
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > 750:
            self.rect.y = 750

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= 3
        if keys[pg.K_s]:
            self.rect.y += 3
        if keys[pg.K_d]:
            self.rect.x += 3
        if keys[pg.K_a]:
            self.rect.x -= 3