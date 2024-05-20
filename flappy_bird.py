import pygame
import os

from bird import Bird

WIDTH, HEIGHT = 550, 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

def draw_game(window, bird):
    window.blit(BG_IMG, (0,0))
    bird.draw(window)
    pygame.display.update()

def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    bird = Bird(200, 100)
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #bird.move()
        draw_game(window, bird)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()