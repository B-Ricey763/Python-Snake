import sys
import pygame
from pygame import draw
from pygame import display
from pygame.locals import *
from pygame.time import Clock

clock = Clock()

pygame.init()

size = 512, 512
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

field = [[0 for y in range(10)] for x in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[x][y] == 1:

                draw.rect(screen, white, (x*10, y*10, 10, 10))
    pygame.display.update()

    clock.tick(60)


