import pygame, sys
from pygame.locals import *
import random

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

#locations of the squares spawn

DISPLAY = pygame.display.set_mode((HD))
pygame.display.set_caption("RACING 2D")

CAR_IMG = pygame.image.load("CAR.png")
CAR = pygame.transform.scale(CAR_IMG, (70,70))

def get_random_rect():
    x = random.randint(10, 1280)
    rect = pygame.Rect(x,20,60,20)
    return rect


rect1 = get_random_rect()
rect2 = get_random_rect()
rect3 = get_random_rect()

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


    pygame.draw.rect(DISPLAY, WHITE, rect1)
    pygame.draw.rect(DISPLAY, WHITE, rect2)
    pygame.draw.rect(DISPLAY, WHITE, rect3)

    pygame.display.update()
