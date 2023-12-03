import pytest
from src.item import Item, InstantiateCSVError

"""Здесь надо написать тесты с использованием pytest для модуля item."""

item1 = Item("Монитор", 15000, 70)
item2 = Item("Мышка", 1000, 120)
item3 = Item("Заглушка", 1000, 120)


def test_attributes():
    assert Item.pay_rate == 1.0
    assert item1.name == 'Монитор'
    assert item2.name == 'Мышка'
    assert item1.price == 15000
    assert item2.price == 1000
    assert item1.quantity == 70
    assert item2.quantity == 120


def test_calculate_total_price():
    assert item1.calculate_total_price() == float(15000 * 70)
    assert item2.calculate_total_price() == float(1000 * 120)


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 12000


def test_name_setter():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    item3.name = 'Беспроводная зарядка'
    assert item3.name == 'Беспроводн'


def test_count_positions():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_equality():
    assert Item.string_to_number('7.7') == 7


def test_repr_and_str():
    assert repr(item1) == "Item('Смартфон', 12000, 70)"
    assert str(item1) == 'Смартфон'
    assert repr(item3) == "Item('Беспроводн', 1000, 120)"
    assert str(item2) == 'Мышка'


def test_adding():
    assert item1 + item2 == 190


def test_instantiate_from_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('opa.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../src/items_6.csv')


