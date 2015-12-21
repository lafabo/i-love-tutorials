states = [
	'Oregon':'OR',
	'Florida':'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI'
]

cities = [
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
]

cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print '-'*10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

print '-'*10
print "Michigan's abbreviation is ", states['Michigan']
print "Florida has: ", states['Florida']

print "-"*10
for state, abbrev in states.items():
	print "%s has the city %s" % (abbrev, city)

print "-"*10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev.)