from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Яблоко", 50, 100)
item2 = Item("Слива", 70, 50)

# TestCase#0 Pay_rate
assert Item.pay_rate == 1.0

# TestCase#1 Name
assert item1.name == 'Яблоко'
assert item2.name == 'Слива'

# TestCase#2 Price
assert item1.price == 50
assert item2.price == 70

# TestCase#3 Quantity
assert item1.quantity == 100
assert item2.quantity == 50

# TestCase#4 Function total price
assert item1.calculate_total_price() == float(50*100)
assert item2.calculate_total_price() == float(70*50)

