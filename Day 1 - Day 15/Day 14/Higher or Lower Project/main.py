
import random, art, game_data

print(art.logo)
GameData = game_data.data
# random.choice(GameData)
choice1 = random.choice(GameData)
choice2 = random.choice(GameData)
while choice2 == choice1:
    choice2 = random.choice(GameData)
score = 0

keepPlaying = True
while keepPlaying:
    who_has_more_followers = ""
    print("")
    print(f"Compare A: {choice1["name"]}, a {choice1["description"]} from {choice1["country"]}")
    print(art.vs)
    print(f"Against B: {choice2["name"]}, a {choice2["description"]} from {choice2["country"]}")
    player_choice = input("Who has more followers? Choose A, or B: ").lower()
    if choice1["follower_count"] > choice2["follower_count"]:
        who_has_more_followers = "a"
    else:
        who_has_more_followers = "b"
    if player_choice == who_has_more_followers:
        score += 1
        print(f"You are correct! Your new score is {score}!")
        choice1 = choice2
        while choice2 == choice1:
            choice2 = random.choice(GameData)
    elif player_choice == "a" or player_choice == "b":
        print(f"I am sorry, but you lost with a score of {score}!")
        keepPlaying = False
    else:
        print("Invalid input. Please try again.")
