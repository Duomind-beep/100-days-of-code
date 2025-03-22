print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

starting_point = "You are back on the island shore."
death_by_injury = "You have died from your injuries. Game Over."
death_by_expose = "You have died from exposure. Game Over."
death_by_hunger = "You have died from exposure. Game Over."
yes = "y" or "Y" or "yes" or "Yes"
no = "n" or "N" or "no" or "No"
inventory = 0
cave_entrance = "You find a dark cave. A cold air breathes out and you shiver to the core."

print("You are shipwrecked and have washed up on a island.")
# this determines if the player goes to collect supplies or goes to the cave unprepared
first_choice = input("Do you swim back to the wreckage to fine survivors and supplies, or Explore the Island? Type swim or explore: ")
if first_choice == "swim" or "Swim":
    print("You find no survivors. But you do find a sword, bandages, a torch, and two apples. You swim back to shore soaking wet.")
    inventory = 1

print("You explore the explore the island. You find a dark cave. A cold air breathes out and you shiver to the core.")
print("You enter the cave slowly")
if inventory != "empty":
     print("You see a bear in front of you. It is ready to attack.")
else:
     print("You push more and more in the cave as it swallow you in darkness.")
     print("You are attacked by creature that you cannot see.")


fight_bear = input("Do you fight the creature? Y or N? ")
if fight_bear == yes and inventory != "empty":
    print("You slay the bear!")
    fur_coat = input("The bear's body lays before you. Do you stop to collect from its body? Y or N? ")
    if fur_coat == yes:
        inventory +=1
        print("You have skinned the bear for its fun made it your coat. It keeps you warm despite your still damp clothes")

print("You continue on into the dungeon.")
first_door = input("You find a wooden door. There is a ghostly wail behind it. Do you open it? Y or N? ")
if first_door == yes:
    print("You open the door to find an undead skeleton wielding a mace. It's about to attack")
    if inventory == 2:
            print("You slay the undead. Beyond the piles of bone you find a treasure chest.")
            print("You Win!")
    else:
                print("The Undead Skeleton blows an icy cold breath towards your bare skin.")
                print(death_by_expose)
else:
        print("You continue on and fall down a trap hole.")
        print(death_by_injury)


