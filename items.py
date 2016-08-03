class Item():
	"""The base class for all items"""
	def __init__(self, name, description, value, weight, size):
		self.name = name
		self.description = description
		self.value = value
		self.weight = weight
		self.size = size
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nWeight: %s\nSize: %s\n" % (self.name, self.description, self.value, self.weight, self.size)
		
class Weapon(Item):
	def __init__(self, name, description, value, weight, size, damage):
		self.damage = damage
		Item.__init__(self, name, description, value, weight, size)
		
	def __str__(self):
		return "%s\n=====\n%s\nValue: %s\nDamage: %s\n\n" % (self.name, self.description, self.value, self.damage)
		

class ItemContainer(Item):
	"""The Item Container"""
	def __init__(self, name, description, value, weight, size):
		if size == "small":
			self.maxSize = 3
		elif size == "medium":
			self.maxSize = 10
		else:
			self.maxSize = 20
			
		self.container = []
		
		Item.__init__(self, name, description, value, weight, size)
		
	def isEmpty():
		return len(self.container) == 0
		
	def addItem(self, item):
		self.container.append(item)
		
	def removeItem(self, item):
		self.container.remove(item)
		
	def __str__(self):
		description = "%s contains:\n" % (self.name)
		for item in self.container:
			description += item.__str__()
			description += "\n"
		return description
		
