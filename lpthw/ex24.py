print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do\n newlines and \ttabs.'

poem = """
\tThe lovely world
with logic so firmy planted
cannot discern \n the needs of love
nor comprehed passion from intuition
and requires an explanation
\n\twhere there is none
"""
print "--------\n" + poem + "\n--------"

five = 10 - 2 + 3 - 6

print "This should be five: %s" % five

def secret_formula(started):
    jeally_beans = started * 500
    jars = jeally_beans / 1000
    crates = jars / 100
    return jeally_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point /= 10

print "We can also do that this way: "
print "We'd have %d beans, %d jars, and %d crates " % secret_formula(start_point)
