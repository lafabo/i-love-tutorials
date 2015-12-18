from sys import argv

script, user_name = argv
promt = "> "

print "Hi %s, i'm the %s script" % (user_name, script)
print "I'd like to ask you a few questions"
print "Do you like me %s?" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name 
lives = raw_input(promt)

print "What kind of computer do you have?"
comp = raw_input(promt)

print """
Alright, so you said %r about liking me/
You live in %r.
And you have a %r computer
""" % (likes, lives, comp)
