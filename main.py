import pygame, sys, time
from settings import *
from sprites import Background, Base, Bird

class Game:
    def __init__(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        self.favicon = pygame.image.load('favicon.ico').convert()
        pygame.display.set_icon(self.favicon)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        background_width = pygame.image.load('sprites/background-day.png').get_width()
        self.scale_factor = WINDOW_WIDTH / background_width

        Background(self.all_sprites, self.scale_factor)
        Base(self.all_sprites, self.scale_factor)
        self.bird = Bird(self.all_sprites, self.scale_factor)

    def run(self):
        last_time = time.time()
        while True:
            dt = time.time() - last_time
            last_time =  time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.bird.flap()

            self.display_surf.fill('white')
            self.all_sprites.draw(self.display_surf)
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surf)

            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()