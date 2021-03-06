import json
from os.path import realpath

def generate_element(name, params):
	# gets the element's parameters from design.json
	params_str = ""
	for param, value in params.items():
		if param == "type":
			continue

		params_str += f"\n\t{param}={value},"

	# returns the new element with the formated parameter list
	params_str = params_str[:-1] + "\n"
	return f"\n\n{name} = gui.{params['type']}({params_str})"

def generate_elements(gui_elems_name):
	path = realpath(__file__).split("\\")
	path.pop(-1)
	path = '\\'.join(path)
	print(path)
	# opens design.json
	with open(path + "\\design.json", "r") as file:
		data = json.load(file)

	# creates gui_elements.py
	with open(path + "\\" + gui_elems_name, "w") as file:
		file.write("import gui") # first line is the import statement

		# creates all the elements declared in design.json	
		for name, params in data.items():
			text = generate_element(name, params)
			file.write(text)

if __name__ == "__main__":
	generate_elements("gui_elements.py")