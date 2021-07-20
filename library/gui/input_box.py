from gui.gui_element import *
from gui.text_block import *

class InputBox(GuiElement, TextBlock):
	#############################
	######## Constructor ########
	#############################

	def __init__(
			self,
			x,
			y,
			width,
			height,
			initial_text,
			placeholder,
			text_size,
			text_color,
			placeholder_color,
			font,
			background_color,
			hover_color,
			click_color,
			border_color,
			border_width
		):
		TextBlock.__init__(self, initial_text, text_size, text_color, font)
		GuiElement.__init__(self, x, y, width, height, background_color, hover_color, click_color, border_width, border_color)
		self._placeholder = placeholder
		self._placeholder_color = placeholder_color
		self._focused = False

    ############################
	######## Properties ########
	############################

	# placeholder
	#####################################
	@property
	def placeholder(self):
		return self._placeholder
	
	@placeholder.setter
	def placeholder(self, value):
		self._placeholder = value
	#####################################

    # placeholder_color
	#####################################
	@property
	def placeholder_color(self):
		return self._placeholder_color
	
	@placeholder_color.setter
	def placeholder_color(self, value):
		self._placeholder_color = value
	#####################################

	# focused
	#####################################
	@property
	def focused(self):
		if Mouse.left.pressed:
			self._focused = self.hovered

		return self._focused
	#####################################

	#########################
	######## Methods ########
	#########################

	def render(self, window):
		# clears the surface
		background_color = self.click_color if self.focused else self.background_color
		self.surface.fill(background_color)

		# text
		if self.focused:
			self.text += Keys.text
			if Keys(pygame.K_BACKSPACE).pressed:
				self.text = self.text[:-1]

		text = self.placeholder if self.text == "" else self.text
		color = self.placeholder_color if self.text == "" else self.text_color
		self._render_text = self._render_font.render(text, True, color)
		text_x = self.width / 2 - TextBlock.width.fget(self) / 2
		text_y = self.height / 2 - TextBlock.height.fget(self) / 2
		TextBlock.render(self, self.surface, text_x, text_y)

		# border
		GuiElement.render(self, self.surface)

		# draws the surface to the window
		window.blit(self.surface, (self.x, self.y))