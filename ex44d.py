class Parent(object):

	def override(self):
		print "PARENT override()"
		
	def implicit(self):
		print "PARENT implicit()"
		
	def altered(self):
		print "PARENT altered()"
		
class Child(Parent):

	def override(self):
		print "CHILD override()"
		
	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"
		
dad = Parent()  # assigns dad object to class Parent()
son = Child()   # assigns son object to class Child()

dad.implicit()  # prints out 'PARENT implicit()'
son.implicit()  # prints out 'PARENT implicit()'

dad.override()  # prints out 'PARENT override()'
son.override()  # prints out 'CHILD override()'

dad.altered()  # prints out 'PARENT altered()'
son.altered()  # prints out 'CHILD, BEFORE PARENT altered(), PARENT altered(), CHILD, AFTER PARENT altered()'

