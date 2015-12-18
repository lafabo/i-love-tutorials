#modules
from sys import argv
#parsing argv
script, filename = argv 
#assign file name
txt = open(filename)

print "Here's your file %r:" % filename 
#reading the file
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input("> ")
txt_again = open(file_again)

print txt_again.read()
txt_again(close)
