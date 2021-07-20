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
		GuiElement.__init__(self, x, y, width, height, background_color, hover_color, border_width, border_color)

	#########################
	######## Methods ########
	#########################

	def render(self, window):
		# clears the surface
		background_color = self.hover_color if self.hovered else self.background_color
		self.surface.fill(background_color)

		# text
		text_x = self.width / 2 - TextBlock.width.fget(self) / 2
		text_y = self.height / 2 - TextBlock.height.fget(self) / 2
		TextBlock.render(self, self.surface, text_x, text_y)

		# border
		GuiElement.render(self, self.surface)

		# draws the surface to the window
		window.blit(self.surface, (self.x, self.y))