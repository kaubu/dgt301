class House:
	def __init__(self, id: str, address: str, num_bedrooms: int, asking_price: float, area: float):
		self.id = id
		self.address = address
		self.num_bedrooms = num_bedrooms
		self.asking_price = asking_price
		self.area = area

	def calculate_price_per_area(self) -> float:
		return self.asking_price / self.area
	
	def calculate_price_per_room(self) -> float:
		return self.asking_price / self.num_bedrooms
	
	def show_info(self):
		"""
		>>> h = House("DGB2353", "14 Orion Terrace", 2, 595000, 340)
		>>> h.show_info()
		ID: DGB2353
		Address: 14 Orion Terrace
		Number of bedrooms: 2
		Asking price: $595000.00
		"""
		print(f"""ID: {self.id}
Address: {self.address}
Number of bedrooms: {self.num_bedrooms}
Asking price: ${self.asking_price:.2f}""")

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	houses = [
		House("DGB2354", "22 Helens Road", 4, 320000, 250),
		House("DGB2355", "2 Ashton Crescent", 3, 110000, 190),
		House("DGB2356", "5 Stratton St", 5, 550000, 320),
	]

	for house in houses:
		house.show_info()
		print(f"""Price by area: ${house.calculate_price_per_area():.2f}
Price per room: ${house.calculate_price_per_room():.2f}
***********""")
