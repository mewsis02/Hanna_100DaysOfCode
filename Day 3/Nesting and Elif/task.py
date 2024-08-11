
print("Welcome to the rollercoaster!")
height = int(input("\nWhat is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nWhat is your age? "))
    if age < 12:
        print("You must pay $5.")
    elif age <= 18:
        print("You must pay $7.")
    else:
        print("You must pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
