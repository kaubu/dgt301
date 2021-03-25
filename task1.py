class BasketballPlayer:
	def __init__(self, name, games_played, goals_scored):
		self.name = name
		self.games_played = games_played
		self.goals_scored = goals_scored
	
	def display_average(self):
		"""
		>>> b1 = BasketballPlayer("Karen", 20, 80)
		>>> b1.display_average()
		Player: Karen, Average goals per game: 4.0
		"""
		# average_goals_per_game = goals_scored / games_played
		print(f"Player: {self.name}, Average goals per game: {self.goals_scored / self.games_played}")

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	b2 = BasketballPlayer("Tommy", 25, 60)
	b2.display_average()
	b3 = BasketballPlayer("Maria", 22, 77)
	b3.display_average()
	b4 = BasketballPlayer("Steven", 56, 76)
	b4.display_average()
