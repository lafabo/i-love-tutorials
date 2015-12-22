states = [
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
]
# create a basic set of states and some cities in them
cities = [
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
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
	print "%s has the city %s" % (abbrev, city)

print "-"*10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print "-"*10
state = states.get('Texas', none)

if not state:
	print "Sorry, no Texas"

city = cities.get('TX', 'Does Not Exist')
print "the city for the state 'TX' is %s" % city