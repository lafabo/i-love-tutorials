from sys import argv

script, filename = argv

print "We're going to erase %r." % filename 
print "If you don't want that hit CTRL-C (^C)"
print "If you want that hit RETURN"

raw_input("?")

print "Opening the file..."

target = open(filename, "w")

print "Trucationg the file."
target.truncate()

print "Now i'm going to write some lines in the file"
line1 = raw_input("line1")
line2 = raw_input("line2")
line3 = raw_input("line3")

target.write(line1 + "\n" + line2 + "\n" + line3)

print "And finally we close it!"
target.close()
