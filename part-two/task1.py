"""
I apologize for this horrendous code, 
I probably could've coded it better, to get rid of repetition, 
but, it's Tkinter... soo...
"""

from tkinter import *

class Task1RadioButton:
	def __init__(self, parent):
		# verbs = ["pet", "snuggle with", "appreciate", "stroke", "feed", "pick up"]
		# adjectives = ["fluffy", "cute", "adorable", "furry", "soft", "quiet"]

		self.options_frame = Frame(parent)
		
		self.verb_frame = Frame(self.options_frame, relief = GROOVE, borderwidth = 3)
		self.verb_var = StringVar()
		self.verb_var.set("pet")
		self.verb_rb1 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "pet", text = "pet", command=self.change_message)
		self.verb_rb1.pack(anchor=W)
		self.verb_rb2 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "snuggle with", text = "snuggle with", command=self.change_message)
		self.verb_rb2.pack(anchor=W)
		self.verb_rb3 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "appreciate", text = "appreciate", command=self.change_message)
		self.verb_rb3.pack(anchor=W)
		self.verb_rb4 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "stroke", text = "stroke", command=self.change_message)
		self.verb_rb4.pack(anchor=W)
		self.verb_rb5 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "feed", text = "feed", command=self.change_message)
		self.verb_rb5.pack(anchor=W)
		self.verb_rb6 = Radiobutton(self.verb_frame, variable = self.verb_var, value = "pick up", text = "pick up", command=self.change_message)
		self.verb_rb6.pack(anchor=W)

		self.adj_frame = Frame(self.options_frame, relief = GROOVE, borderwidth = 3)
		self.adj_var = StringVar()
		self.adj_var.set("fluffy")
		self.adj_rb1 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "fluffy", text = "fluffy", command=self.change_message)
		self.adj_rb1.pack(anchor=W)
		self.adj_rb2 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "cute", text = "cute", command=self.change_message)
		self.adj_rb2.pack(anchor=W)
		self.adj_rb3 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "adorable", text = "adorable", command=self.change_message)
		self.adj_rb3.pack(anchor=W)
		self.adj_rb4 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "furry", text = "furry", command=self.change_message)
		self.adj_rb4.pack(anchor=W)
		self.adj_rb5 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "soft", text = "soft", command=self.change_message)
		self.adj_rb5.pack(anchor=W)
		self.adj_rb6 = Radiobutton(self.adj_frame, variable = self.adj_var, value = "quiet", text = "quiet", command=self.change_message)
		self.adj_rb6.pack(anchor=W)

		# self.verb_frame.grid(row=0, column=0, sticky=N+S+W)
		# self.adj_frame.grid(row=0, column=1, sticky=N+S+E)
		self.verb_frame.pack(side = LEFT, expand = YES, fill = BOTH)
		self.adj_frame.pack(side = RIGHT, expand = YES, fill = BOTH)
		self.options_frame.pack(side = TOP, expand = YES, fill = BOTH)

		# After everything
		self.message_label = Label(parent)
		self.change_message()
		# self.message_label.grid(row=1, column=0, rowspan=2)
		self.message_label.pack(side = BOTTOM, expand = YES, fill = X)
	
	def change_message(self):
		self.message_label.configure(text = f"I am going to {self.verb_var.get()} the {self.adj_var.get()} cat.")

if __name__ == "__main__":
	root = Tk()
	root.title("Cat descriptions")
	root.geometry("300x180")
	cats = Task1RadioButton(root)
	root.mainloop()
