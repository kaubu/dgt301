class Country:
	def __init__(self, name, continent, capital, population, land_area):
		self.name = name
		self.continent = continent
		self.capital = capital
		self.population = population
		self.land_area = land_area
	
	def calculate_population_density(self):
		return int(self.population / self.land_area)
	
	def display_data(self):
		"""
		>>> c1 = Country("Ireland", "Europe", "Dublin", 6399152, 84421)
		>>> c1.display_data()
		Country name: Ireland, continent: Europe, capital: Dublin, population: 6399152, land area: 84421km^2, population_density: 75/km^2
		"""
		print(f"Country name: {self.name}, continent: {self.continent}, capital: {self.capital}, population: {self.population}, land area: {self.land_area}km^2, population_density: {self.calculate_population_density()}/km^2")

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	c1 = Country("New Zealand", "Oceania", "Wellington", 4917000, 268021)
	c1.display_data()
	c1 = Country("Ireland", "Europe", "Dublin", 6399152, 84421)
	c1.display_data()
