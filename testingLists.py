# i declare people as 8 here at the top so its easily visible and memorable, because it will be used later on
ppl = 8
# this is just printing a welcome statement to introduce the users to who is included in the database
print("Welcome to Slimepedia!"
      '\n' "We currently have information on", ppl,  "people!"
      '\n' "Their names are Rimuru, Guy, Milim, Luminous, Leon, Dagruel, Dino, Ramiris")

# this is for the overall class of Demon Lords
class DemonLord:

    # ye old classic def __init__(self)
    def __init__(self, first, last, age, rank, residence):
        self.first = first
        self.last = last
        self.age = age
        self.rank = rank
        self.residence = residence

# declaring the list
list = []

# this is adding to the list each variable of DemonLord which is set to all of these items it's basically a mixture
# of lists and class, allowing me to manipulate all the below items as lists rather than regular variables in a class

list.append(DemonLord('Rimuru', 'Tempest', 39, 'Catastrophe', 'Jura Tempest Federation'))
list.append(DemonLord('Guy', 'Crimson', 'Since the Dawn of Creation', 'Catastrophe', 'Ice Continent'))
list.append(DemonLord('Milim', 'Nava', 2000, 'Catastrophe', 'Capitol of the Forgotten Dragon'))
list.append(DemonLord('Luminous', 'Valentine', 2000, 'Disaster', 'Holy Empire Ruberios'))
list.append(DemonLord('Leon', 'Cromwell', 200, 'Disaster', 'El Dorado'))
list.append(DemonLord('Dagruel', 'None', 20000, 'Catastrophe', 'Barren Lands'))
list.append(DemonLord('Dino', 'None', 'Since the Dawn of Creation', 'Disaster', 'None'))
list.append(DemonLord('Ramiris', 'None', 50000, "Hero's Guide", 'Jura Tempest Federation'))

def learn():
    # setting the loop to false here triggers the while loop
    loop = False
    while loop == False:
        # user_input takes the user's input on who they want to learn about
        user_input = input("Enter the name of who you wish to learn more about: ").title()
        # this for loop reads through all the entries and see's if the input is equal to the user's input
        idx = 0
        for i in list:
            if user_input == list[idx].first or idx >= len(list):
                loop = user_input == list[idx].first
                print("Their first name is:", list[idx].first, "Their last name is:", list[idx].last, "Their age is:", list[idx].age,
                      "Their rank is", list[idx].rank, "Their currently live in:", list[idx].residence, sep='\n')
                break
            idx += 1
        if loop == False:
            print("please enter a valid input")

# this is a subclass of DemonLord to allow the input for new people all to be stored in the same list
class Newpeople(DemonLord):

        another1 = input("Do you want to add another person to the list? (y/n): ").lower()

        while another1 == 'y':
            # all the inputs for the list, still integrated into the class
            first, last, age, rank, residence = input("Enter First name, last name, age, rank, residence (in this order, no commas): ").title().split()
            # this adds the variables to this list as well as keeps them in the class
            list.append(DemonLord(first, last, age, rank, residence))
            # increase the number of people
            ppl += 1
            print("We now have information on", ppl, "total people!")
            another1 = input("Do you want to add another person to the list? (y/n): ").lower()

# this is the main program
learn()