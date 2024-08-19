
# Number Guessing Project
import art, random
print(art.logo)

print("Welcome To Hanna Guesses!")
print("In this game, You will guess a number between 1 and 100,")
difficulty = input("but first, would you like to play easy, normal or hard? ").lower()
starting_num_of_guesses = 0

if difficulty == "easy":
    starting_num_of_guesses = 9
elif difficulty == "normal":
    starting_num_of_guesses = 7
elif difficulty == "hard":
    starting_num_of_guesses = 5
else:
    starting_num_of_guesses = 9
    print("I will assume you want to play easy mode.")
print(f"You get {starting_num_of_guesses} attempts to mess around with!")

keepGuessing = True
lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
num_of_guesses = starting_num_of_guesses

while keepGuessing:
    print("")
    print(f"You have {num_of_guesses} attempts to guess the random number.")
    guess = int(input(f"Please give me a guess between {lowest_number}-{highest_number}: "))
    num_of_guesses -= 1
    if guess > answer:
        print("Too high. Please guess again.")
        if not guess > highest_number:
            highest_number = guess
    elif guess < answer:
        print("Too low. Please guess again.")
        if not guess < lowest_number:
            lowest_number = guess
    elif guess == answer:
        print(f"You guessed the answer of {answer} in {starting_num_of_guesses - num_of_guesses} attempts!")
        keepGuessing = False
    elif num_of_guesses == 0:
        print(f"The correct answer was {answer}.")
        keepGuessing = False
