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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

First_step = (input("Do you want to go left or go right? (Left/Right)")).capitalize()
if First_step == "Left":
  print("You are in the right way.")
else:
  print("You fall into a hole and die.")
  exit()
Second_step = (input("You see a flooding river and do you want to swim or wait? (Swim/Wait)")).capitalize()
if Second_step == "Wait":
  print("After 30mins, you see a boat and you use it to cross the river.")
else:
  print("You get attacked by trout and you die.")
  exit()
Third_step = (input("You see 3 doors one yellow, one red and one blue. Which one do you choose? (Yellow/Red/Blue)")).capitalize()
if Third_step == "Yellow":
  print("You find a treasure chest and you win. Congrat!")
else:
  if Third_step == "Red":
    print("You are burned by fire and you die.")
    exit()
  elif Third_step == "Blue":
    print("You are eaten by beasts and you die.")
    exit()
  else:
    print("You did not choose any door and a zombie came out and killed you.")
    exit()