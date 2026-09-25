
#   ***** ..... General Store Calculator ..... *****

sum = 0
while True:
    item = input("item name :: ")

    if(item != "q"  ):
        userInput = input(f"{item}.price  :--> ")
        sum = sum + int(userInput)
    else:
        break