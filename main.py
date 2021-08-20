import pygame, sys
from pygame.locals import *

pygame.init()
FPS_CAP = 60
tick = pygame.time.Clock()

HD = (1280,720)

DISPLAY = pygame.display.set_mode((HD))
pygame.display.set_caption("RACING 2D")

## game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    print(event)
pygame.display.update()
