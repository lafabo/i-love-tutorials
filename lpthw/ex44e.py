# composition


class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"


class Child(object):

	def __init__(self):
		self.other = Other()

	def override(self):
		print "CHILD override()"

	def implicit(self):
		print "CHILD implicit()"

	def altered(self):
		print "CHILD BEFORE altered()"
		self.other.altered()
		print "CHILD AFTER altered()"


son = Child()

son.implicit()
son.override()
son.altered()
