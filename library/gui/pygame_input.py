import pygame

#####################
######## Key ########
#####################

class Key:
	def __init__(self):
		self._pressed = False
		self._down = False
		self._released = False

	@property
	def pressed(self):
		return self._pressed
	
	@property
	def down(self):
		return self._down
	
	@property
	def released(self):
		return self._released

##########################
######## Keyboard ########
##########################

class KeysMeta(type):
	_keys = {}

	def __call__(cls, char):
		if char in cls._keys:
			return cls._keys[char]
		return Key()

# allows to access KeysMeta without any instance
class Keys(metaclass=KeysMeta):
	pass

#######################
######## Mouse ########
#######################

class MouseMeta(type):
	#########################
	######## Members ########
	#########################

	_left = Key()
	_middle = Key()
	_right = Key()

	_x = 0
	_y = 0
	_delta_x = 0
	_delta_y = 0

	############################
	######## Properties ########
	############################

	@property
	def left(self):
		return self._left
	
	@property
	def middle(self):
		return self._middle
	
	@property
	def right(self):
		return self._right

	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y
	
	@property
	def delta_x(self):
		return self._delta_x
	
	@property
	def delta_y(self):
		return self._delta_y
	
# allows to access MouseMeta without any instance
class Mouse(metaclass=MouseMeta):
	pass

################################
######## Input Handling ########
################################

def handle_input(events):
	# resets the keys 
	for _, key in Keys._keys.items():
		key._pressed = False
		key._released = False

	# resets the mouse
	Mouse._left._pressed = False
	Mouse._left._released = False;
	Mouse._middle._pressed = False
	Mouse._middle._released = False;
	Mouse._right._pressed = False
	Mouse._right._released = False;

	# mouse position
	Mouse._x, Mouse._y = pygame.mouse.get_pos()
	Mouse._delta_x, Mouse._delta_y = pygame.mouse.get_rel()

	for event in events:
		# keyboard input
		if hasattr(event, "key"):
			if not event.key in Keys._keys:
				Keys._keys[event.key] = Key()
			key = Keys._keys[event.key]		
			if event.type == pygame.KEYDOWN:
				key._pressed = True
				key._down = True
			elif event.type == pygame.KEYUP:
				key._released = True
				key._down = False

		# mouse input
		elif hasattr(event, "button"):
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1: # left pressed
					Mouse._left._pressed = True
					Mouse._left._down = True
				elif event.button == 2: # middle pressed
					Mouse._middle._pressed = True
					Mouse._middle._down = True
				elif event.button == 3: # right pressed
					Mouse._right._pressed = True
					Mouse._right._down = True
			elif event.type == pygame.MOUSEBUTTONUP:
				if event.button == 1: # left released
					Mouse._left._released = True
					Mouse._left._down = False
				elif event.button == 2: # middle pressed
					Mouse._middle._released = True
					Mouse._middle._down = False
				elif event.button == 3: # right pressed
					Mouse._right._released = True
					Mouse._right._down = False