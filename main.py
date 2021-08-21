import pygame, sys
from pygame.locals import *
import random
import time as THREAD_SLEEP

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


rect1 = get_random_rect()
rect2 = get_random_rect()
rect3 = get_random_rect()
rect4 = get_random_rect()
rect5 = get_random_rect()


def check_collision(carX, carY, rect1, rect2,rect3,rect4,rect5,points):
    carX += 35
    if carX >= rect1.x and carX <= rect1.x + 70:
        if rect1.y > 600 and rect1.y < 620:
            print("1")
            paused(points)
    if carX >= rect2.x and carX <= rect2.x + 70:
        if rect2.y > 600 and rect2.y < 620:
            print("2")
            paused(points)
    if carX >= rect3.x and carX <= rect3.x + 70:
        if rect3.y > 600 and rect3.y < 620:
            print("3")
            paused(points)
    if carX >= rect4.x and carX <= rect4.x + 70:
        if rect4.y > 600 and rect4.y < 620:
            print("4")
            paused(points)
    if carX >= rect5.x and carX <= rect5.x + 70:
        if rect5.y > 600 and rect5.y < 620:
            print("5")
            paused(points)

def paused(points):

    DISPLAY.fill(WHITE)

    pause = True
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    quit()

        DISPLAY.fill(RED)
        message = "You got: " + str(points) + " Points. Press Enter to exit."
        text = font.render(message, 1, (WHITE))
        text_rect = text.get_rect(center=(1000//2, 720//2))
        DISPLAY.blit(text, text_rect)

        pygame.display.update()
        tick.tick(10)


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
        if carX > 0:
            carX -= 10
    if keys_pressed[pygame.K_RIGHT]:
        if carX < 1000 - 70:
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
    check_collision(carX, carY, rect1, rect2,rect3,rect4,rect5,time)


    pygame.draw.rect(DISPLAY, WHITE, rect1)
    pygame.draw.rect(DISPLAY, RED, rect2)
    pygame.draw.rect(DISPLAY, GREEN, rect3)
    pygame.draw.rect(DISPLAY, BLUE, rect4)
    pygame.draw.rect(DISPLAY, BLACK, rect5)
    DISPLAY.blit(time_score, (10,10))



    pygame.display.update()
