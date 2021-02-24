import sys
import pygame
from pygame import draw
from pygame.locals import *
from pygame.time import Clock
from field import *

clock = Clock()

pygame.init()

size = 512, 512
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

field = Field(10, 10)
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    i+=1
    screen.fill(black)
    field.set_value(Point(i, 1), FieldState.SNAKE)
    field.render(screen)
    pygame.display.update()

    clock.tick(60)


