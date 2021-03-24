class OneString:
	def __init__(self):
		self.set_string()
	
	def set_string(self):
		self.my_string = input("Enter a word or sentence. ")
	
	def show_string(self):
		print(f"This object stores {self.my_string}")

if __name__ == "__main__":
	s1 = OneString()
	s2 = OneString()
	s1.show_string()
	s2.show_string()
