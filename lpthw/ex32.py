the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'oranges', 'pears', 'banana']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for n in the_count:
    print 'count %d' % n

for fruit in fruits:
    print "A fruit of type: %s" % fruit

for i in change:
    print "i got %r" % i

elements = []

for i in range(0,6):
    print "Adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Elenent was: %d" % i
