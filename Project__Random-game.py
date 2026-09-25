
#    ********** ..... Random Number Game Project ..... **********

import random
target = random.randint(1,50)

while True:
    user_choice = input("Guess any number or Quit(Q) ....")
    if(user_choice == "Q"):
        break
    user_choice =int(user_choice)
    if(user_choice == target):
        print("*** Greatly successful ***: Correct !")
        break
    elif(user_choice > target):
        print("Your Guess is to Large . Guess small number __")
    else:
        print("Your Guess is to Small . Guess large number __")


print("----- Game Over -----")
