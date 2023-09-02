import pytest
from src.phone import Phone

phone1 = Phone("Iphone", 150000, 70, 2)
phone2 = Phone("Samsung", 120000, 120, 2)
phone3 = Phone("Test", 0, 0, 2)


def test_attributes():
    assert phone2.name == 'Samsung'
    assert phone1.price == 150000
    assert phone1.quantity == 70
    assert phone2.number_of_sim == 2
    # with pytest.raises(ValueError):
    #     phone3.number_of_sim = 0


def test_repr_and_str():
    assert repr(phone1) == "Phone('Iphone', 150000, 70, 2)"
    assert repr(phone2) == "Phone('Samsung', 120000, 120, 2)"
    assert str(phone2) == 'Samsung'


def test_adding():
    assert phone1 + phone2 == 190
