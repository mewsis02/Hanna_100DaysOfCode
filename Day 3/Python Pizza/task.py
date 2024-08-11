
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? Small (S), Medium (M) or Large (L): ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0
if size == "small" or size == "s":
    bill = 15
    if pepperoni == "y":
        bill += 2
elif size == "medium" or size == "m":
    bill = 20
    if pepperoni == "y":
        bill += 3
elif size == "large" or size == "l":
    bill = 25
    if pepperoni == "y":
        bill += 3

if extra_cheese == "y" and bill != 0:
    bill += 1

print("")
if bill != 0:
    print("Your request has been accepted.")
    print(f"You must pay ${bill} for that pizza.")
else:
    print("Sorry, but we do not carry that pizza!")
