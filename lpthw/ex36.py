#Hunt the wumpus which i wrote during Hello Python book   
from random import choice, randint


from random import choice

cave_numbers = range(1,21)
player_location = choice(cave_numbers)
wumpus_col = 10
found = 0

#generate wumpus in cave_numbers
def wumpus_location(cave_numbers, wumpus_col)
    wumpus_list = []
    while i <= wumpus_col:
        if wumpus_list.count(i) != 1:
            wumpus_list.append(choice(cave_numbers))
            i += 1
    return wumpus_list

while player_location == wumpus_location:
    player_location = choice(cave_numbers)
    print "Welcome to Hunt the Wumpus!"
    print "You can see", len(caves), "caves"
    print "To play, just type the number"
    print "of the cave you wish to enter next"


while found:
    print "You are in cave", player_location
    if (player_location == wumpus_location - 1 or
                player_location == wumpus_location + 1):
        print "I smell a wumpus!"
    print "Which cave next?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
                    int(player_input) not in cave_numbers):
        print player_input, "is not a cave!"
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Aargh! You got eaten by a wumpus!"
            break

