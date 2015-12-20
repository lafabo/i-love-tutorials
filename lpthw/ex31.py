print "You enter a dark room with two doors. Do you go through door 1 or door 2?"
door = raw_input("> ")

if door == '1':
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake"
    print "2. Scream at the bear"

    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off. Good job"
    elif bear == "2":
        print "The bear eats your legs off. Nice!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Ctulhu's retina"
    print "1. Blueberries"
    print "2. Yellow jacket clotherspins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input('> ')

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good Job!"
    else:
        print "The instanity rots your eyes into a pool of muck. Nice!"
else:
    print "So what to do?"
    print "1. fall at knife and die"
    print "2. Teleport to the home"
    choice = raw_input("> ")

    if choice == "1":
        print "You stumble around and fall on a knife and die."
    elif choice == "2":
        print "You win. At least i think so. You are mother's little winner."
    else:
        print "While you are waited you become eld"
