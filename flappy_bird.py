import pygame
import os

from bird import Bird
from base import Base
from pipe import Pipe


class FlappyBird:
    WIDTH, HEIGHT = 550, 800
    BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
    pygame.font.init()
    FONT = pygame.font.SysFont("comicsans", 50)

    def __init__(self):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.birds = [Bird(230, 350)]
        self.pipes = [Pipe(600)]
        self.base = Base(730)
        self.clock = pygame.time.Clock()
        self.score = 0

    def draw(self):
        self.window.blit(self.BG_IMG, (0,0))
        self.base.draw(self.window)
        for bird in self.birds:
            bird.draw(self.window)
        for pipe in self.pipes:
            pipe.draw(self.window)
        text = self.FONT.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(text, (self.WIDTH - 10 - text.get_width(), 10))

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.birds[0].jump()

    def loop(self):

        self.clock.tick(30)

        for bird in self.birds:
            bird.move()

        pipes_to_remove = []
        add_pipe = False
        for pipe in self.pipes:
            if pipe.collide(self.birds):
                pass
            if pipe.x + pipe.img_top.get_width() < 0:
                pipes_to_remove.append(pipe)
            if not pipe.passed and pipe.x < self.birds[0].x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            self.score += 1
            self.pipes.append(Pipe(600))

        for pipe in pipes_to_remove:
            self.pipes.remove(pipe)

        self.birds[0].check_ground_collision(self.base)
        self.base.move()
