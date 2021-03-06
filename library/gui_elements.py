import gui

button = gui.Button(
	x=200,
	y=200,
	width=265,
	height=40,
	text="Text",
	text_size=30,
	text_color=[20, 20, 20],
	font="arial",
	background_color=[200, 200, 200],
	hover_color=[210, 210, 210],
	click_color=[180, 180, 180],
	border_color=[[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 0]],
	border_width=[2, 2, 2, 2]
)

input_box = gui.InputBox(
	x=500,
	y=200,
	width=150,
	height=30,
	initial_text="",
	placeholder="type here...",
	text_size=24,
	placeholder_color=[100, 100, 100],
	text_color=[20, 20, 20],
	font="arial",
	background_color=[200, 200, 200],
	hover_color=[210, 210, 210],
	click_color=[180, 180, 180],
	border_color=[[20, 20, 20], [20, 20, 20], [20, 20, 20], [20, 20, 20]],
	border_width=[1, 1, 1, 1]
)