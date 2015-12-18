name = 'D\'artanyan'
age = 35 # i don't know exactly 
height = 185 # cm
#height cm -> inches
height_inc = height * 0.39

weight = 75 # kg
#weight kg -> pounds 
weight_pou = weight * 2.2

eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print 'Let\'s talk about %s.' % name
print 'He\'s %d cm tall.' % height
print 'He\'s %d kg heavy' % weight
print 'Actually that\'s not too heavy'
print 'He\'s got %s eyes and %s hair.' % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth 

#this line is tricky, try to get it exectly right
print "If i add %d, %d and %d I get %d." % (age, height, weight, age + height + weight)
print "In pounds / centemiters it will be like: %u pounds and %u inches" % (weight_pou, height_inc)

print('%r' % (2*'hi' + str(2.2)))
