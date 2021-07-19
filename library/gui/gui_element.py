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

	def __init__(
			self,
			x,
			y,
			width,
			height,
			background_color,
			hover_color,
			border_width,
			border_color
		):
		self._x = x
		self._y = y
		self._width = width
		self._height = height
		self._background_color = background_color
		self._hover_color = hover_color
		self._border_width = border_width
		self._border_color = border_color
		all_elements.append(self)

	############################
	######## Properties ########
	############################

	# x
	#####################################
	@property
	def x(self):
		return self._x
	
	@x.setter
	def x(self, value):
		self._x = value
	#####################################

	# y
	#####################################
	@property
	def y(self):
		return self._y
	
	@y.setter
	def y(self, value):
		self._y = value
	#####################################

	# width
	#####################################
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value
	#####################################

	# height
	#####################################
	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value
	#####################################

	# background_color
	#####################################	
	@property
	def background_color(self):
		return self._background_color

	@background_color.setter
	def background_color(self, value):
		self._background_color = value
	#####################################

	# hover_color
	#####################################	
	@property
	def hover_color(self):
		return self._hover_color

	@hover_color.setter
	def hover_color(self, value):
		self._hover_color = value
	#####################################

	# border_width
	#####################################
	@property
	def border_width(self):
		return self._border_width

	@border_width.setter
	def border_width(self, value):
		self._border_width = value
	#####################################

	# border_color
	#####################################
	@property
	def border_color(self):
		return self._border_color
		
	@border_color.setter
	def border_color(self, value):
		self._border_color = value
	#####################################

	# input
	#####################################
	@property
	def hovered(self):
		return self.x < Mouse.x < self.x + self.width and self.y < Mouse.y < self.y + self.height

	@property
	def clicked(self):
		return Mouse.left.released and self.hovered

	@property
	def down(self):
		return Mouse.left.down and self.hovered
	#####################################

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
		# border
		pygame.draw.rect(window, self.border_color[0], (0, 0, self.border_width[0], self.height)) # left
		pygame.draw.rect(window, self.border_color[1], (0, 0, self.width, self.border_width[1])) # top
		pygame.draw.rect(window, self.border_color[2], (self.width - self.border_width[2], 0, self.border_width[2], self.height)) # right
		pygame.draw.rect(window, self.border_color[3], (0, self.height - self.border_width[3], self.width, self.border_width[3])) # bottom