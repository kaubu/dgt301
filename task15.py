class ComboOrder:
	def __init__(self, burger, drink, size="medium"):
		self.burger = burger
		self.drink = drink
		self.drink_size = size
		self.chips = size
	
	def display_order(self):
		print(f"""Burger: {self.burger}
Drink: {self.drink_size} {self.drink}
Chips: {self.chips}
""")

if __name__ == "__main__":
	order1 = ComboOrder("cheese", "cola")
	order2 = ComboOrder("lamb", "lemonade", "large")
	order1.display_order()
	order2.display_order()
