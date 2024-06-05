import pygame, sys, time
from settings import *
from sprites import Background, Base, Bird, Pipe

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
        self.base = Base([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.bird = Bird(self.all_sprites, self.scale_factor)

        self.pipe_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.pipe_timer, 1400)
        self.pipes = []

    def collisions(self):
        for pipe in self.pipes:
            if pygame.sprite.collide_mask(self.bird, pipe):
                pygame.quit()
                sys.exit()
        if pygame.sprite.collide_mask(self.bird, self.base):
            pygame.quit()
            sys.exit()

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
                if event.type == self.pipe_timer:
                    self.pipes.append(Pipe([self.all_sprites, self.collision_sprites], self.scale_factor))

            self.display_surf.fill('white')
            self.all_sprites.draw(self.display_surf)
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_surf)

            pygame.display.update()
            self.clock.tick(FRAMERATE)

if __name__ == '__main__':
    game = Game()
    game.run()