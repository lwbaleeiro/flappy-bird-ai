import pygame
import os
import random


class Pipe:
    PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
    GAP = 200
    VELOCITY = 5

    def __init__(self, x):
        self.x = x
        self.height = 0
        self.top = 0
        self.bottom = 0
        self.img_top = pygame.transform.flip(self.PIPE_IMG, False, True)
        self.img_bottom = self.PIPE_IMG
        self.passed = False
        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.img_top.get_height()
        self.bottom = self.height + self.GAP

    def move(self):
        self.x -= self.VELOCITY

    def draw(self, window):
        window.blit(self.img_top, (self.x, self.top))
        window.blit(self.img_bottom, (self.x, self.bottom))

    def collide(self, birds):
        for bird in birds:
            bird_mask = bird.get_mask()
            top_mask = pygame.mask.from_surface(self.img_top)
            bottom_mask = pygame.mask.from_surface(self.img_bottom)

            top_offset = (self.x - bird.x, self.top - round(bird.y))
            bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

            top_collide_point = bird_mask.overlap(top_mask, top_offset)
            bottom_collide_point = bird_mask.overlap(bottom_mask, bottom_offset)

            if top_collide_point or bottom_collide_point:
                return True
        return False
