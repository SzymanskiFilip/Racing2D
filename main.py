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
BLUE = (0,0,255)
GREEN = (0,255,0)

RES = (1000,720)
carX = 1280//2
carY = 600

#font and time counter
pygame.font.init()
font = pygame.font.SysFont('Consolas',30)
time = 0


#locations of the squares spawn

DISPLAY = pygame.display.set_mode((RES))
pygame.display.set_caption("RACING 2D")

CAR_IMG = pygame.image.load("CAR.png")
CAR = pygame.transform.scale(CAR_IMG, (70,70))

def get_random_rect():
    x = random.randint(10, 1000)
    rect = pygame.Rect(x,20,70,20)
    return rect

def move_obstacles(rect1, rect2, rect3, rect4,rect5):
    rect1.y += 10
    rect2.y += 7
    rect3.y += 13
    rect4.y += 5
    rect5.y += 11

def collided():
    DISPLAY.fill(RED)


rect1 = get_random_rect()
rect2 = get_random_rect()
rect3 = get_random_rect()
rect4 = get_random_rect()
rect5 = get_random_rect()

collided = False

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
        carX -= 10
    if keys_pressed[pygame.K_RIGHT]:
        carX += 10

    if rect1.y > 800:
        rect1 = get_random_rect()
    if rect2.y > 800:
        rect2 = get_random_rect()
    if rect3.y > 800:
        rect3 = get_random_rect()
    if rect4.y > 800:
        rect4 = get_random_rect()
    if rect5.y > 800:
        rect5 = get_random_rect()


    DISPLAY.fill(STREET_COLOR)
    DISPLAY.blit(CAR, (carX, carY))
    time = pygame.time.get_ticks()//100
    time_score = font.render("POINTS: " + str(time), True, (255,255,255))

    move_obstacles(rect1,rect2,rect3,rect4,rect5)

    if carX == rect1.x and carY == rect1.y:
        print("collided with white rect")


    pygame.draw.rect(DISPLAY, WHITE, rect1)
    pygame.draw.rect(DISPLAY, RED, rect2)
    pygame.draw.rect(DISPLAY, GREEN, rect3)
    pygame.draw.rect(DISPLAY, BLUE, rect4)
    pygame.draw.rect(DISPLAY, BLACK, rect5)
    DISPLAY.blit(time_score, (10,10))



    pygame.display.update()
