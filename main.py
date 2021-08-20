import pygame, sys
from pygame.locals import *

pygame.init()
FPS_CAP = 60
tick = pygame.time.Clock()

#COLORS
STREET_COLOR = (115, 128, 145)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

HD = (1280,720)
carX = 1280//2
carY = 600

DISPLAY = pygame.display.set_mode((HD))
pygame.display.set_caption("RACING 2D")

CAR_IMG = pygame.image.load("CAR.png")
CAR = pygame.transform.scale(CAR_IMG, (70,70))

## game loop
while True:
    tick.tick(FPS_CAP)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #movement handling
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        print("LEFT")
        carX -= 10
    if keys_pressed[pygame.K_RIGHT]:
        print("RIGHT")
        carX += 10

    DISPLAY.fill(STREET_COLOR)
    DISPLAY.blit(CAR, (carX, carY))
    pygame.display.update()
