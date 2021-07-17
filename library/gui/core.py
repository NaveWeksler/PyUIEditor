from gui.pygame_input import handle_input

all_elements = []

def update(window, events):
	handle_input(events)

	for element in all_elements:
		element.render(window)

		if hasattr(element, "_on_click") and element.clicked:
			element._on_click()
		if hasattr(element, "_on_down") and element.down:
			element._on_down()
		if hasattr(element, "_on_hover") and element.hovered:
			element._on_hover()