from gui.gui_element import *

class Window(GuiElement):
	#############################
	######## Constructor ########
	#############################

	def __init__(self, width, height, title):
		super().__init__(0, 0, width, height)
		self._open = True
		self._clock = pygame.time.Clock()
		self._window = pygame.display.set_mode((width, height))
		self.title = title # calls title.setter()

	############################
	######## Properties ########
	############################

	@property
	def open(self):
		return self._open

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		self._title = value
		pygame.display.set_caption(self.title)

	@GuiElement.width.setter
	def width(self, value):
		self._width = value
		self._window = pygame.display.set_mode((self.width, self.height))

	@GuiElement.height.setter
	def height(self, value):
		self._height = value
		self._window = pygame.display.set_mode((self.width, self.height))
	
	#########################
	######## Methods ########
	#########################

	def update(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self._open = False

		self._window.fill((240, 240, 240))

	def render(self):
		pygame.display.update()
		self._clock.tick(60)