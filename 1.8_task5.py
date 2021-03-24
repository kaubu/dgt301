import datetime

class Person:
	def __init__(self, name, birth_year, is_male: bool):
		self.name = name
		self.birth_year = birth_year
		self.is_male = is_male
	
	def get_age(self, this_year):
		"""
		>>> p = Person("Timothy", 1967, True)
		>>> p.get_age(2013)
		46
		"""
		age = this_year - self.birth_year
		return age
	
	def print_info(self):
		now = datetime.datetime.now()
		this_year = now.year
		gender_dict = {"gender": "Male" if self.is_male else "Female", "pronoun": "He" if self.is_male else "She"}
		print(f"{self.name} will be {self.get_age(this_year)} this year. {gender_dict['pronoun']} is {gender_dict['gender']}.")

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	person1 = Person("Joe", 2000, True)
	person2 = Person("Freda", 1990, False)
	person1.print_info()
	person2.print_info()
