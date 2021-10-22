print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input(("What percentage tip would you like to give? 10, 12, or 15? ")))
people = int(input("How many people to split the bill? "))
split = f"Each person should pay: ${round((bill + (tip*bill/100))/people, 2)}"
print(split)
