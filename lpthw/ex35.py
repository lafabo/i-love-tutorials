from sys import exit

def gold_room():
    print "This room is full of gold. How much you take?"
    nextr = raw_input("> ")
    if 0 in nextr or 1 in nextr:
        how_much = int(next)
    else:
        dead("Man, learn to type a numbers")

    if how_much < 50:
        print "Nice, you are not greedy, you win"
        exit(0)
    else:
        dead("You are greedy")

def bear_room():
    print "there is a bear here."
    print "the bear has a bunch of honey"
    print "the fat bear is in front of another door"
    print "how are you going to move the bear?"
    bear_moved = False

    while True:
        nextr = raw_input("> ")

        if nextr == "take honey":
            dead("The bear looks at you then kill ytou")
        elif nextr == "taunt bear" and not bear_moved:
            print "the bear has moved from the door. You can go through it now"
            bear_moved = True
        elif nextr == "taunt bear" and bear_moved:
            dead("Bear got a frag")
        elif nextr == "open door" and bear_moved:
            gold_room()
        else:
            print "i don't know wha that means"

def ctulhu_room():
    print "Here you see the great evil Ctulhu"
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for you life or eat your head?"

    nextr = raw_input("> ")
    if "flee" in nextr:
        start()
    elif "head" in nextr:
        dead("At least that was tasty")
    else:
        ctulhu_room()

def dead(why):
    print why, "Good Job"
    exit(0)

def start():
    print "You are in the dark room"
    print "There is a door to your right and left"
    print "Which one do you take?"

    nextr = raw_input("> ")
    if nextr == 'left':
        bear_room()
    elif nextr == 'right':
        ctulhu_room()
    else:
        dead("You stumble until you starve")

start()
