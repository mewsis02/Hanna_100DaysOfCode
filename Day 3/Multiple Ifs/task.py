
print("Welcome to the rollercoaster!")
height = int(input("\nWhat is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("\nWhat is your age? "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7.")
    else:
        bill = 12
        print("Adult Tickets are $12.")
    want_photos = input("\nWould you like a photo? Yes/No? ").lower()
    if want_photos == "yes":
        bill += 3
    print(f"\nYou must pay ${bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")
