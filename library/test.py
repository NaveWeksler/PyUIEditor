import gui

window = gui.Window(800, 450, "App")
label = gui.Label(200, 200, "Text", 30, (240, 20, 20), "comicsansms", window)
label.text_color = (20, 20, 240)
label.text_size = 20

while window.open:
	window.update()
	label.render(window)
	window.render()