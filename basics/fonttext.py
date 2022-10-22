import pygame, sys
from pygame.locals import *

#Initializing the Setting 
pygame.init()
display = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World')

#Creating Colors
WHITE = (255,255,255)
Green = (0,255,0)
Blue = (0,0,128)

#Choosing the fonts
fontObj = pygame.font.Font('freesansbold.ttf', 32)

#format goes .render('Your text', yes or no, )
textSurfaceObj = fontObj.render('Hello world!', True, Green, Blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

#Creating the Main loop
while True:
    display.fill(WHITE)
    display.blit(textSurfaceObj, textRectObj)    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


