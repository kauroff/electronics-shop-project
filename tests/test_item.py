from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Монитор", 15000, 70)
item2 = Item("Мышка", 1000, 120)
item3 = Item("Заглушка", 1000, 120)

# TestCase#0 Pay_rate
assert Item.pay_rate == 1.0

# TestCase#1 Name
assert item1.name == 'Монитор'
assert item2.name == 'Мышка'

# TestCase#2 Price
assert item1.price == 15000
assert item2.price == 1000

# TestCase#3 Quantity
assert item1.quantity == 70
assert item2.quantity == 120

# TestCase#4 Function total price
assert item1.calculate_total_price() == float(15000*70)
assert item2.calculate_total_price() == float(1000*120)

# TestCase#5 name.getter
assert item1.name == 'Монитор'

# TestCase#6 name.setter
item1.name = 'Смартфон'
assert item1.name == 'Смартфон'
item3.name = 'Беспроводная зарядка'
assert item3.name == 'Беспроводн'

# TestCase#7 Count positions
Item.instantiate_from_csv('../src/items.csv')
assert len(Item.all) == 5

# TestCase#8 Equal
assert Item.string_to_number('7.7') == 7

