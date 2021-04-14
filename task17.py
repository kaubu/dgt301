class EggOrder:
	def __init__(self, name: str, num_eggs: int):
		self.name = name
		self.num_eggs = num_eggs
		self.PRICE_PER_DOZEN = 6.5 # Constant
	
	def calc_price(self) -> int: return (self.num_eggs / 12.0) * self.PRICE_PER_DOZEN
	def format_money(self, d: float) -> str: return f"${d:.2f}"
	def __str__(self) -> str: return f"{self.name} ordered {self.num_eggs} eggs. The price is {self.format_money(self.calc_price())}."

class DailyOrder:
	def __init__(self, day: str, egg_orders: list):
		self.day = day
		self.egg_orders = egg_orders
	
	def get_orders(self):
		"""
		Collects order information - name, number of eggs – in a loop
		"""
		print("Collecting orders...")
		name = ""
		while name.upper() != "F":
			name = input("What is your customer's name? (Type \"F\" to finish)\n>> ")
			if name.upper() != "F":
				egg_orders.append(EggOrder(name, self.read_int(f"How many eggs does {name} wish to order?\n>> ")))

	def show_orders(self):
		"""
		Calculates price for each egg order, and displays order information - name, number of eggs, price
		"""
		print("Showing orders...")
		for egg_order in self.egg_orders:
			print(egg_order)
	
	def show_report(self):
		if len(self.egg_orders) == 0: print("No orders.")
		else:
			total_eggs = 0
			for egg_order in self.egg_orders: # Get index i through list
				total_eggs += egg_order.num_eggs
			
			print(f"""Summary:
Total eggs: {total_eggs}
Dozens required: {self.get_dozens(total_eggs)}""")

			average = 0
			if len(self.egg_orders) > 0: average = total_eggs / len(self.egg_orders) # If there is at least one egg order, assign the total amount of eggs divided by the amount of egg orders to get the average
			print(f"Average number of eggs per customer: {average:.1f}")

	def get_dozens(self, num_eggs: int) -> int:
		"""
		Returns whole number of dozens required to meet required number of eggs
		"""
		num_dozens = num_eggs // 12
		if num_eggs % 12 != 0: num_dozens += 1 # If num_eggs is not divisible by 12, add one to num_dozens
		return num_dozens

	def read_int(prompt: int) -> int:
		while True:
			try:
				choice = int(input(prompt))
				break
			except ValueError:
				print("Not a valid integer!")
		return choice

# Main
if __name__ == "__main__":
	a = EggOrder("bob", 18)
	print(f"{a.calc_price()}")
	b = EggOrder("alice", 27)
	c = EggOrder("michael", 7)
	d = DailyOrder("Monday", [a, b, c])
	d.show_orders()
	d.show_report()
