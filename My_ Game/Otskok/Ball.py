import pygame as pg

class Ball(pg.sprite.Sprite):
    def __init__(self, x, y, xm, ym):
        super().__init__()
        self.image = pg.image.load('texture/Ball.png')
        self.rect = self.image.get_rect(center=(x, y))
        self.vectorx = xm
        self.vectory = ym

    def update(self):
        self.rect.x += self.vectorx
        self.rect.y += self.vectory
        if self.rect.x < 0:
            self.vectorx = -self.vectorx
        if self.rect.x > 960:
            self.vectorx = -self.vectorx
        if self.rect.y < 0:
            self.vectory = -self.vectory
        if self.rect.y > 760:
            self.vectory = -self.vectory