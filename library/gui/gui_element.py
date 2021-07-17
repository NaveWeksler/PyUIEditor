from gui.pygame_input import *
from gui.core import *

class GuiElement:
	#############################
	######## Constructor ########
	#############################

	def __new__(cls, *args, **kwargs):
		if cls is GuiElement:
			raise TypeError("Cannot create an instance of GuiElement")
		return object.__new__(cls)

	def __init__(self, x, y, width, height):
		self._x = x
		self._y = y
		self._width = width
		self._height = height
		all_elements.append(self)

	############################
	######## Properties ########
	############################

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height

	@property
	def hovered(self):
		return self.x < Mouse.x < self.x + self.width and self.y < Mouse.y < self.y + self.height

	@property
	def clicked(self):
		return Mouse.left.released and self.hovered

	@property
	def down(self):
		return Mouse.left.down and self.hovered

	############################
	######## Decorators ########
	############################

	def on_click(self, func):
		self._on_click = func
		return func

	def on_down(self, func):
		self._on_down = func
		return func

	def on_hover(self, func):
		self._on_hover = func
		return func
	
	#########################
	######## Methods ########
	#########################

	def render(self, window):
		pass