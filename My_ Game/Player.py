import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, hp):
        super().__init__()
        self.plar = 1
        self.image = pg.image.load(f'texture/Player{self.plar}.png')
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
        if keys[pg.K_w] and keys[pg.K_d]:
            self.plar = 5
            self.rect.y -= 3
            self.rect.x += 3
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_s] and keys[pg.K_d]:
            self.plar = 8
            self.rect.y += 3
            self.rect.x += 3
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_s] and keys[pg.K_a]:
            self.plar = 7
            self.rect.y += 3
            self.rect.x -= 3
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_w] and keys[pg.K_a]:
            self.plar = 6
            self.rect.y -= 3
            self.rect.x -= 3
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_w]:
            self.rect.y -= 3
            self.plar = 1
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_s]:
            self.rect.y += 3
            self.plar = 3
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_d]:
            self.rect.x += 3
            self.plar = 4
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        elif keys[pg.K_a]:
            self.rect.x -= 3
            self.plar = 2
            self.image = pg.image.load(f'texture/Player{self.plar}.png')
        if self.rect.y <= 175 and self.rect.y >= 170 and self.rect.x <= 749 and self.rect.x >= 201:
            self.rect.y = 176
        if self.rect.y <= 105 and self.rect.y >= 100 and self.rect.x <= 749 and self.rect.x >= 201:
            self.rect.y = 99
        if self.rect.y <= 175 and self.rect.y >= 100 and self.rect.x <= 205 and self.rect.x >= 200:
            self.rect.x = 199
        if self.rect.y <= 175 and self.rect.y >= 100 and self.rect.x <= 750 and self.rect.x >= 745:
            self.rect.x = 751

        if self.rect.y <= 525 and self.rect.y >= 520 and self.rect.x <= 599 and self.rect.x >= 351:
            self.rect.y = 526
        if self.rect.y <= 455 and self.rect.y >= 450 and self.rect.x <= 599 and self.rect.x >= 351:
            self.rect.y = 449
        if self.rect.y <= 525 and self.rect.y >= 450 and self.rect.x <= 355 and self.rect.x >= 350:
            self.rect.x = 349
        if self.rect.y <= 525 and self.rect.y >= 450 and self.rect.x <= 600 and self.rect.x >= 595:
            self.rect.x = 601

        if self.rect.y <= 700 and self.rect.y >= 695 and self.rect.x <= 124 and self.rect.x >= 51:
            self.rect.y = 701
        if self.rect.y <= 305 and self.rect.y >= 300 and self.rect.x <= 124 and self.rect.x >= 51:
            self.rect.y = 299
        if self.rect.y <= 700 and self.rect.y >= 300 and self.rect.x <= 55 and self.rect.x >= 50:
            self.rect.x = 49
        if self.rect.y <= 700 and self.rect.y >= 300 and self.rect.x <= 125 and self.rect.x >= 120:
            self.rect.x = 126

        if self.rect.y <= 700 and self.rect.y >= 695 and self.rect.x <= 899 and self.rect.x >= 821:
            self.rect.y = 701
        if self.rect.y <= 305 and self.rect.y >= 300 and self.rect.x <= 899 and self.rect.x >= 821:
            self.rect.y = 299
        if self.rect.y <= 700 and self.rect.y >= 300 and self.rect.x <= 830 and self.rect.x >= 825:
            self.rect.x = 824
        if self.rect.y <= 700 and self.rect.y >= 300 and self.rect.x <= 900 and self.rect.x >= 895:
            self.rect.x = 901