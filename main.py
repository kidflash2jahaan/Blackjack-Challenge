import random

import art

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(player, player_score):
    card = random.choice(deck)
    if card == 11 and player_score + card > 21:
        card = 1

    player.append(card)
    return player_score + card


while True:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() != "y":
        break

    print(art.logo)

    human = []
    computer = []

    human_score = 0
    computer_score = 0

    for i in range(2):
        human_score = deal_card(human, human_score)
        computer_score = deal_card(computer, computer_score)

    while True:
        if human_score > 21:
            break

        print(f"Your cards: {human}, current score: {human_score}")
        print(f"Computer's first card: {computer[0]}")

        if input("Type 'y' to get another card, type 'n' to pass: ").lower() != "y":
            break

        human_score = deal_card(human, human_score)

    while computer_score < 17:
        computer_score = deal_card(computer, computer_score)

    print(f"Your final hand: {human}, final score: {human_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    if human_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif human_score > computer_score:
        print("You win 😃")
    elif human_score == computer_score:
        print("Draw 🙃")
    elif human_score < computer_score:
        print("You lose 😤")
