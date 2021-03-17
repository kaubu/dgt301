import sys

def float_check(n) -> float:
	float_num = n

	while True:
		try:
			float_num = float(float_num)
			break
		except:
			print("Please enter a real number!")
			float_num = input()
	
	return float_num

if __name__ == "__main__":
	bids = []
	names = []

	reserve_price = float_check(input("What is the reserve price?\n"))
	print("The auction has started.\nType 'q' to quit the auction.")

	while True:
		if bids or names: print(f"The highest bid so far is ${bids[len(bids)-1]:.2f}")

		name = input("What is your name?\n")
		if name == "q": break
		bid = input("What is your bid?\n")
		if bid == "q": break

		bid = float_check(bid) # One thing that you can't do, is declare a non-integer that isn't q, because then you can no longer exit until you bid.

		# If this is the first iteration OR a bid requested was higher than the current bid
		if (not bids or not names) or (bid > bids[len(bids)-1]):
			names.append(name)
			bids.append(bid)
		# Else if the bid was lower then the current bid
		elif bid <= bids[len(bids)-1]:
			print("You need a higher bid!")
			continue
		
		print("Bid succesful.")
	
	if bids[len(bids)-1] >= reserve_price: print(f"Congratulations {names[len(names)-1]}, you win! Your bid of ${bids[len(bids)-1]:.2f} met the reserve of ${reserve_price:.2f}.")
	else: print(f"Unfortunately the reserve price of ${reserve_price:.2f} was not met, so nobody won the item.")

	print("History of bets:")

	for i in range(0, len(bids)): print(f"{names[i]} bid ${bids[i]:.2f}")
