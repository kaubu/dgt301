class Movie:
	def __init__(self, title, release_year, director, rating, cost, revenue):
		self.title = title
		self.release_year = release_year
		self.director = director
		self.rating = rating
		self.cost = cost
		self.revenue = revenue
	
	def calculate_net_profit(self):
		return self.revenue - self.cost
	
	def display_data(self):
		print(f"""Info for movie: {self.title}
Director: {self.director}
Year released: {self.release_year}
Rating: {self.rating}/5
Cost: ${self.cost:.2f}
Revenue: ${self.revenue:.2f}
Net profit: ${self.calculate_net_profit():.2f}
""")

if __name__ == "__main__":
	m1 = Movie("Attack of the Martians", 2007, "Tom Hall", 4.5, 78000, 125000)
	m1.display_data()
	m2 = Movie("Legends", 2021, "Bryce Lu", 4.7, 7800000, 12000000)
	m2.display_data()
	m3 = Movie("Marshmellow Steve", 2003, "Emily Pelham", 5.0, 5600000, 1000000000)
	m3.display_data()
