
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 5-15? "))
people = int(input("How many people to split the bill? "))

final_bill = bill + (bill * (tip/100))
bill_per_person = final_bill / people
# Rounds bill_per_person to 2 decimal places, even if it ends in .00
# Any questions? https://www.geeksforgeeks.org/how-to-round-floating-value-to-two-decimals-in-python/
bill_per_person = "%.2f" % bill_per_person

print(f"Every person should pay ${bill_per_person}")
