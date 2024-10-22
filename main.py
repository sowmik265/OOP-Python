from item import Item
from keyboard import Keyboard

item1 = Keyboard("my item",1000,8)
item1.apply_discount()
print(item1.price)
