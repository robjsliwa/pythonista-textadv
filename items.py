class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value, weight, size):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		self.size = size
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nWeight: %s\nSize: %s" % (self.name, self.description, self.value, self.weight, self.size)
		
class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nDamage: %s\n" % (self.name, self.description, self.value, self.damage)
		
		
