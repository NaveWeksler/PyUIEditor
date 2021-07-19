import pygame

class TextBlock:
	#############################
	######## Constructor ########
	#############################

	def __init__(self, text, text_size, text_color, font):
		self._font = font
		self._text = text
		self._text_color = text_color
		self.text_size = text_size # updates everything by calling text_size.setter()

	############################
	######## Properties ########
	############################

	# text
	#####################################
	@property
	def text(self):
		return self._text

	@text.setter
	def text(self, value):
		self._text = value
		self._render_text = self._render_font.render(self.text, True, self.text_color)
	#####################################

	# text_size
	#####################################
	@property
	def text_size(self):
		return self._text_size

	@text_size.setter
	def text_size(self, value):
		self._text_size = value
		self._render_font = pygame.font.SysFont(self.font, self.text_size)
		self._render_text = self._render_font.render(self.text, True, self.text_color)
	#####################################

	# text_color
	#####################################
	@property
	def text_color(self):
		return self._text_color

	@text_color.setter
	def text_color(self, value):
		self._text_color = value
		self._render_text = self._render_font.render(self.text, True, self.text_color)
	#####################################
	
	# font
	#####################################
	@property
	def font(self):
		return self._font

	@font.setter
	def font(self, value):
		self._font = value
		self._render_font = pygame.font.SysFont(self.font, self.text_size)
		self._render_text = self._render_font.render(self.text, True, self.text_color)
	#####################################

	# width
	#####################################
	@property
	def width(self):
		return self._render_text.get_width()
	#####################################

	# height
	#####################################
	@property
	def height(self):
		return self._render_text.get_height()
	#####################################

	#########################
	######## Methods ########
	#########################

	def render(self, window, x, y):
		window.blit(self._render_text, (x, y))