from flappy_bird import FlappyBird
import pygame


def run_game():
    flappy_bird = FlappyBird()
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        flappy_bird.jump()

        for pipe in flappy_bird.pipes:
            if pipe.collide(flappy_bird.birds[0]):
                return True

        if flappy_bird.birds[0].check_ground_collision(flappy_bird.base):
            return True

        flappy_bird.loop()
        flappy_bird.draw()

        pygame.display.update()


if __name__ == "__main__":
    restart = True
    while restart:
        restart = run_game()
