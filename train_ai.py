import os
import neat
import pygame
from flappy_bird import FlappyBird
import pickle


GENERATIONS = 50
CHECK_POINT_SAVE = 5


def train_ai(genomes, neural_network):
    clock = pygame.time.Clock()
    fb_game = FlappyBird(len(genomes))
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        pipe_index = 0
        if len(fb_game.birds) > 0:
            if len(fb_game.pipes) > 1 and fb_game.birds[0].x > fb_game.pipes[0].x + fb_game.pipes[0].img_top.get_width():
                pipe_index = 1

        for i, bird in enumerate(fb_game.birds):
            genomes[i].fitness += 0.1
            bird.move()

            output = neural_network[fb_game.birds.index(bird)].activate((bird.y,
                                                                         abs(bird.y - fb_game.pipes[pipe_index].height),
                                                                         abs(bird.y - fb_game.pipes[pipe_index].bottom)))

            if output[0] > 0.5:
                bird.jump()

        pipes_to_remove = []
        add_pipe = False
        for pipe in fb_game.pipes:
            pipe.move()
            for bird in fb_game.birds:
                index = fb_game.birds.index(bird)
                if pipe.collide(bird):
                    genomes[index].fitness -= 1
                    neural_network.pop(index)
                    genomes.pop(index)
                    fb_game.birds.pop(index)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.img_top.get_width() < 0:
                pipes_to_remove.append(pipe)

        if add_pipe:
            fb_game.new_pipe()
            for genome in genomes:
                genome.fitness += 5

        for pipe in pipes_to_remove:
            fb_game.pipes.remove(pipe)

        for bird in fb_game.birds:
            if bird.check_ground_collision(fb_game.base):
                index = fb_game.birds.index(bird)
                genomes.pop(index)
                neural_network.pop(index)
                fb_game.birds.pop(index)

        fb_game.draw()
        fb_game.base.move()
        pygame.display.update()

        if len(fb_game.birds) == 0:
            break

        # break if score gets large enough
        '''if score > 20:
            pickle.dump(nets[0],open("best.pickle", "wb"))
            break'''


def evaluation_genomes(genomes, config):
    neural_network = []
    gnomes_list = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        neural_network.append(neat.nn.FeedForwardNetwork.create(genome, config))
        gnomes_list.append(genome)

    train_ai(gnomes_list, neural_network)


def run_neat(path_config):

    config = neat.Config(neat.DefaultGenome,
                         neat.DefaultReproduction,
                         neat.DefaultSpeciesSet,
                         neat.DefaultStagnation,
                         path_config)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    statistics_reporter = neat.StatisticsReporter()
    population.add_reporter(statistics_reporter)
    # Salva o estado e permite reiniciar o algoritimo em um determinado ponto, em numero de gerações.
    population.add_reporter(neat.Checkpointer(CHECK_POINT_SAVE))

    winner = population.run(evaluation_genomes, GENERATIONS)

    # salva o melhor modelo
    with open("best.pickle", "wb") as file:
        pickle.dump(winner, file)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.ini")
    run_neat(config_path)
