#modules imports
from art import logo
import random



def deal_card():
    """Returns a Random Card from the Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return a score calculated from cards"""
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(p_score, d_score):
    if p_score == d_score:
        return "Draw 🙃"
    elif d_score == 0:
        return "Lose, opponent has a Blackjack 😱"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif p_score > 21:
        return "You went over. You lose 😭"
    elif d_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score > d_score:
        return "You win 🙂"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    player_hand = []
    dealer_hand = []
    dealer_score = -1
    player_score = -1
    is_game_over = False

    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Computer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0  or player_score > 21:
            is_game_over = True
        else:
            player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if player_should_deal == "y":
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score {player_score}")
    print(f"Dealer's hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()



# Win Conditions

#

#
# if sum(dealer_hand) and sum(player_hand) == 21:
#     print("Dealer Wins")
#     game_over = False
#
#
# if sum(player_hand) or sum(dealer_hand) > 21:
#     for card in player_hand or dealer_hand:
#         if card == 11:
#             card = 1
#         else:
#             if sum(player_hand) > 21:
#                 print("Dealer Wins")
#                 game_over = False
#             elif sum(dealer_hand) > 21:
#                 print("Player wins")
#                 game_over = False

#
# def end_game():
#     print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
#     if sum(dealer_hand) < 21:
#     if sum(player_hand) > 21:
#         print("You went over. You lose.")
#     if sum(dealer_hand) > 21:
#         print("You Win!")
#     if sum(dealer_hand) == 21:
#         print("Dealer Wins")
#     if sum(dealer_hand) == 21 and sum(player_hand) == 21:
#         print("Dealer wins")
#     if sum(dealer_hand)  < 21:





# # drawing functions
# def player_draw():
#     player_card = random.choice(cards)
#     player_hand.append(player_card)
#     print(f"Your hand: {player_hand}, current score: {sum(player_hand)}")
#     return
#
# def dealer_draw():
#     random_card = random.choice(cards)
#     dealer_hand.append(random_card)
#     return
#
#
# #player's choice of new game or not
# start_game = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ").lower()
# if start_game == "y":
#     print(art.logo)
# # 1st round draws
#     player_draw()
#     player_draw()
#     dealer_draw()
#     dealer_draw()
#
#
#     print(f"Your cards: {player_hand}")
#     print(f"Computer's first card: {dealer_hand[0]}")
#     for card in player_hand
#         if card ==
#
#     while game_over is True:
#
#         hit_or_pass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
#
#         if hit_or_pass == "y":
#             player_draw()
#
#             if sum(player_hand) > 21:
#                 for card in player_hand:
#                     if card == 11:
#                         card = 1
#                     else:
#                         game_over = False
#             elif not game_over:
#                  print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
#
#             print(f"Your cards: {player_hand}")
#             print(f"Computer's first card: {dealer_hand}")
#
#         else:
#             print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
#
#
#
#
# else:
#     game_over = False