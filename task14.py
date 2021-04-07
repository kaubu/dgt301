class Rectangle:
	"""
	The __init__ method for the rectangle class is defined in terms of its x and y position resting on a
	2-dimensional plane and the parameters: width, height and scale have default values.
	By default it is a unit rectangle
	"""
	def __init__(self, pos_x, pos_y, width = 1, height = 1, scale = 1):
		"""
		>>> r = Rectangle(0,0)
		>>> r = Rectangle(0,0, 2,3)
		>>> r = Rectangle(0,0, scale=5)
		>>> r = Rectangle(1,1,height=5)
		>>> r = Rectangle(1,1, width=5)
		"""
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.width = width * scale
		self.height = height * scale
	
	def move(self, pos_x=1, pos_y=2):
		self.pos_x += pos_x
		self.pos_y += pos_y
	
	def display_position(self):
		"""
		>>> r = Rectangle(0,0)
		>>> r.move(1,2)
		>>> r.display_position()
		x: 1, y: 2
		>>> r.move(1,-1)
		>>> r.display_position()
		x: 2, y: 1
		"""
		print(f"x: {self.pos_x}, y: {self.pos_y}")

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	r = Rectangle(0, 0)
	r.display_position()
	r.move(2, 3)
	r.display_position()
	r.move(-5, 6)
	r.display_position()
