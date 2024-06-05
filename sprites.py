from typing import Any
import pygame
from settings import *
from random import choice, randint

class Background(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        background_img = pygame.image.load('sprites/background-day.png').convert()
        background_width = background_img.get_width() * scale_factor
        background_height = background_img.get_height() * scale_factor
        background_img = pygame.transform.scale(background_img, (background_width, background_height))
        
        self.image = pygame.Surface((background_width*2, background_height))
        self.image.blit(background_img, (0,0))
        self.image.blit(background_img, (background_width, 0))
        
        self.rect = self.image.get_rect(topleft = (0,0))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 30 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)

class Base(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        base_img = pygame.image.load('sprites/base.png').convert_alpha()
        base_width = base_img.get_width() * scale_factor
        base_height = base_img.get_height() * scale_factor
        base_img = pygame.transform.scale(base_img, (base_width, base_height))
        self.image = pygame.Surface((base_width*2, base_height))
        self.image.blit(base_img, (0,0))
        self.image.blit(base_img, (base_width,0))
        self.rect = self.image.get_rect(bottomleft = (0,WINDOW_HEIGHT + 65))
        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 200 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)
