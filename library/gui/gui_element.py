import pygame

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
	
	#########################
	######## Methods ########
	#########################

	def render(self, window):
		pass