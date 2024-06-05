from typing import Any
import pygame
from settings import *
from random import choice, randint

class Background(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        background_img = pygame.image.load('sprites/background-day.png').convert()
        background_img = pygame.transform.scale(background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        self.image = pygame.Surface((WINDOW_WIDTH*2, WINDOW_HEIGHT))
        self.image.blit(background_img, (0,0))
        self.image.blit(background_img, (WINDOW_WIDTH, 0))
        
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 30 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)