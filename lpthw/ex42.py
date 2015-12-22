#animal is-a object
class Animal(object):
	pass

#is-a
class Dog(Animal):

	def __init__(self, name):
		#
		self.name = name


#is-a
class Cat(Animal):

	def __init__(self, name):
		#
		self.name = name


#is-a
class Person(object):

	def __init__(self, name, salery):
		#
		super(Employee, self).__init__(name)
		#
		self.salery = salery

#is-a
class Fish(object):
	pass

#is-a
class Salmon(Fish):
	pass

#is-a
class Halibut(Fish):
	pass


#rover is-a Dog
rover = Dor('Rover')

#is-a
satan = Cat('Satan')

#is-a
mary = Person('Mary')

#has-a
mary.pet = satan

#is-a
frank = Employee('Frank', 1200)

#has-a
frank.pet = rover

#is-a
flipper = Fish()

#is-a
crouse = Salmon()

#is-a
harry = Halibut()