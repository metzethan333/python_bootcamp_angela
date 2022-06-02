# blackjack
############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
import random
import replit
from art import logo

still_playing = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)


def deal_cards(cards):
    return random.choice(cards)


user_cards = []
computer_cards = []

while still_playing:
    for _ in range(2):
        computer_cards.append(deal_cards(cards))
        if sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
    for _ in range(2):
        user_cards.append(deal_cards(cards))


    def more_player_cards(cards):
        more_cards = input(f"Your cards are: {user_cards}. Do you want to draw             another card? y, or n: ")
        if more_cards == "y":
            user_cards.append(random.choice(cards))
        elif calculate_score(cards):

          print(f"The computers first card is {computer_cards[0]}.")
        more_player_cards(cards)
        if sum(user_cards) > 21:
          print("you lose")
          still_playing == False
          print("Your hand is {user_cards}")


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.

    def calculate_score(cards):
        return sum(computer_cards)
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
        if sum(computer_cards) == 21 and len(computer_cards) < 3:
            return 0
            print("The computer got a blackjack")
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
        elif 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards.remove(11)
            user_cards.append(1)


    calculate_score(cards)

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    computer_score = calculate_score(computer_cards)
    user_score = calculate_score(user_cards)
    if computer_score == 21 and user_score == 21:
        print("its a draw.")
        still_playing = False
    elif computer_score > 21:
        print("You won")
        print(f"The computers cards were {computer_cards}. They went over 21.")
        play_again = input("Do you want to play again? Y or n: ")
        if play_again == "y":
            replit.clear()
        elif play_again == "n":
            still_playing == False

# end game here
# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

