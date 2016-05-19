from functools import partial

class Infix(object):
	def __init__(self, func):
		self.func = func
	def __or__(self, other):
		return self.func(other)
	def __ror__(self, other):
		return Infix(partial(self.func, other))
	def __call__(self, v1, v2):
		return self.func(v1, v2)

@Infix
def m(x, y):
	return (x[0]*y[0], x[1]*y[1])