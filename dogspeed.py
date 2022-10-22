import pygame, sys
from pygame.locals  import*

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
FPS = 30 #Frames per second settings 
fpsClock = pygame.time.Clock()

#Setting up the window 
display = pygame.display.set_mode((1000,1000), 0 ,32)
pygame.display.set_caption('Animation')

#Set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

catImg = pygame.image.load('cat.jpg')
catx=10
caty=10
direction = 'right'

# run the game loop
while True:
    display.fill(WHITE)
    if direction == 'right':
        catx += 5
        if catx == 10:
            direction == 'down' 
    elif direction == 'down':
        caty += 5
        if caty == 10:
            direction = 'left'
    elif direction == 'left':
        catx -=5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -=5
        if caty == 10:
            direction = 'right'

    display.blit(catImg, (catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)