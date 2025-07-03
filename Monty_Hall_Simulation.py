
import random

#This program was made for demonstration purposes on my YouTube channel. Some code may be unoptimized, but I feel it helps non-coders understand the logic.
#In regards to my portfolio, it is being used to show that I have familiarity with python, but is not meant to showcase advanced logic or mathematical skills.

# wins
wins = 0
# games
games = 0
# Run 10,000 times.

while games < 10000:
    # Make a list of 1-3 
    doors = [1, 2, 3]
    removableDoors = doors.copy();
    
    # Pick a value between 1 and 3. This is the winning door
    winningDoor = random.randint(1, 3)

    # Simulate user picking a door by selecting a random value of 1-3
    userDoor = random.randint(1, 3)

    # Remove door that is neither the contestant's door NOR the winning door. (Necessary due to line 1, but not normally)
    
    try:
        #exclude winning door
        removableDoors.remove(winningDoor)
        #exclude the user's choice
        removableDoors.remove(userDoor)
    except ValueError:
        pass  # Value not found, no problem

        #At this point, we will have one or two options of doors we can remove, pick a random one.
    removedDoor = random.choice(removableDoors)


    try:
        #actually remove the door
        doors.remove(removedDoor)
    except ValueError:
        pass  # Value not found, no problem


    # contestant switches value.
        #While unorthodx, this logic will be useful when we make derivative projects.
    userDoorOld = userDoor
    userDoor = random.choice(doors)
    while userDoor == userDoorOld:
        userDoor = random.choice(doors)
    

    # if switched value == winning door, wins ++;
    if userDoor == winningDoor:
        wins+=1
    # games++;
    games += 1

# print wins, / games."%",
        #Note to self: need to convert to strings before displaying
print ("Games won: " + str(wins) + "\nTotal Games: " + str(games) + "\n" + str(wins/games *100) +"%")

