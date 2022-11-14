guessWho = 0
blackHair = 0
living = 0
pinkHair = 0
destruction = 0

def function():

    print("Your character choices are Rimuru, Shizu, Hinata, Milim, and Shuna")
    guessWho = input("Is your characters hair blue? (y/n): ")
    if guessWho == 'y':
        print("your character is Rimuru")
    elif guessWho == 'n':
        blackHair = input("Is your characters hair black? (y/n): ")
        if blackHair == 'y':
            living = input("Is your character alive?: (y/n)")
            if living == 'y':
                print("Your character is Hinata")
            else:
                print("Your character is Shizu")
        elif  blackHair == 'n':
            pinkHair = input("Does your character have pink hair? (y/n): ")
            if pinkHair == 'y':
                destruction = input("Does your character go on random quests of mass destruction and act like they're a child?: (y/n)")
            if destruction == 'y':
                print("your character is Milim")
            else:
                print("you character is Shuna")
        else:
           print("please enter a valid input")

    else:
        print("please enter a valid input")

function()
