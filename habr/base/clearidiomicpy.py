# cycle

for i in xrange(6):
	print i**2

print "\n\n\n"

# cycle with list
colors = ['red', 'blue', 'green', 'yellow']
for color in colors:
	print color,

print '\n'
for color in reversed(colors):
	print color

print 'enumerated'
for i, color in enumerate(colors):
	print i, '->', color

print "\n\n\n"

# cycle with 2 lists
names = ['joe', 'bob', 'bart', 'matt']
colors = ['red', 'blue', 'green', 'yellow']
for name, color in zip(names, colors):
	print name, '->', color

print "\n\n\n"

# quick sort
colors = ['red', 'blue', 'green', 'yellow']
print sorted(colors, key=len)

print "\n\n\n"

# cycle with dict
mydict = {'A':'Adam', 'B':'Bob', 'C':'Charlie', 'R':'Ronny', 'Z':'Zed'}

print mydict
#       -> best for editing dict is editing by keys
for k in mydict.keys():
	if k.startswith('R'):
		del mydict[k]
print mydict

# -
# fast:
for k,v in mydict.items():
	print k, '->', v

# fastest with iterator
for k, v in mydict.iteritems():
	print k, '->', v

print "\n\n\n"

# counting elements in the dict
colors = ['red', 'blue', 'green', 'yellow']
d = {}
for color in colors:
	d[color] = d.get(color, 0)+1

print d
#using defaultdict
print 'using defaultdict'
from collections import defaultdict
d = defaultdict(int)
for color in colors:
	d[color] += 1
print d

print "\n\n\n"

# group list elements

names = ['ray', 'rachel', 'matt', 'roger', 'betty', 'bob', 'judith']
d = defaultdict(list)
print names
for name in names:
	key = len(name)
	d[key].append(name)

print d