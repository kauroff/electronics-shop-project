from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Монитор", 15000, 70)
item2 = Item("Мышка", 1000, 120)

# TestCase#0 Pay_rate
assert Item.pay_rate == 1.0

# TestCase#1 Name
assert item1.name == 'Монитор'
assert item2.name == 'Мышка'

# TestCase#2 Price
assert item1.price == 15000
assert item2.price == 120

# TestCase#3 Quantity
assert item1.quantity == 70
assert item2.quantity == 120

# TestCase#4 Function total price
assert item1.calculate_total_price() == float(15000*70)
assert item2.calculate_total_price() == float(120*120)

