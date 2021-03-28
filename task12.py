class Actor:
	def __init__(self): self.gender = "Male"
	def set_female(self): self.gender = "Female"
	def show_gender(self): print(f"This actor's gender is {self.gender}")

if __name__ == "__main__":
	actors = []
	
	for i in range(1, 36):
		actor = Actor()
		if i % 5 == 0 and i != 0: # If i is not 0, and is divisible by 5
			actor.set_female()
		actors.append(actor)
	
	for actor in actors:
		actor.show_gender()
