bids = []
names = []
bid = 0.00
name = ""

def float_check(msg) -> float:
	while True:
		try:
			float_input = input(msg)
			if float_input == "q":
				break
			float_input = float(float_input)
			break
		except:
			print("Please enter an real number!")
	
	return float_input

reserve_price = float_check("What is the reserve price?\n")
print("The auction has started.\nType 'q' to quit the auction.")

while name != "q" and bid != "q":
	if bids or names:
		print(f"The highest bid so far is ${bids[len(bids)-1]:.2f}")

	name = input("What is your name?\n")
	bid = float_check("What is your bid?\n")

	if name != "q" or bid != "q":
		if bids or names:
			if bid > bids[len(bids)-1]:
				names.append(name)
				bids.append(bid)
				print("Bid succesful.")
			else:
				print("You need a higher bid!")
		else:
			names.append(name)
			bids.append(bid)
			print("Bid succesful.")

if bids[len(bids)-1] >= reserve_price:
	print(f"Congratulations {names[len(names)-1]}, you win! Your bid of ${bids[len(bids)-1]:.2f} met the reserve of ${reserve_price:.2f}.")
else:
	print("Unfortunately the reserve price was not met, so nobody one the item.")

print("History of bets:")

for i in range(0, len(bids)):
	print(f"{names[i]} bid ${bids[i]:.2f}")