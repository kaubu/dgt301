# Not complete yet

from tkinter import *
from tkinter import ttk

calc_switch = False

class top_view:
	def __init__(self, parent):	
		self.result_frame = ttk.Frame(parent)
		
		self.calc_input = ttk.Entry(self.result_frame)
		self.calc_input.insert(0, "0")
		self.calc_input.configure(state="readonly")
		self.calc_input.grid(column=0, row=0)

		self.calc_result = ttk.Label(self.result_frame, text="0")
		self.calc_result.grid(column=1, row=0)

		self.top_frame = ttk.Frame(parent)

		self.ac_button = ttk.Button(self.top_frame, command=lambda i=self.calc_input: clear_input(i), text="AC")
		self.lbracket_button = ttk.Button(self.top_frame, command=lambda i=self.calc_input: append_char(i, "("), text="(")
		self.rbracket_button = ttk.Button(self.top_frame, command=lambda i=self.calc_input: append_char(i, ")"), text=")")
		self.modulus_button = ttk.Button(self.top_frame, command=lambda i=self.calc_input: append_char(i, "%"), text="%")
		self.back_button = ttk.Button(self.top_frame, command=lambda i=self.calc_input: back(i), text="←")

		self.ac_button.grid(column=0, row=1)
		self.lbracket_button.grid(column=1, row=1)
		self.rbracket_button.grid(column=2, row=1)
		self.modulus_button.grid(column=3, row=1)
		self.back_button.grid(column=4, row=1)

		self.result_frame.grid_rowconfigure(0, weight=1)
		self.result_frame.grid_columnconfigure(0, weight=1)
		self.result_frame.grid(row=0, column=0, sticky="nsew")

		self.top_frame.grid_rowconfigure(1, weight=1)
		self.top_frame.grid_columnconfigure(0, weight=1)
		self.top_frame.grid(row=1, column=0, sticky="nsew")

class numbers:
	def __init__(self, parent, calc_input):
		self.number_frame = ttk.Frame(parent)

		# self.seven = ttk.Button(self.number_frame, command=lambda i=calc_input: append_char(i, "7"), text="7")

		# self.seven.grid(row=0, column=0, sticky="nsew")

		element(self.number_frame, calc_input, "7", 0, 0, "nsew")
		element(self.number_frame, calc_input, "8", 0, 1, "nsew")
		element(self.number_frame, calc_input, "9", 0, 2, "nsew")
		element(self.number_frame, calc_input, "4", 1, 0, "nsew")
		element(self.number_frame, calc_input, "5", 1, 1, "nsew")
		element(self.number_frame, calc_input, "6", 1, 2, "nsew")
		element(self.number_frame, calc_input, "1", 2, 0, "nsew")
		element(self.number_frame, calc_input, "2", 2, 1, "nsew")
		element(self.number_frame, calc_input, "3", 2, 2, "nsew")
		element(self.number_frame, calc_input, "0", 3, 0, "nsew")
		element(self.number_frame, calc_input, ".", 3, 1, "nsew")

		self.number_frame.grid(row=0, column=0, sticky="nsew") # Operator in row 1

class operators:
	def __init__(self, parent, calc_input, calc_result):
		self.operator_frame = ttk.Frame(parent)

		element(self.operator_frame, calc_input, "/", 0, 0, "ew")
		element(self.operator_frame, calc_input, "*", 1, 0, "ew")
		element(self.operator_frame, calc_input, "-", 2, 0, "ew")
		element(self.operator_frame, calc_input, "+", 3, 0, "ew")

		eq = ttk.Button(self.operator_frame, command=lambda i=calc_input, j=calc_result: calculate_total(i, j), text="=")
		eq.grid(row=0, column=1, sticky="nsew")

		self.operator_frame.grid_rowconfigure(0, weight=1)
		self.operator_frame.grid(row=0, column=1, sticky="nsew")

class calculator_gui:
	def __init__(self, parent):
		self.main_frame = ttk.Frame(parent)
		self.view = top_view(self.main_frame)
		
		self.button_frame = ttk.Frame(parent)
		self.numbers = numbers(self.button_frame, self.view.calc_input)
		self.operators = operators(self.button_frame, self.view.calc_input, self.view.calc_result)
	
		self.main_frame.grid(row=0, column=0, sticky="nsew")
		self.button_frame.grid(row=1, column=0, sticky="nsew")

def calculate_total(calc_input, calc_result):
	result = eval(calc_input.get())
	calc_result.configure(text=result)

def element(superparent, calc_input, ele, erow, ecolumn, esticky):
	an_element = ttk.Button(superparent, command=lambda i=calc_input: append_char(i, ele), text=ele)
	an_element.grid(row=erow, column=ecolumn, sticky=esticky)

def clear_input(calc_input):
	set_text(calc_input, "0") # Check whenever a button is pressed, and delete this zero

def back(i):
	current_input = i.get()
	if current_input != "0":
		set_text(i, f"{i.get()[:-1]}")
	if i.get() == "":
		set_text(i, "0")

def append_char(obj, text):
	current_input = obj.get()
	if current_input == "0":
		set_text(obj, text)
	else:
		set_text(obj, f"{current_input}{text}")

def set_text(obj, text):
	obj.configure(state="normal")
	obj.delete(0,END)
	obj.insert(0,text)
	obj.configure(state="readonly")

if __name__ == "__main__":
	root = Tk()
	root.title("Simple Calculator")
	root.geometry("380x200")

	ttk.Style().configure("TButton", padding=4, relief="flat")

	gui = calculator_gui(root)

	root.mainloop()
