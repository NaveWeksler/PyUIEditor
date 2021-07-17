import json

# opens design.json
with open("design.json", "r") as file:
	data = json.load(file)

# creates gui_elements.py
with open("gui_elements.py", "w") as file:
	file.write("import gui") # first line is the import statement

	# creates all the elements declared in design.json	
	for name, params in data.items():
		# gets the element's parameters from design.json
		params_str = ""
		for param, value in params.items():
			if param == "type":
				continue

			params_str += f"\n\t{param}={value},"

		# writes the parameters to gui_elements.py
		params_str = params_str[:-1] + "\n"
		text = f"\n\n{name} = gui.{params['type']}({params_str})"
		file.write(text)