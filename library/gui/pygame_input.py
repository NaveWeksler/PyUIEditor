import pygame

class Key:
	def __init__(self):
		self._clicked = False
		self._down = False
		self._released = False

	@property
	def clicked(self):
		return self._clicked
	
	@property
	def down(self):
		return self._down
	
	@property
	def released(self):
		return self._released

class Input:
	_a = Key()
	_b = Key()
	_c = Key()
	_d = Key()
	_e = Key()
	_g = Key()
	_h = Key()
	_i = Key()
	_j = Key()
	_k = Key()
	_l = Key()
	_m = Key()
	_n = Key()
	_o = Key()
	_p = Key()
	_q = Key()
	_r = Key()
	_s = Key()
	_t = Key()
	_u = Key()
	_v = Key()
	_w = Key()
	_x = Key()
	_y = Key()
	_z = Key()

	@property
	def a(self):
		return self._a

	@property
	def b(self):
		return self._b

	@property
	def c(self):
		return self._c
	
	@property
	def d(self):
		return self._d