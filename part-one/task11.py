class Helicopter:
	def __init__(self, number): self.number = number
	def up(self): self.number += 1
	def down(self): self.number -= 1

if __name__ == "__main__":
	helicopters = []
	for i in range(100): helicopters.append(Helicopter(i))

	for i in range(100): 
		if i <= 50:
			helicopters[i].up()
			print(f"{i} up")
		else:
			helicopters[i].down()
			print(f"{i} down")
