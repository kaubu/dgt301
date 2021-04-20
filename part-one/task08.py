class TeamSport:
	def __init__(self):
		self.store_info()
	
	def store_info(self):
		self.sport_name = input("What is the name of a team sport? ")
		self.num_players = int(input(f"How many players in a {self.sport_name} team? "))
	
	def show_info(self):
		options = ["a team sport.", "not a team sport."]
		print(f"{self.sport_name} is {options[0] if self.num_players > 1 else options[1]}")
		print(f"There are {self.num_players} players in a {self.sport_name} team.")

if __name__ == "__main__":
	ts1 = TeamSport()
	ts2 = TeamSport()
	ts1.show_info()
	ts2.show_info()
