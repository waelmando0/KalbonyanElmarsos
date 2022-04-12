# (Shared, Class) / Static Variable:
#  Variable that is shared across all object in a class.

# Just define it inside the class
# but out side the _ init_ function:

class Spaceship():

	# class  static variables
	toughness = 0.8

	def _init_(self):

		# instance variables
		self.callsign = ''
		self._shieldStrength = 100

	# other code omitted