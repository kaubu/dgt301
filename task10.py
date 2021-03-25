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
	schools = []
	for i in range(5):
		collect_data()
		schools.append(School(school_name, school_pupils, school_classrooms))
	
	for school in schools:
		school.show_info()
	
	# Extension
	lowest_class = None
	for school in schools:
		if not lowest_class:
			lowest_class = school
			continue
		
		if school.calculate_average_pupils() < lowest_class.calculate_average_pupils(): lowest_class = school
	
	print("\nClass with the lowest class size:")
	lowest_class.show_info()
