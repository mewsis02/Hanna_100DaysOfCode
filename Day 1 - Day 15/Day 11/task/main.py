
import random, art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(art.logo)


def blackjack():
    print("")
    # pull 2 cards for both the player and the computer
    player_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    computer_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
    player_cards_total = player_cards[0] + player_cards[1]
    computer_cards_total = computer_cards[0] + computer_cards[1]

    # Checks if you or computer got Blackjack
    if computer_cards[0] == 11 or computer_cards[1] == 11:
        if computer_cards[0] == 10 or computer_cards[1] == 10:
            return "Computer Got Blackjack! You lost!"
    elif player_cards[0] == 11 or player_cards[1] == 11:
        if player_cards[0] == 10 or player_cards[1] == 10:
            return "You Got Blackjack! You win!"

    # Checks if you have an ace, and determines what the value should be
    if player_cards_total >= 21:
        if player_cards[0] == 11:
            player_cards[0] = 1
        if player_cards[1] == 11:
            player_cards[1] = 1

    # Checks if computer has an ace, and determines what the value should be
    if computer_cards_total >= 21:
        if computer_cards[0] == 11:
            computer_cards[0] = 1
        if computer_cards[1] == 11:
            computer_cards[1] = 1

    pull_more_cards = True
    while pull_more_cards:
        # Gets The Sum Of The Cards in Player & Computer's Possessions
        display_player_cards = ""
        player_cards_total = 0
        for player_card in player_cards:
            display_player_cards += f"{str(player_card)} + "
            player_cards_total += player_card

        # Checks if your score goes over 21
        if player_cards_total > 21:
            return f"\nYour score of {player_cards_total} went over 21, so you lost!"

        new_player_card = 0
        while new_player_card != "yes/no":
            print("")
            print(f"Computer's Hand: {computer_cards[0]}")
            print(f"Player's Hand  : {display_player_cards}")
            new_player_card = input("Pull a new card? Type yay, or nay: ")
            if new_player_card == "yay":
                play_new_card = random.randint(0, 12)
                if cards[play_new_card] == 11 and player_cards_total + 11 > 21:
                    player_cards.append(1)
                else:
                    player_cards.append(cards[play_new_card])
                new_player_card = "yes/no"
                print(f"You pulled a new card with a value of {player_cards[len(player_cards)-1]}!")
            elif new_player_card == "nay":
                new_player_card = "yes/no"
                pull_more_cards = False
            else:
                print("That was an invalid answer.")

    while computer_cards_total < 16:
        computer_cards.append(cards[random.randint(0, 12)])
        computer_cards_total = 0
        for computer_card in computer_cards:
            computer_cards_total += computer_card
    print(f"\nYour score was {player_cards_total}, and the computer score was {computer_cards_total},")
    if computer_cards_total > 21:
        return "and since the computer went over 21, you won!"
    elif player_cards_total > computer_cards_total:
        return "so you win!"
    elif computer_cards_total > player_cards_total:
        return "so you lost!"
    elif player_cards_total == computer_cards_total:
        return "so you ended in a draw!"


keepPlaying = True
while keepPlaying:
    result = blackjack()
    print(result)
    keepPlaying_string = input("Would you like to keep playing? yay or nay: ")
    if keepPlaying_string == "yay":
        keepPlaying = True
    elif keepPlaying_string == "nay":
        print("Goodbye For Now :3")
        keepPlaying = False
    else:
        print("That was an invalid answer, so I will take that as a yes.")
