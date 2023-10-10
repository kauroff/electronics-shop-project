from src.item import Item


class Mixin:
    language = 'EN'

    @property
    def language(self):
        return self.language

    def __str__(self):
        return f'{self.language}'

    @language.setter
    def language(self, language):
        self.change_lang()

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'


class Keyboard(Mixin):
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}'
