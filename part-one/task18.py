# Not mine, only modified

import random
class Question:
	""" Authors: Gray, Harper, Garner, Robins; Date: 2 December 2012
	Purpose: This class supports the class Quiz. Instances of this class represent individual
	questions in the quiz, and possible answers, with the correct answer at a random place in
	the list of possible answers (dummies).
	"""
	def __init__(self, question, answer, dummies):
		""" Constructor for instances of Question, sets up the instance variables representing
		the question, and calls self.set_answer to set up the instance variable representing
		the possible answers (including the correct answer).
		"""
		self.question = question
		self.answer = answer
		self.dummies = dummies
		self.set_answers()
	
	def set_answers(self):
		""" Inserts correct answer at random place in the list of possible answers (dummies). """
		self.answers = self.dummies
		self.answers.insert(random.randrange(len(self.dummies) + 1), self.answer)
	
class Quiz:
	""" Authors: Gray, Harper, Garner, Robins; Date: 2 December 2012
	Purpose: This class manages a (text only) multi-choice quiz. It will be extended in future versions with a
	graphical user interface, and access to files of multiple questions and answers. This class is supported by the
	class Question. Instances of Question represent the individual questions (and answers of the quiz). In this
	version of the program there are only two questions. """
	def __init__(self, questions):
		""" Creates a list containing two Question objects by passing the Question constructor
		- a string representing the question
		- a string representing the correct answer
		- a list of strings representing the dummy answers
		"""
		self.questions = questions

		self.questions_correct = 0
		self.num_questions = len(self.questions)

	def take_quiz(self):
		""" This method is the main driver for the quiz. It loops through questions,
		presents each one and its possible answers. It then calls the process_answer method
		passing in a reference to the current question.
		"""
		for q in self.questions: # for each question object in the list of questions
			print( q.question ) # print the question
			for i in range(len(q.answers)): # print the possible answers
				print("\t" + str(i + 1) + ":\t" + q.answers[i])
			print()
			self.process_answer(q) # get answer from user and give appropriate response
		
		self.display_results()

	def process_answer(self, q):
		""" This method reads in the user's answer (should be an int in the range 0 to the number
		of possible answers). It gives an appropriate response to the user's answer.
		The while loop continues until the user inputs an int that is in range. Once they do
		their answer is checked against the correct one to see if it matches.
		Remember input comes in as a string and must be converted to int.
		"""
		user_answer = -1
		# keeps looping until user's input is an int in range
		while not 0 <= user_answer < len(q.answers):
			a = input("Please type the number of your answer here: ")
			try:
				user_answer = int(a) - 1 # if input is not an int we go to the except clause
				if not 0 <= user_answer < len(q.answers):
				# input is not in range no further action is taken (the while loop will repeat)

					print("\nThat was out of range.\n")
				elif user_answer == q.answers.index(q.answer):
				# input is equal to the index of the correct answer (the while loop will end)
					print("\nCorrect!\n")
					self.questions_correct += 1
				else:
				# input not equal to the index of the correct answer (the while loop will end)
					print("\nIncorrect, the answer is " + q.answer + ".\n")

			except ValueError:
				# if user's input is not an int this executes (anticipating errors is good design!)
				print("\nThat was not a sensible input. Integers only please.\n")
	
	def display_results(self):
		percentage_correct = (self.questions_correct / self.num_questions) * 100

		if percentage_correct <= 25: print("Better luck next time!")
		elif percentage_correct <= 50: print("Nice try!")
		elif percentage_correct <= 75: print("Very good!")
		else: print("Congratulations!")

		if percentage_correct % 1 == 0: percentage = f"{percentage_correct:.0f}"
		else: percentage = f"{percentage_correct:.2f}"

		print(f"You scored {self.questions_correct}/{self.num_questions} correct. That means you had an accuracy of {percentage}%.")

#main routine
if __name__ == "__main__":
	test_quiz = Quiz([
		Question("What is the capital of Mongolia?", "Ulan Bator", ["Vladivostok", "Astana","Lhasa"]),
		Question("Who wrote 'The Picture of Dorian Gray?", "Oscar Wilde", ["George Bernard Shaw", "Evelyn Waugh", "Somerset Maugham"]),
		Question("What is the capital of Kenya?", "Nairobi", ["N'Djamena", "Cape Town", "Djibouti"]),
		Question("What programming language was voted \"most-loved\" language on Stack Overflow for 5 years in a row?", "Rust", ["Python", "C++", "Javascript"]),
	])
	
	test_quiz.take_quiz()
