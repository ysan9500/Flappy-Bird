import pygame
from settings import *
from random import choice, randint

class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load('sprites\background-day.png').convert()
        self.rect = self.image.get_rect(topleft = (0,0))