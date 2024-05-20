import pygame
import neat
import os
import time
import random

WIDTH, HEIGHT = 600, 800

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pine.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))