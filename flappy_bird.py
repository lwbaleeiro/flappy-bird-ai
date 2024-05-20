import pygame
import os

from bird import Bird
from base import Base
from pipe import Pipe

WIDTH, HEIGHT = 550, 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_game(window, bird, base, pipe):
    window.blit(BG_IMG, (0,0))
    base.draw(window)
    bird.draw(window)
    pipe.draw(window)
    pygame.display.update()

def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    bird = Bird(100, 50)
    base = Base(600)
    pipe = Pipe(400)
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #bird.move()
        draw_game(window, bird, base, pipe)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()