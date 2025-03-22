import random
from art import logo
print(logo)

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
TURNS = 0

# function to check users' guess against actual answer
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

# Function to set difficulty
def set_difficulty():
    level = (input("Choose a difficulty. Type 'easy' or 'hard': ").lower())
    if level == "easy":
       return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


# game_over = False
def game():
    # generates mystery number that player has to guess correctly
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number between 1 and 100.")
    mystery_num = random.randint(1,100)


    turns = set_difficulty()

    # repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != mystery_num:
        print(f"You have {turns} attempts remaining to guess the number. ")
        # let player guess a number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, mystery_num, turns)
        if turns == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            return
        elif gues != mystery_num:
            print("Guess again")
game()

# track the number of turns and reduce by 1 if they get it wrong







# easy or hard determine the number lives the player gets
# level_decision = False
# while level_decision is False:
#     if difficulty == "easy":
#         lives = 10
#         level_decision = True
#     elif difficulty == "hard":
#         lives = 5
#         level_decision = True
#     else:
#         print("Invalid input. Please try again.")
#         difficulty = (input("Welcome to the Number Guessing Game! "
#                             "I'm thinking of a number between 1 and 100."
#                             "Choose a difficulty. Type 'easy' or 'hard': ").lower())
# # game will loop until the player is out of attempts or wins the game
# while game_over is False:
#     if lives != 0:
#         guess = int(input(f"You have {lives} attempts remaining to guess the number. "
#                             "Make a guess: "))
#         if guess < mystery_num:
#             print("Too Low")
#             print("Guess again")
#             lives -= 1
#         elif guess > mystery_num:
#             print("Too High")
#             print("Guess again")
#             lives -= 1
#         elif guess == mystery_num:
#             print(f"You got it! The answer was {mystery_num}.")
#             game_over = True
#     else:
#         print("You've run out of guesses. Refresh the page to run again.")
#         game_over = True
#
#
#
