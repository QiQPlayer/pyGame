import pygame as pg
import random


class Gain(pg.sprite.Sprite):
    def __init__(self, x, y, vid):
        super().__init__()
        self.vids = vid
        self.image = pg.image.load(f'texture/Gain{vid}.png')
        self.rect = self.image.get_rect(center=(x, y))
