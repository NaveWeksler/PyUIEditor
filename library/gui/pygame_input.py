import pygame

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

class MouseMeta(type):
	#########################
	######## Buttons ########
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
	

class Mouse(metaclass=MouseMeta):
	pass

class KeysMeta(type):
	_keys = {}

	def __call__(cls, char):
		if char in cls._keys:
			return cls._keys[char]
		return Key()

class Keys(metaclass=KeysMeta):
	pass

def handle_input(events):
	for _, key in Keys._keys.items():
		key._pressed = False
		key._released = False

	for event in events:
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