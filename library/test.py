'setup'
#####################################
from gui_elements import *
import pygame
import random

window = pygame.display.set_mode((800, 450))
pygame.display.set_caption("App")
clock = pygame.time.Clock()
#####################################

'testing event listeners'
###### @Ofaspir try to add selector/instance of element .on_click() not genral button

#####################################
@button.on_click
def button_clicked():
	button.x = random.randint(0, window.get_width() - button.width)
	button.y = random.randint(0, window.get_height() - button.height)

@button.on_down
def button_down():
	button.text_color = tuple((color + random.randint(-3, 3)) % 255 for color in button.text_color)

@button.on_hover
def button_hovered():
	button.background_color = tuple((color + random.randint(-3, 3)) % 255 for color in button.background_color)
	button.hover_color = tuple((color + random.randint(-3, 3)) % 255 for color in button.hover_color)
#####################################

'game loop'
#####################################
while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			exit()

	window.fill((240, 240, 240))
	gui.update(window, events)
	pygame.display.update()
	clock.tick(60)
#####################################
