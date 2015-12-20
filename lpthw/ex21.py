def add(a, b):
    print "Adding %d + %d " % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multipying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d " % (a, b)
    return a / b


print "Let's do some math!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age %d, height %d, weight %d and iq: %d" % (age, height, weight, iq)


print "Here is the puzzle"
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

div2 = divide(iq, 2)
mul2 = multiply(weight, div2)
sub2 = subtract(height, mul2)
what2 = add(age, sub2)

print "\n\nAlternative: %r" % what2


print "Something: %r" % (divide(subtract(5, 8), (multiply(5, add(9, 2)))))
