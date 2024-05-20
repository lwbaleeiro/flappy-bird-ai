import neat
import pygame
from flappy_bird import FlappyBird


def run_game():
    flappy_bird = FlappyBird()
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        flappy_bird.jump()

        flappy_bird.loop()
        flappy_bird.draw()
        pygame.display.update()


if __name__ == "__main__":
    run_game()
