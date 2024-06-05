import pygame, sys, time
from settings import *
from sprites import Background

class Game:
    def __init__(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

    def run(self):
        while True:
            self.display_surf.fill('white')
            self.all_sprites.draw(self.display_surf)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()