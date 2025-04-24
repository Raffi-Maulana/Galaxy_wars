import pygame
import random
import sys
from pygame.locals import *

pygame.init()
#screen set
SCREENWIDTH = 288
SCREENHEIGHT = 512
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), pygame.FULLSCREEN)


#Load images
background_img = pygame.image.load("background.png")
player_img = pygame.image.load("airplane.png").convert_alpha()

FramePerSecond = pygame.time.Clock()

#Game loop
running = True
while running:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	
	screen.blit(background_img, (0,0))
	screen.blit(player_img, (0,0))
	pygame.display.flip()
	
	FramePerSecond.tick(60)

pygame.quit()
sys.exit()