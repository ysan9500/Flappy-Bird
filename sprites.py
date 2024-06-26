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
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.pos.x -= 200 * dt
        if self.rect.centerx <= 0:
            self.pos.x = 0
        self.rect.x = round(self.pos.x)

class Bird(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        self.import_frames(scale_factor)
        self.frame_index = 2
        self.image = self.frames[self.frame_index]

        self.rect = self.image.get_rect(midleft = (WINDOW_WIDTH/20,WINDOW_HEIGHT/2))
        self.pos = pygame.math.Vector2(self.rect.topleft)

        self.gravity = 20
        self.direction = -4
        self.flapframe = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.wing_sound = pygame.mixer.Sound('audio\wing.ogg')

    def import_frames(self, scale_factor):
        bluebird_img_1 = pygame.image.load(f'sprites/bluebird-downflap.png').convert_alpha()
        bluebird_img_1 = pygame.transform.scale(bluebird_img_1, pygame.math.Vector2(bluebird_img_1.get_size())*scale_factor)
        bluebird_img_2 = pygame.image.load(f'sprites/bluebird-midflap.png').convert_alpha()
        bluebird_img_2 = pygame.transform.scale(bluebird_img_2, pygame.math.Vector2(bluebird_img_2.get_size())*scale_factor)
        bluebird_img_3 = pygame.image.load(f'sprites/bluebird-upflap.png').convert_alpha()
        bluebird_img_3 = pygame.transform.scale(bluebird_img_3, pygame.math.Vector2(bluebird_img_3.get_size())*scale_factor)
        self.frames = [bluebird_img_1, bluebird_img_2, bluebird_img_3]

    def apply_gravity(self, dt):
        self.direction += self.gravity * dt
        self.pos.y += self.direction
        self.rect.y = round(self.pos.y)

    def flap(self):
        self.wing_sound.play()
        self.direction = -8
        self.flapframe = 4

    def animate(self, dt):
        if self.flapframe > -1:
            self.flapframe -= 5*dt
            if int(self.flapframe) == 4:
                self.image = self.frames[2]
            if int(self.flapframe) == 3:
                self.image = self.frames[1]
            if int(self.flapframe) == 2:
                self.image = self.frames[0]
            if int(self.flapframe) == 1:
                self.image = self.frames[1]
            if int(self.flapframe) == 0:
                self.image = self.frames[2]

    def rotate(self):
        rotated_bird = pygame.transform.rotozoom(self.image, -self.direction, 1)
        self.image = rotated_bird
    def update(self, dt):
        self.apply_gravity(dt)
        self.animate(dt)
        #self.rotate()

class Pipe(pygame.sprite.Sprite):
    def __init__(self, groups, scale_factor):
        super().__init__(groups)
        pipe_img = pygame.image.load('sprites\pipe-green.png').convert_alpha()
        pipe_img = pygame.transform.scale(pipe_img, pygame.math.Vector2(pipe_img.get_size())*scale_factor)
        self.image = pygame.Surface((pipe_img.get_width(), WINDOW_HEIGHT + 100), pygame.SRCALPHA)
        self.image.blit(pipe_img, (0,randint(550, 600)))
        pipe_img = pygame.transform.flip(self.image, False, True)
        self.image.blit(pipe_img, (0,0))
        self.image = self.image.convert_alpha()
        
        x = WINDOW_WIDTH + randint(40, 100)
        y = WINDOW_HEIGHT + randint(0,100)
        self.rect = self.image.get_rect(midbottom = (x,y))
        self.mask = pygame.mask.from_surface(self.image)


        self.pos = pygame.math.Vector2(self.rect.topleft)

    def update(self, dt):
        self.pos.x -= 400 * dt
        self.rect.x = round(self.pos.x)
        if self.rect.right <= -100:
            self.kill()
