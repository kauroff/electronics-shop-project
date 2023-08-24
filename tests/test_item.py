from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

# TestCase#0 Pay_rate
assert Item.pay_rate == 1.0

# TestCase#1 Name
assert item1.name == 'Смартфон'
assert item2.name == 'Ноутбук'

# TestCase#2 Price
assert item1.price == 10000
assert item2.price == 20000

# TestCase#3 Quantity
assert item1.quantity == 20
assert item2.quantity == 5

# TestCase#4 Function total price
assert item1.calculate_total_price() == float(10000*20)
assert item2.calculate_total_price() == float(20000*5)

