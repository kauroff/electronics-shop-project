class Mixin:
    language = 'EN'

    def __init__(self, language='EN'):
        self.language = language

    def change_lang(self):
        if Mixin.language == 'EN':
            Mixin.language = 'RU'
        elif Mixin.language == 'RU':
            Mixin.language = 'EN'


class Keyboard(Mixin):
    def __init__(self, name: str, price: int, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}'

    @property
    def language(self):
        return self.language
