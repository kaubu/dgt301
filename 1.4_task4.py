class Cellphone:
	def __init__(self, make, model, year, price):
		self.make = make
		self.model = model
		self.year = year
		self.price = price
		self.DEPRECIATION_RATE = 0.67
	
	def depreciated(self, years):
		"""
		>>> p1 = Cellphone("Nokia", "6610", 2002, 400)
		>>> p1.depreciated(9)
		Depreciated value after 9 years: $10.88
		"""
		print(f"Depreciated value after {years} years: ${(self.price * (self.DEPRECIATION_RATE ** years)):.2f}")
	
	def display_data(self):
		"""
		>>> p1 = Cellphone("Nokia", "6610", 2002, 400)
		>>> p1.display_data()
		Make: Nokia, Model: 6610, Year: 2002, Price: $400.00
		"""
		print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price:.2f}")

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	c1 = Cellphone("Samsung", "Galaxy S4", 2013, 560)
	c1.display_data()
	c2 = Cellphone("Oppo", "AX5", 2020, 249)
	c2.display_data()
	c2.depreciated(1)
