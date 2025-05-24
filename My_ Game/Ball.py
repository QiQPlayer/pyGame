import pygame as pg

pg.mixer.init()
o = pg.mixer.Sound('otskok.mp3')

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
            o.play()
        if self.rect.x > 960:
            self.vectorx = -self.vectorx
            o.play()
        if self.rect.y < 0:
            self.vectory = -self.vectory
            o.play()
        if self.rect.y > 760:
            self.vectory = -self.vectory
            o.play()

        if self.rect.x >= 215 and self.rect.y >= 110 and self.rect.x <= 748 and self.rect.y <= 150:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 215 and self.rect.y >= 160 and self.rect.x <= 748 and self.rect.y <= 175:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 210 and self.rect.y >= 111 and self.rect.x <= 260and self.rect.y <= 174:
            self.vectorx = -self.vectorx
            o.play()
        if self.rect.x >= 740 and self.rect.y >= 111 and self.rect.x <= 750 and self.rect.y <= 174:
            self.vectorx = -self.vectorx
            o.play()

        if self.rect.x >= 365 and self.rect.y >= 460 and self.rect.x <= 598 and self.rect.y <= 500:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 365 and self.rect.y >= 510 and self.rect.x <= 598 and self.rect.y <= 525:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 360 and self.rect.y >= 461 and self.rect.x <= 410 and self.rect.y <= 524:
            self.vectorx = -self.vectorx
            o.play()
        if self.rect.x >= 590 and self.rect.y >= 461 and self.rect.x <= 600 and self.rect.y <= 524:
            self.vectorx = -self.vectorx
            o.play()

        if self.rect.x >= 65 and self.rect.y >= 310 and self.rect.x <= 123 and self.rect.y <= 340:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 65 and self.rect.y >= 690 and self.rect.x <= 123 and self.rect.y <= 700:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 60 and self.rect.y >= 311 and self.rect.x <= 110 and self.rect.y <= 699:
            self.vectorx = -self.vectorx
            o.play()
        if self.rect.x >= 110 and self.rect.y >= 311 and self.rect.x <= 125 and self.rect.y <= 699:
            self.vectorx = -self.vectorx
            o.play()

        if self.rect.x >= 840 and self.rect.y >= 310 and self.rect.x <= 898 and self.rect.y <= 340:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 840 and self.rect.y >= 690 and self.rect.x <= 898 and self.rect.y <= 700:
            self.vectory = -self.vectory
            o.play()
        if self.rect.x >= 835and self.rect.y >= 311 and self.rect.x <= 885 and self.rect.y <= 699:
            self.vectorx = -self.vectorx
            o.play()
        if self.rect.x >= 885 and self.rect.y >= 311 and self.rect.x <= 900 and self.rect.y <= 699:
            self.vectorx = -self.vectorx
            o.play()