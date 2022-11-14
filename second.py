# this is a while loop for the first input

cookieAmount = 0
eggAmount = 2
flourAmount = 3
gsugarAmount = 1
bsugarAmount = 1
butterAmount = 1
chocChipAmount = 2
addExtra = 0

while cookieAmount < 1:
    cookieAmount = int(input("How many bakers: "))
    if cookieAmount < 1:
        print("enter a positive number")
if cookieAmount > 0:

        # each baker will make 24 cookies
        # all variables are measured in cups
        # all ingredients are measured for a set of 24 cookies
        # set new variables for multiplication

    eggT = eggAmount * cookieAmount
    flourT = flourAmount * cookieAmount
    gsugarT = gsugarAmount * cookieAmount
    bsugarT = bsugarAmount * cookieAmount
    butterT = butterAmount * cookieAmount
    ccT = chocChipAmount * cookieAmount
    randomVar = 'm'

    #this controls the input for the extra ingedients, making sure you input y or n
    while randomVar != 'y' or randomVar != 'n':
        randomVar = (input("Do you need extra ingredients?: (y/n)"))
        if randomVar == 'y':
            while addExtra < 1:
                addExtra = int(input("How many more batches (of 24) do you want?:"))
                if addExtra < 1:
                    print("please enter a positive number")
            if addExtra > 0:
                # these TTV variables are the "final" variable that will be printed after the addition of the extra set
                eggTTV = eggT + (eggAmount * addExtra)
                flourTTV = flourT + (flourAmount * addExtra)
                gsugarTTV = gsugarT + (gsugarAmount * addExtra)
                bsugarTTV = bsugarT + (bsugarAmount * addExtra)
                butterTTV = butterT + (butterAmount * addExtra)
                ccTTV = ccT + (chocChipAmount * addExtra)
            finalCookieCount = cookieAmount + addExtra

            output = "you will need {} eggs, {} flour, {} sugar, {} brown sugar, {} butter, {} Chocy Chip, for {} batches of cookies"
            print(output.format(eggTTV, flourTTV, gsugarTTV, bsugarTTV, butterTTV, ccTTV, finalCookieCount))
            break
        elif randomVar == 'n':
                # setting all the TTV and first set of variables equal to prevent bugs
            eggTTV = eggT
            flourTTV = flourT
            gsugarTTV = gsugarT
            bsugarTTV = bsugarT
            butterTTV = butterT
            ccTTV = ccT
            finalCookieCount = cookieAmount

            output = "you will need {} cups of eggs, {} cups of flour, {} cups of sugar, {} cups of brown sugar, {} cups of butter, {} cups of Chocy Chip, for {} batches of cookies"
            print(output.format(eggTTV, flourTTV, gsugarTTV, bsugarTTV, butterTTV, ccTTV, finalCookieCount))
            break
        else:
            print("Please enter valid input")


 # haha 69 lines of code :D