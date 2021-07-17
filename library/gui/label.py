from gui.gui_element import *

class Label(GuiElement):
	#############################
	######## Constructor ########
	#############################

	def __init__(self, x, y, text, text_size, text_color, font):
		super().__init__(x, y, 0, 0)
		self._font = font
		self._text = text
		self._text_color = text_color
		self.text_size = text_size # updates everything by calling text_size.setter()

	############################
	######## Properties ########
	############################

	@property
	def text(self):
		return self._text

	@property
	def text_size(self):
		return self._text_size

	@property
	def text_color(self):
		return self._text_color
	
	@property
	def font(self):
		return self._font

	@text.setter
	def text(self, value):
		self._text = value
		self._render_text = self._render_font.render(self.text, True, self.text_color)

	@text_size.setter
	def text_size(self, value):
		self._text_size = value
		self._render_font = pygame.font.SysFont(self.font, self.text_size)
		self._render_text = self._render_font.render(self.text, True, self.text_color)

	@text_color.setter
	def text_color(self, value):
		self._text_color = value
		self._render_text = self._render_font.render(self.text, True, self.text_color)

	@font.setter
	def font(self, value):
		self._font = value
		self._render_font = pygame.font.SysFont(self.font, self.text_size)
		self._render_text = self._render_font.render(self.text, True, self.text_color)

	#########################
	######## Methods ########
	#########################

	def render(self, window):
		window.blit(self._render_text, (self.x, self.y))