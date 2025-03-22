import random
from art import logo
from art import vs
from game_data import data



def game():
   score = 0
   game_should_continue = True
   while game_should_continue:
        dict_a = random.choice(data)
        name_a = dict_a['name']
        description_a = dict_a['description']
        country_a = dict_a['country']
        dict_b = random.choice(data)
        name_b = dict_b['name']
        description_b = dict_b['description']
        country_b = dict_b['country']
        followers_a = dict_a['follower_count']
        followers_b = dict_b['follower_count']
        if dict_a == dict_b:
            dict_a = random.choice(data)


        print(f"{logo}Compare A: {name_a}, a {description_a}, from {country_a}")
        print(f"{vs}Compare B: {name_b}, a {description_b}, from {country_b}")
        print(followers_a)
        print(followers_b)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()


        if guess == "A":
            if followers_a > followers_b:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score} ")
                return
        if guess == "B":
            if followers_b > followers_a:
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                print(f"Sorry, that's wrong. Final score: {score} ")
                return

game()