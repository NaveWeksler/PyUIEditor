from gui.gui_element import *
from gui.text_block import *

class Button(GuiElement, TextBlock):
	#############################
	######## Constructor ########
	#############################

	def __init__(
			self,
			x,
			y,
			width,
			height,
			text,
			text_size,
			text_color,
			font,
			background_color,
			hover_color,
			border_color,
			border_width
		):
		TextBlock.__init__(self, text, text_size, text_color, font)
		GuiElement.__init__(self, x, y, width, height)

		self._background_color = background_color
		self._hover_color = hover_color
		self._border_color = border_color
		self._border_width = border_width
		self._surface = pygame.Surface((self.width, self.height))

	############################
	######## Properties ########
	############################

	@property
	def surface(self):
		return self._surface

	@property
	def background_color(self):
		return self._background_color

	@property
	def hover_color(self):
		return self._hover_color
	
	@property
	def border_color(self):
		return self._border_color
	
	@property
	def border_width(self):
		return self._border_width
	
	@background_color.setter
	def background_color(self, value):
		self._background_color = value

	@hover_color.setter
	def hover_color(self, value):
		self._hover_color = value

	@border_color.setter
	def border_color(self, value):
		self._border_color = value

	@border_width.setter
	def border_width(self, value):
		self._border_width = value

	@GuiElement.x.setter
	def x(self, value):
		self._x = value

	@GuiElement.y.setter
	def y(self, value):
		self._y = value

	@GuiElement.width.setter
	def width(self, value):
		self._width = value
		self._surface = pygame.transform.scale(self.surface, (self.width, self.height))

	@GuiElement.height.setter
	def height(self, value):
		self._height = value
		self._surface = pygame.transform.scale(self.surface, (self.width, self.height))
	
	#########################
	######## Methods ########
	#########################

	def render(self, window):
		# clears the surface
		background_color = self.hover_color if self.hovered else self.background_color
		self._surface.fill(background_color)

		# text
		text_x = self.width / 2 - TextBlock.width.fget(self) / 2
		text_y = self.height / 2 - TextBlock.height.fget(self) / 2
		TextBlock.render(self, self.surface, text_x, text_y)

		# border
		pygame.draw.rect(self.surface, self.border_color, (0, 0, self.width - 1, self.height - 1), self.border_width)

		# draws the surface to the window
		window.blit(self.surface, (self.x, self.y))