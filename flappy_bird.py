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

    def __init__(self, bird_population=1):
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.birds = []
        self.pipes = [Pipe(600)]
        self.base = Base(730)
        self.clock = pygame.time.Clock()
        self.score = 0

        for _ in range(bird_population):
            self.birds.append(Bird(230, 350))

    def draw(self):
        self.window.blit(self.BG_IMG, (0, 0))
        self.base.draw(self.window)
        for bird in self.birds:
            bird.draw(self.window)
        for pipe in self.pipes:
            pipe.draw(self.window)

        text = self.FONT.render(f"Birds alive: {len(self.birds)}", True, (255, 255, 255))
        text_score = self.FONT.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(text, (self.WIDTH - 10 - text.get_width(), 10))
        self.window.blit(text_score, (self.WIDTH - 10 - text.get_width(), 690))

    def jump(self, single_player=True, bird=None):
        if single_player:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.birds[0].jump()
        elif not single_player and bird:
            bird.jump()

    def loop(self):  # For single player game

        self.clock.tick(30)

        for bird in self.birds:
            bird.move()

        pipes_to_remove = []
        add_pipe = False
        for pipe in self.pipes:
            for bird in self.birds:
                if pipe.collide(bird):
                    pass
                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.img_top.get_width() < 0:
                pipes_to_remove.append(pipe)

            pipe.move()

        if add_pipe:
            self.score += 1
            self.new_pipe()

        for pipe in pipes_to_remove:
            self.pipes.remove(pipe)

        for bird in self.birds:
            if bird.check_ground_collision(self.base):
                self.birds.remove(bird)

        self.base.move()

    def new_pipe(self):
        self.pipes.append(Pipe(600))
