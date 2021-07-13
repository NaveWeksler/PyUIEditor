import pygame
import gui

window = pygame.display.set_mode((800, 450))
pygame.display.set_caption("App")
clock = pygame.time.Clock()

label = gui.Label(200, 200, "Text", 30, (240, 20, 20), "comicsansms")
label.text_color = (20, 20, 240)
label.text_size = 20

while True:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			exit()

	window.fill((240, 240, 240))
	gui.update(window, events)
	label.render(window)
	pygame.display.update()
	clock.tick(60)