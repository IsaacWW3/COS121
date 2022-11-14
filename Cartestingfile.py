#importing this allows for me to generate random numbers later on
import random

# this function calculates the car's speed
def car_speed():
    global carMph
    global distance
    # inputs to allow the calculation of how fast your car is going
    distance = int(input("How far are you going? (miles): "))
    carTime = int(input("How long do you want it to take? (hours): "))

    # this calculates the miles per hour your car is going (distance divided by time)
    carMph = distance / carTime
    # this prints the miles per hour your car is going for the user
    print("You are going", carMph, "mph")

# a function that makes sure you are on the right side of the road
def road_side():

    # side is set to 'm' to trigger the while loop
    side = 'm'
    # the while loop is to allow input for what side of the road the car is on
    while side != 'l' or side != 'r':
        side = input("What side of the road are you on? (l/r): ")
        if side == 'l':
            print("Your car will now shift to the right side of the road")
            break
        elif side == 'r':
            print("Your car is on the correct side of the road")
            break
        else:
            print("Please enter a valid input")


# this function will check the speed against the speed limit to make sure you don't go too fast
def speed_check():
    # to carry over the value of carMph from car_speed(), you have to re-declare it as global inside the next function
    global carMph
    global speedLimit

    speedLimit = int(input("What is the speed limit? (Mph): "))
    # this uses a while loop nested inside of an if statement to calculate how much to speed up
    if carMph > speedLimit:
        print("Car speed has been lowered to meet speed limit")
        # im goint to be honest, i dont understand why the break comes before the math operator, but thats how the syntax is described
        while carMph > speedLimit:
           # print(carMph)
            if carMph == speedLimit:
                break
            carMph -= 1
        print("Your new speed is", carMph, "Mph")
        # this elif is used to calculate the difference between the speed limit and car speed to tell the driver to speed up
    elif speedLimit > carMph:
        speedDifference = speedLimit - carMph
        print("You can speed up", speedDifference, "Mph")
        while carMph < speedLimit:
            # print(carMph)
            if carMph == speedLimit:
                break
            carMph += 1
        print("Car is now going", carMph, "Mph")
        # this is else is the failsafe incase the driver is already going the speedlimit
    else:
        print("Continue driving the speed limit")


def continue_move():

    global carMph
    global speedLimit
    # this statement allows the car to accelerate again
    # the driver must follow road laws so they will only be driving the speed limit
    carMph = speedLimit
    # getting the time from the user to calculate their acceleration
    time = float(input("How fast did you accelerate to the speed limit? (seconds): "))
    # this is the formula for acceleration
    acceleration = (carMph - 0) / time

    print("You sped up at a rate of", acceleration, "miles per second")
    print("You are now driving at", carMph, "mph")

# this function calculates how the car will stop at a stop sign
def impending_obstacle():
    # im declaring carMph as a global here in hopes to fix the current bugs with this function
    global carMph

    # declaring stopSign as 'm' up here allows the while statement to begin to run
    obstacle = 'm'
    # this while statement is to allow for a feedback loop when the user doesn't enter a proper input for the string
    while obstacle != 'y' or obstacle != 'n':

        obstacle = input("Do you see an obstacle? (y/n): ")
        if obstacle == 'y':
            # calculating the deceleration
            def car_must_stop():

                global carMph
                # takes the input for how far the vehicle went while breaking
                distance_covered = float(input("How much distance was covered during deceleration (yards)?: "))
                # this is the formula for deceleration, i input final velocity at 0 assuming we are coming to a complete stop
                # this equation could be used to calculate deceleration for regular breaking in a vehicle as well
                deceleration = (0 - carMph ** 2) / (2 * distance_covered)

                print("You decelerated at a rate of", deceleration, "yps (yards per second)")

            car_must_stop()

            continue_move()
            break
        # the ^ second use of break above is for the first while loop, where obstacle is either y or n
        # below the elif is saying if "n" then the car will just continue at the current speed
        elif obstacle == 'n':
            print("Your car will continue at", carMph, "Mph")
            break
        else:
            print("please enter a valid input")


# a function for calculating what to do when turning left
def turning_left():

    left = input("Are you turning left? (y/n): ")
    # the if statement below checks to see if there is oncoming traffic before turning left
    if left == 'y':
        traffic = input("is there oncoming traffic? (y/n): ")
        if traffic == 'y':
            print("You wait until traffic goes by to turn left")
        elif traffic == 'n':
            print("You may turn left now")
        else:
            print("Please enter a valid input")
    elif left == 'n':
        print("Your car continues straight")
    else:
        print("please enter a valid input")



#traffic circle detection and rules function

def traffic_circle():

    approach_circle = input("Are you approaching a traffic circle? (y/n): ")
    if approach_circle == 'y':
        print("You must yield to the circle traffic")
        #here this allows you to input how many lanes (for simplicity sake i only said 1 or 2 lanes)
        lanes = int(input("Is this a one or two lane traffic circle? (1,2): "))
        if lanes == 1:
            print("You will yield to traffic and drive around the circle such as a normal human being would (that means hit the center curb at least once)")
        elif lanes == 2:
            l_or_r = input("Are you in the right of left lane? (l or r): ")
            if l_or_r == 'l':
                print("you stay in the left lane until you are able to leave at the proper exit or merge right")
            elif l_or_r == 'r':
                print("you stay in the right lane until you are able to exit the circle")
            else:
                print("please enter a valid input")
        else:
            print("please enter either 1 or 2 (these are valid inputs)")
    elif approach_circle == 'n':
        print("You continue driving as normal")
    else:
        print("please enter a valid input")
# i feel like most of this code in this function is self explanitory if you read it


# a function that calculates miles per gallon
def miles_per_gallon():

    global distance

    # this is the input for the gallons used during the trip
    gallons = int(input("How many gallons did your car use for your trip: "))
    # this is the formula for calculating miles per gallon
    mpg = distance / gallons
    print("Your car gets", round(mpg), "miles per gallon")

# this function is for dealing with slow vehicles
def slow_vehicle():
    car_slow = input("Does your car have to move slower than the speed limit? (y/n)")
    if car_slow == 'y':
        print("Your car will remain as far right on the road as it can to allow other vehicles to pass")
    elif car_slow == 'n':
        print("You car will continue driving normally down the road")
    else:
        print("please enter a valid input")

# this function generates a random number for another function
def random_num():
    global value
    value = random.randint(1, 5)
    # print(value)

# this takes the random value generated from random_num, and runs a function for an event based off of the number given
def events_happen():
    global value
    if value == 1:
        impending_obstacle()
    elif value == 2:
        road_side()
    elif value == 3:
        slow_vehicle()
    elif value == 4:
        turning_left()
    elif value == 5:
        traffic_circle()


# this function pairs the num and events functions to make it more concise
def num_events():
    random_num()
    events_happen()


# this function runs car_speed and speed_check first, allowing the function to get the needed variables
def final():
    car_speed()
    speed_check()
    global distance

    #then this function has a while loop to run the random events every mile, taking a mile off the total amount you want to travel
    while distance > 0:
        num_events()
        distance -= 1
        if distance > 0:
            print("you have", distance, "miles left to travel")
        elif distance == 0:
            print("You have arrived at your destination!!")
            break

# this function "is" the car, it runs all the programs needed ending by calculating the miles per gallon at the end of the trip
def main():
    final()
    miles_per_gallon()

main()