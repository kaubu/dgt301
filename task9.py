class School:
	def __init__(self, name, num_pupils, num_classrooms):
		self.name = name
		self.num_pupils = num_pupils
		self.num_classrooms = num_classrooms
	
	def calculate_average_pupils(self):
		return self.num_pupils / self.num_classrooms
	
	def show_info(self):
		"""
		>>> s = School("Eveyln Intermediate", 96, 1500)
		>>> s.show_info()
		Eveyln Intermediate has 15.62 pupils per room
		"""
		print(f"{self.name} has {self.calculate_average_pupils():.2f} pupils per room")

def collect_data():
	global school_name, school_pupils, school_classrooms
	school_name = input("Enter the name of the school: ")
	while True:
		try:
			school_pupils = int(input("Enter the number of pupils the school has: "))
			break
		except ValueError:
			print("Please enter an integer!")
	while True:
		try:
			school_classrooms = int(input("Enter the number of classrooms the school has: "))
			break
		except ValueError:
			print("Please enter an integer!")

if __name__ == "__main__":
	collect_data()
	school1 = School(school_name, school_pupils, school_classrooms)
	school1.show_info()
	collect_data()
	school2 = School(school_name, school_pupils, school_classrooms)
	school2.show_info()
