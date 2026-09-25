
#  1  for snake...
#  -1 for water...
#   0 for gun...

import random
computer = random.choice([1,-1,0])
mystr = input("enter choice :")
mydic = {"s": 1 , "w" : -1 , "g" : 0}
mychoice = mydic[mystr]
reversedic = {1:"snake",-1:"water",0:"gun"}
print(f"you choose {reversedic[mychoice]} ")
print(f"computer choose {reversedic[computer]} ")


if(computer == mychoice):
    print("..Game Draw..")
else:
    if(computer == 1 and mychoice ==-1):
        print("..you Loss")
    elif(computer == 1 and mychoice== 0):
        print("..you Win..")
    elif(computer == -1 and mychoice == 1):
        print("..you Win..")
    elif(computer == -1 and mychoice == 0):
        print("..you Loss..")
    elif(computer == 0 and mychoice == 1):
        print("..you loss..")
    elif(computer == 0 and mychoice == -1):
        print("..you Win..")
    else:
        print("invalid choice")