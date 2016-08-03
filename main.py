from items import *

newItem1 = Item("Test1", "blah blas", "20", "10kg", "small")
print newItem1

newItem2 = Item("Test2", "blah blas", "20", "10kg", "small")
print newItem2

newItem3 = Item("Test3", "blah blas", "20", "10kg", "small")
print newItem3

weapon1 = Weapon("Sword", "Cool sword", "50", "12kg", "small", "12")
print weapon1

newContainer = ItemContainer("TestContainer", "blah blas", "20", "10kg", "small")
newContainer.addItem(newItem1)
newContainer.addItem(newItem2)
newContainer.addItem(weapon1)

print newContainer
