def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "That's enough for a party!\n"

print "We can give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or we can use variables from script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even use math inside too: "
cheese_and_crackers(10+20,5+6)

print "And we can combinate the too, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def last_ten(num):
    print "Now we count from %r to %r" % (num-10, num)
    for i in range(num-10, num+1):
        print i

last_ten(20)
