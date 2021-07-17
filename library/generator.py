import json

with open("design.json", "r") as file:
	data = json.load(file)

with open("components.py", "w") as file:
	file.write("import gui")

	for name, params in data.items():
		params_str = ""
		for param, value in params.items():
			if param == "type":
				continue

			params_str += f"\n\t{param}={value},"

		params_str = params_str[:-1] + "\n"
		text = f"\n\n{name} = gui.{params['type']}({params_str})"
		file.write(text)