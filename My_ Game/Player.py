import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.image.load('texture/Player.png')
        self.rect = self.image.get_rect(center=(x, y))

    def w(self):
        self.rect.y -= 10

    def a(self):
        self.rect.x -= 10

    def s(self):
        self.rect.y += 10

    def d(self):
        self.rect.x += 10

    def update(self):
        self.rect.y -= 5
