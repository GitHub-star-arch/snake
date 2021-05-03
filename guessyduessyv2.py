import random

number=int(random.randint(1,100))
chance=int(3)
gc=bool(False)
while (chance!=0 and gc==bool(False)):
    guess1=int(input("You have "+ str(chance) +" lives. Guess a number between 1-100:"))
    if (guess1==number):
        gc=bool(True)
        print("You are great")
    elif (guess1>number):
        print("Try lower.")
    elif (guess1<number):
        print("Try Higher")
    chance=chance-1
if (gc!=bool(True)):
    print("Is that trash I smell oh wait its you.")
input('press enter...')
