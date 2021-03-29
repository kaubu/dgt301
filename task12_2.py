class Actor:
	def __init__(self): self.gender = "Male"
	def set_female(self): self.gender = "Female"
	def show_gender(self): print(f"This actor's gender is {self.gender}")

if __name__ == "__main__":
	actors = []
	
	for i in range(1, 36): actors.append(Actor())
	
	for i, actor in enumerate(actors):
		print(i)
		if (i + 1) % 5 == 0: actors[i].set_female() # If i is not 0, and is divisible by 5, set gender to female
	
	for actor in actors: actor.show_gender()
