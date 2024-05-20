import pygame
import os

from bird import Bird
from base import Base
from pipe import Pipe

WIDTH, HEIGHT = 550, 800
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
pygame.font.init()
FONT = pygame.font.SysFont("comicsans", 50)

def show_infos(window, score):
    text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(text, (WIDTH - 10 - text.get_width(), 10))

def draw_game(window, bird, base, pipes):
    window.blit(BG_IMG, (0,0))
    base.draw(window)
    bird.draw(window)
    for pipe in pipes:
        pipe.draw(window)
    
def main():
    score = 0
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    bird = Bird(230, 350)
    base = Base(730)
    pipes = [Pipe(600)]
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bird.jump()

        bird.move()
        pipes_to_remove = []
        add_pipe = False
        for pipe in pipes:
            if pipe.collide(bird):
                pass
            if pipe.x + pipe.img_top.get_width() < 0:
                pipes_to_remove.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
            pipe.move()

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))

        for pipe in pipes_to_remove:
            pipes.remove(pipe)
        
        bird.check_ground_collision(base)
        base.move()
        draw_game(window, bird, base, pipes)
        show_infos(window, score)

        pygame.display.update()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()