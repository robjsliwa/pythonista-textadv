class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s" % (self.name, self.description, self.value)
		
class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nDamage: %s\n" % (self.name, self.description, self.value, self.damage)
		
		
